"""
Main Training Script
-------------------
This script orchestrates the complete model training pipeline:
1. Data preprocessing
2. Model training with hyperparameter tuning
3. Model evaluation
4. Model saving
"""

import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from preprocessing import DataPreprocessor
from model import ChurnPredictor


def main():
    """
    Main function to run the complete training pipeline.
    """
    print("\n" + "="*80)
    print("TELECOM CUSTOMER CHURN PREDICTION - MODEL TRAINING PIPELINE")
    print("="*80)
    
    # Step 1: Data Preprocessing
    print("\n[STEP 1/4] Data Preprocessing")
    preprocessor = DataPreprocessor('telecom_churn.csv')
    data = preprocessor.preprocess_pipeline(test_size=0.2, random_state=42)
    
    # Step 2: Model Training
    print("\n[STEP 2/4] Model Training")
    predictor = ChurnPredictor(random_state=42)
    predictor.train_model(
        data['X_train'], 
        data['y_train'], 
        hyperparameter_tuning=True
    )
    
    # Step 3: Model Evaluation
    print("\n[STEP 3/4] Model Evaluation")
    metrics = predictor.evaluate_model(
        data['X_test'], 
        data['y_test'], 
        feature_names=data['feature_names']
    )
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    predictor.plot_confusion_matrix(metrics['confusion_matrix'])
    predictor.plot_roc_curve(data['X_test'], data['y_test'])
    predictor.plot_feature_importance()
    
    # Step 4: Save Model
    print("\n[STEP 4/4] Saving Model")
    predictor.save_model('models/churn_model.pkl')
    
    # Summary
    print("\n" + "="*80)
    print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
    print("="*80)
    print("\nModel Performance Summary:")
    print(f"  Accuracy:  {metrics['accuracy']:.4f}")
    print(f"  Precision: {metrics['precision']:.4f}")
    print(f"  Recall:    {metrics['recall']:.4f}")
    print(f"  F1-Score:  {metrics['f1_score']:.4f}")
    print(f"  ROC-AUC:   {metrics['roc_auc']:.4f}")
    
    print("\nSaved Files:")
    print("  ✓ models/churn_model.pkl")
    print("  ✓ models/scaler.pkl")
    print("  ✓ models/feature_names.pkl")
    print("  ✓ models/confusion_matrix.png")
    print("  ✓ models/roc_curve.png")
    print("  ✓ models/feature_importance.png")
    
    print("\nNext Steps:")
    print("  1. Review the model performance metrics")
    print("  2. Check the visualization plots in the models/ directory")
    print("  3. Run the Flask app to test predictions: python app.py")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
