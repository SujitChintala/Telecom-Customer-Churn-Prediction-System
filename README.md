# 📊 Telecom Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive machine learning project that predicts customer churn in the telecom industry using Logistic Regression. This project includes a complete data science pipeline from EDA to deployment with an interactive web interface.

## 🎯 Project Overview

Customer churn prediction is crucial for telecom companies to identify customers likely to leave and take proactive retention measures. This project implements a production-ready machine learning solution with:

- **Exploratory Data Analysis (EDA)** with comprehensive visualizations
- **Data Preprocessing Pipeline** with feature scaling and validation
- **Logistic Regression Model** with hyperparameter tuning
- **Web Application** with Flask backend and modern frontend
- **Model Evaluation** with multiple performance metrics
- **Interactive UI** for real-time predictions

## 📁 Project Structure

```
Logistic_Regression_Project/
│
├── notebooks/
│   └── 01_EDA_and_Analysis.ipynb       # Exploratory Data Analysis
│
├── src/
│   ├── preprocessing.py                 # Data preprocessing module
│   └── model.py                         # Model training and evaluation module
│
├── models/
│   ├── churn_model.pkl                  # Trained model (generated)
│   ├── scaler.pkl                       # Fitted scaler (generated)
│   ├── feature_names.pkl                # Feature names (generated)
│   ├── confusion_matrix.png             # Confusion matrix plot (generated)
│   ├── roc_curve.png                    # ROC curve plot (generated)
│   └── feature_importance.png           # Feature importance plot (generated)
│
├── templates/
│   └── index.html                       # Web interface template
│
├── static/
│   ├── style.css                        # CSS styling
│   └── script.js                        # JavaScript for interactivity
│
├── telecom_churn.csv                    # Dataset
├── train.py                             # Main training script
├── app.py                               # Flask web application
├── requirements.txt                     # Python dependencies
├── .gitignore                           # Git ignore file
└── README.md                            # This file
```

## 🚀 Features

### Data Science Pipeline
- ✅ Comprehensive EDA with 15+ visualizations
- ✅ Data quality checks (missing values, duplicates, outliers)
- ✅ Feature correlation analysis
- ✅ Statistical comparisons between churned and non-churned customers
- ✅ Feature engineering insights

### Model Development
- ✅ Logistic Regression with hyperparameter tuning (GridSearchCV)
- ✅ Stratified train-test split
- ✅ Feature scaling using StandardScaler
- ✅ Cross-validation for robust evaluation
- ✅ Multiple evaluation metrics (Accuracy, Precision, Recall, F1, ROC-AUC)

### Web Application
- ✅ Clean and modern user interface
- ✅ Real-time predictions via REST API
- ✅ Input validation and error handling
- ✅ Probability visualization
- ✅ Personalized recommendations
- ✅ Responsive design for mobile devices

## 📊 Dataset

The dataset contains **3,333 customer records** with the following features:

| Feature | Description | Type |
|---------|-------------|------|
| **AccountWeeks** | Number of weeks the customer has been with the company | Numeric |
| **ContractRenewal** | Whether the contract was renewed (0=No, 1=Yes) | Binary |
| **DataPlan** | Whether the customer has a data plan (0=No, 1=Yes) | Binary |
| **DataUsage** | Amount of data used (GB) | Numeric |
| **CustServCalls** | Number of customer service calls | Numeric |
| **DayMins** | Total daytime minutes used | Numeric |
| **DayCalls** | Number of daytime calls | Numeric |
| **MonthlyCharge** | Monthly service charge ($) | Numeric |
| **OverageFee** | Overage charges ($) | Numeric |
| **RoamMins** | Roaming minutes used | Numeric |
| **Churn** | Target variable (0=Not Churned, 1=Churned) | Binary |

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Logistic_Regression_Project.git
   cd Logistic_Regression_Project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   .venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### 1. Exploratory Data Analysis

Open and run the Jupyter notebook to explore the data:

```bash
jupyter notebook notebooks/01_EDA_and_Analysis.ipynb
```

The notebook includes:
- Data loading and inspection
- Data quality assessment
- Target variable analysis
- Feature distributions and correlations
- Statistical comparisons
- Outlier detection
- Feature engineering insights

### 2. Train the Model

Run the training script to preprocess data and train the model:

```bash
python train.py
```

This will:
- Load and preprocess the data
- Perform hyperparameter tuning using GridSearchCV
- Train the logistic regression model
- Evaluate performance on test data
- Generate visualization plots
- Save the model and preprocessing artifacts

**Expected Output:**
```
================================================================================
TELECOM CUSTOMER CHURN PREDICTION - MODEL TRAINING PIPELINE
================================================================================

[STEP 1/4] Data Preprocessing
Loading data from telecom_churn.csv...
Data loaded successfully! Shape: (3333, 11)
...

[STEP 2/4] Model Training
Performing hyperparameter tuning using GridSearchCV...
✓ Best parameters found:
  C: 1
  penalty: l2
  solver: liblinear
...

[STEP 3/4] Model Evaluation
Performance Metrics:
  Accuracy:  0.XXXX
  Precision: 0.XXXX
  Recall:    0.XXXX
  F1-Score:  0.XXXX
  ROC-AUC:   0.XXXX
...

[STEP 4/4] Saving Model
✓ Model saved to models/churn_model.pkl
```

### 3. Run the Web Application

Start the Flask server:

```bash
python app.py
```

The application will be available at: **http://localhost:5000**

**Features of the Web Interface:**
- Input customer details through an intuitive form
- Get real-time churn predictions
- View churn probability percentages
- Receive personalized retention recommendations
- Clean and professional design

### 4. Make Predictions

#### Via Web Interface:
1. Open http://localhost:5000 in your browser
2. Fill in the customer details
3. Click "Predict Churn"
4. View the prediction and recommendations

#### Via API:
```python
import requests
import json

# Customer data
customer_data = {
    "AccountWeeks": 128,
    "ContractRenewal": 1,
    "DataPlan": 1,
    "DataUsage": 2.7,
    "CustServCalls": 1,
    "DayMins": 265.1,
    "DayCalls": 110,
    "MonthlyCharge": 89,
    "OverageFee": 9.87,
    "RoamMins": 10
}

# Make prediction request
response = requests.post(
    'http://localhost:5000/predict',
    json=customer_data,
    headers={'Content-Type': 'application/json'}
)

# Get results
result = response.json()
print(json.dumps(result, indent=2))
```

## 📈 Model Performance

The model is evaluated using multiple metrics:

- **Accuracy**: Overall correctness of predictions
- **Precision**: Accuracy of positive predictions (churn)
- **Recall**: Ability to find all churning customers
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under the ROC curve

Performance visualizations are saved in the `models/` directory:
- `confusion_matrix.png` - Shows true vs predicted labels
- `roc_curve.png` - ROC curve with AUC score
- `feature_importance.png` - Most influential features

## 🔍 Key Insights

Based on the exploratory data analysis:

1. **Customer Service Calls**: Strong positive correlation with churn
2. **Contract Renewal**: Customers who don't renew are more likely to churn
3. **Account Weeks**: Longer tenure generally indicates lower churn risk
4. **Overage Fees**: Higher fees correlate with increased churn
5. **Data Plan**: Having a data plan shows mixed effects on churn

## 🎨 Frontend Features

The web interface includes:

- **Modern Design**: Clean, professional UI with gradient backgrounds
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Form Validation**: Real-time input validation with visual feedback
- **Interactive Elements**: Tooltips, animations, and smooth scrolling
- **Visual Feedback**: Color-coded results and probability bars
- **Recommendations**: Personalized action items based on prediction

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Render the home page |
| `/predict` | POST | Make a churn prediction |
| `/api/info` | GET | Get model information |
| `/health` | GET | Check application health |

### Example API Response

```json
{
  "success": true,
  "prediction": 0,
  "prediction_label": "Not Churn",
  "probability": {
    "not_churn": 85.23,
    "churn": 14.77
  },
  "input_features": {
    "AccountWeeks": 128,
    "ContractRenewal": 1,
    ...
  }
}
```

## 🧪 Testing

To test the application:

1. **Unit Testing**: Test individual modules
   ```bash
   python -m pytest tests/  # (if you add tests)
   ```

2. **Manual Testing**: Use the web interface with different customer profiles

3. **API Testing**: Use tools like Postman or curl
   ```bash
   curl -X POST http://localhost:5000/predict \
        -H "Content-Type: application/json" \
        -d '{"AccountWeeks": 128, "ContractRenewal": 1, ...}'
   ```

## 📚 Technologies Used

### Backend
- **Python 3.10**: Programming language
- **Flask**: Web framework
- **Scikit-learn**: Machine learning library
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing

### Data Science
- **Matplotlib**: Plotting and visualization
- **Seaborn**: Statistical visualization
- **Joblib**: Model serialization

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with modern features
- **JavaScript (ES6+)**: Interactivity
- **Font Awesome**: Icons

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Dataset source: Telecom customer data
- Inspiration: Customer retention in telecom industry
- Built as a portfolio project to demonstrate end-to-end ML skills

## 🔮 Future Enhancements

- [ ] Add more ML models (Random Forest, XGBoost, Neural Networks)
- [ ] Implement model comparison dashboard
- [ ] Add batch prediction functionality
- [ ] Include SHAP values for model interpretability
- [ ] Deploy to cloud platform (AWS, Azure, or Heroku)
- [ ] Add user authentication and prediction history
- [ ] Implement A/B testing framework
- [ ] Create Docker container for easy deployment
- [ ] Add real-time monitoring and logging
- [ ] Integrate with CI/CD pipeline

## 📞 Support

If you encounter any issues or have questions:

1. Check the documentation above
2. Search existing issues on GitHub
3. Create a new issue with detailed description
4. Contact the author directly

---

**⭐ If you find this project helpful, please consider giving it a star!**

Made with ❤️ for data science and machine learning
