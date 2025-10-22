# Project Architecture

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE (Browser)                      │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Frontend (HTML/CSS/JavaScript)                   │  │
│  │  • Input Form with Validation                                 │  │
│  │  • Real-time Predictions Display                              │  │
│  │  • Probability Visualization                                  │  │
│  │  • Personalized Recommendations                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↕ HTTP/AJAX
┌─────────────────────────────────────────────────────────────────────┐
│                      FLASK WEB APPLICATION                           │
│                                                                       │
│  ┌──────────────────┐  ┌────────────────┐  ┌───────────────────┐  │
│  │  Route Handlers  │  │  API Endpoints │  │  Error Handling   │  │
│  │  • /             │  │  • /predict    │  │  • Validation     │  │
│  │  • /health       │  │  • /api/info   │  │  • Try/Except     │  │
│  └──────────────────┘  └────────────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────────┐
│                     MODEL PREDICTION PIPELINE                        │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 1. Input Validation → 2. Feature Scaling → 3. Prediction     │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌────────────────┐  ┌──────────────────┐  ┌──────────────────┐   │
│  │ Scaler Object  │  │  Trained Model   │  │ Feature Mappings │   │
│  │ (scaler.pkl)   │  │(churn_model.pkl) │  │(feature_names.pkl)│   │
│  └────────────────┘  └──────────────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
┌──────────────┐
│  Raw CSV     │
│  Dataset     │
│ (3333 rows)  │
└──────┬───────┘
       │
       ↓
┌──────────────────────────────────────┐
│  Data Preprocessing Pipeline         │
│  • Load data (pandas)                │
│  • Quality checks                    │
│  • Train-test split (80-20)          │
│  • Feature scaling (StandardScaler)  │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  Model Training                       │
│  • Hyperparameter tuning (GridCV)    │
│  • Logistic Regression training      │
│  • Cross-validation                  │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  Model Evaluation                     │
│  • Accuracy, Precision, Recall       │
│  • ROC-AUC, F1-Score                 │
│  • Confusion Matrix                  │
│  • Feature Importance                │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  Model Artifacts (Saved)              │
│  • churn_model.pkl                   │
│  • scaler.pkl                        │
│  • feature_names.pkl                 │
│  • Visualization plots               │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  Deployment                           │
│  • Flask API                         │
│  • Web Interface                     │
│  • Real-time Predictions             │
└──────────────────────────────────────┘
```

## Module Dependencies

```
app.py (Flask Application)
    ├── loads: churn_model.pkl
    ├── loads: scaler.pkl
    ├── loads: feature_names.pkl
    ├── uses: templates/index.html
    └── uses: static/ (CSS, JS)

train.py (Training Pipeline)
    ├── imports: src/preprocessing.py
    ├── imports: src/model.py
    └── creates: models/*.pkl, models/*.png

src/preprocessing.py
    ├── uses: pandas, numpy, sklearn
    ├── reads: telecom_churn.csv
    └── saves: scaler.pkl, feature_names.pkl

src/model.py
    ├── uses: sklearn, matplotlib, seaborn
    └── saves: churn_model.pkl, visualizations

notebooks/01_EDA_and_Analysis.ipynb
    ├── reads: telecom_churn.csv
    └── generates: exploratory insights
```

## Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND LAYER                           │
├─────────────────────────────────────────────────────────────┤
│  HTML5 │ CSS3 │ JavaScript ES6+ │ Font Awesome              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                     BACKEND LAYER                            │
├─────────────────────────────────────────────────────────────┤
│  Flask 3.0.0 │ Flask-CORS │ Python 3.10+                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  MACHINE LEARNING LAYER                      │
├─────────────────────────────────────────────────────────────┤
│  Scikit-learn │ Logistic Regression │ GridSearchCV          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   DATA PROCESSING LAYER                      │
├─────────────────────────────────────────────────────────────┤
│  Pandas 2.1.4 │ NumPy 1.24.3 │ StandardScaler               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   VISUALIZATION LAYER                        │
├─────────────────────────────────────────────────────────────┤
│  Matplotlib 3.8.2 │ Seaborn 0.13.0                          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   PERSISTENCE LAYER                          │
├─────────────────────────────────────────────────────────────┤
│  Joblib 1.3.2 │ PKL Files                                   │
└─────────────────────────────────────────────────────────────┘
```

## Request-Response Flow

```
User Action: Submit Form
        ↓
JavaScript: Collect & Validate Input
        ↓
AJAX POST: /predict endpoint
        ↓
Flask: Receive JSON data
        ↓
Validation: Check all required fields
        ↓
        ├─ Error? → Return error JSON → Display error message
        ↓
        └─ Valid? → Continue
               ↓
Feature Extraction: Map to model features
        ↓
Feature Scaling: StandardScaler.transform()
        ↓
Model Prediction: LogisticRegression.predict()
        ↓
Probability Calculation: predict_proba()
        ↓
Response Building: Create JSON response
        ↓
Flask: Return JSON to client
        ↓
JavaScript: Parse response
        ↓
        ├─ Success? → Display results, probabilities, recommendations
        └─ Error? → Display error message
```

## File Organization

```
Logistic_Regression_Project/
│
├── 📁 notebooks/              # Jupyter notebooks for analysis
│   └── 01_EDA_and_Analysis.ipynb
│
├── 📁 src/                    # Source code modules
│   ├── preprocessing.py       # Data preprocessing logic
│   └── model.py              # Model training & evaluation
│
├── 📁 models/                 # Saved model artifacts (generated)
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── feature_importance.png
│
├── 📁 templates/              # HTML templates
│   └── index.html
│
├── 📁 static/                 # Static assets
│   ├── style.css
│   └── script.js
│
├── 📄 telecom_churn.csv       # Dataset
├── 📄 train.py                # Training pipeline script
├── 📄 app.py                  # Flask application
├── 📄 requirements.txt        # Python dependencies
├── 📄 .gitignore             # Git ignore rules
│
├── 📄 README.md              # Main documentation
├── 📄 QUICKSTART.md          # Quick start guide
├── 📄 RESUME_GUIDE.md        # Resume talking points
├── 📄 API_TESTING.md         # API testing examples
├── 📄 ARCHITECTURE.md        # This file
│
├── 📄 setup.bat              # Windows setup script
└── 📄 run.bat                # Windows run script
```

## Model Training Pipeline

```
START
  ↓
Load Data (telecom_churn.csv)
  ↓
Data Quality Check
  ├─ Check missing values
  ├─ Check duplicates
  └─ Validate data types
  ↓
Feature Engineering
  ├─ Separate X (features) and y (target)
  └─ Store feature names
  ↓
Train-Test Split (80-20, stratified)
  ↓
Feature Scaling
  ├─ Fit StandardScaler on training data
  └─ Transform both train and test sets
  ↓
Hyperparameter Tuning
  ├─ Define parameter grid
  │   ├─ C: [0.001, 0.01, 0.1, 1, 10, 100]
  │   ├─ penalty: ['l1', 'l2']
  │   └─ solver: ['liblinear', 'saga']
  ├─ GridSearchCV with 5-fold CV
  └─ Select best parameters
  ↓
Model Training
  └─ Train LogisticRegression with best params
  ↓
Model Evaluation
  ├─ Accuracy
  ├─ Precision
  ├─ Recall
  ├─ F1-Score
  ├─ ROC-AUC
  └─ Confusion Matrix
  ↓
Visualization
  ├─ Confusion Matrix heatmap
  ├─ ROC Curve
  └─ Feature Importance
  ↓
Save Artifacts
  ├─ churn_model.pkl
  ├─ scaler.pkl
  ├─ feature_names.pkl
  └─ Visualization PNGs
  ↓
END
```

## Deployment Options

```
┌──────────────────────────────────────────────────────────┐
│              CURRENT: Local Development                   │
│  • Flask development server                              │
│  • localhost:5000                                        │
│  • Suitable for: Testing, Development, Demo              │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│              OPTION 1: Production Server                  │
│  • Use Gunicorn or uWSGI                                 │
│  • Nginx as reverse proxy                                │
│  • Deploy on: AWS EC2, DigitalOcean, Linode             │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│              OPTION 2: Cloud Platform (PaaS)              │
│  • Heroku                                                │
│  • Google Cloud Run                                      │
│  • AWS Elastic Beanstalk                                 │
│  • Azure App Service                                     │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│              OPTION 3: Containerization                   │
│  • Docker container                                      │
│  • Kubernetes orchestration                              │
│  • Deploy on: Any cloud provider                         │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│              OPTION 4: Serverless                         │
│  • AWS Lambda + API Gateway                              │
│  • Google Cloud Functions                                │
│  • Azure Functions                                       │
└──────────────────────────────────────────────────────────┘
```
