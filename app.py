"""
Flask Web Application for Churn Prediction
------------------------------------------
This application provides a web interface for predicting customer churn
using the trained logistic regression model.
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import joblib
import os
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Global variables for model and preprocessing objects
model_data = None
scaler = None
feature_names = None


def load_model_artifacts():
    """
    Load the trained model, scaler, and feature names.
    """
    global model_data, scaler, feature_names
    
    try:
        # Load model
        model_path = 'models/churn_model.pkl'
        if os.path.exists(model_path):
            model_data = joblib.load(model_path)
            print("✓ Model loaded successfully")
        else:
            print(f"⚠ Warning: Model file not found at {model_path}")
            print("Please run 'python train.py' first to train the model.")
            return False
        
        # Load scaler
        scaler_path = 'models/scaler.pkl'
        if os.path.exists(scaler_path):
            scaler = joblib.load(scaler_path)
            print("✓ Scaler loaded successfully")
        else:
            print(f"⚠ Warning: Scaler file not found at {scaler_path}")
            return False
        
        # Load feature names
        feature_names_path = 'models/feature_names.pkl'
        if os.path.exists(feature_names_path):
            feature_names = joblib.load(feature_names_path)
            print("✓ Feature names loaded successfully")
            print(f"Expected features: {feature_names}")
        else:
            print(f"⚠ Warning: Feature names file not found at {feature_names_path}")
            return False
        
        return True
    
    except Exception as e:
        print(f"✗ Error loading model artifacts: {str(e)}")
        traceback.print_exc()
        return False


@app.route('/')
def home():
    """
    Render the home page with the prediction form.
    """
    return render_template('index.html', feature_names=feature_names)


@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint for making predictions.
    Accepts JSON data with customer features.
    """
    try:
        # Check if model is loaded
        if model_data is None or scaler is None or feature_names is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please train the model first.'
            }), 500
        
        # Get data from request
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        # Extract features in the correct order
        features = []
        missing_features = []
        
        for feature_name in feature_names:
            if feature_name in data:
                try:
                    features.append(float(data[feature_name]))
                except (ValueError, TypeError):
                    return jsonify({
                        'success': False,
                        'error': f'Invalid value for feature: {feature_name}'
                    }), 400
            else:
                missing_features.append(feature_name)
        
        if missing_features:
            return jsonify({
                'success': False,
                'error': f'Missing required features: {", ".join(missing_features)}'
            }), 400
        
        # Convert to numpy array and reshape
        features_array = np.array(features).reshape(1, -1)
        
        # Scale features
        features_scaled = scaler.transform(features_array)
        
        # Make prediction
        prediction = model_data['model'].predict(features_scaled)[0]
        probability = model_data['model'].predict_proba(features_scaled)[0]
        
        # Prepare response
        result = {
            'success': True,
            'prediction': int(prediction),
            'prediction_label': 'Churn' if prediction == 1 else 'Not Churn',
            'probability': {
                'not_churn': round(float(probability[0]) * 100, 2),
                'churn': round(float(probability[1]) * 100, 2)
            },
            'input_features': data
        }
        
        return jsonify(result), 200
    
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': f'Prediction error: {str(e)}'
        }), 500


@app.route('/api/info', methods=['GET'])
def model_info():
    """
    API endpoint to get model information.
    """
    try:
        if model_data is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded'
            }), 500
        
        info = {
            'success': True,
            'model_type': 'Logistic Regression',
            'features': feature_names,
            'num_features': len(feature_names),
            'best_params': model_data.get('best_params', {}),
            'timestamp': model_data.get('timestamp', 'N/A')
        }
        
        return jsonify(info), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_data is not None,
        'scaler_loaded': scaler is not None
    }), 200


if __name__ == '__main__':
    print("\n" + "="*80)
    print("TELECOM CHURN PREDICTION - WEB APPLICATION")
    print("="*80)
    
    # Load model artifacts
    print("\nLoading model artifacts...")
    if load_model_artifacts():
        print("\n✓ All artifacts loaded successfully!")
        print("\nStarting Flask server...")
        print("="*80)
        print("\n🌐 Application running at: http://localhost:5000")
        print("📊 Access the prediction interface in your web browser")
        print("\nPress CTRL+C to stop the server\n")
        
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("\n✗ Failed to load model artifacts.")
        print("\n⚠ Please run the following command first:")
        print("   python train.py")
        print("\nThis will train the model and generate the required files.")
