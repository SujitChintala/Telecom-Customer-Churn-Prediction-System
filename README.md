# 📊 Telecom Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive machine learning project that predicts customer churn in the telecom industry using Logistic Regression. This project includes a complete data science pipeline from exploratory data analysis to deployment with an interactive web interface.

## 🎯 Project Overview

Customer churn prediction is crucial for telecom companies to identify customers likely to leave and take proactive retention measures. This project implements a production-ready machine learning solution that analyzes customer behavior patterns and predicts churn risk with confidence scores and personalized recommendations.

### Key Features

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
│   └── model.py                         # Model training and evaluation
│
├── models/                              # Generated after training
│   ├── churn_model.pkl                  # Trained model
│   ├── scaler.pkl                       # Fitted scaler
│   ├── feature_names.pkl                # Feature mappings
│   ├── confusion_matrix.png             # Performance visualization
│   ├── roc_curve.png                    # ROC curve
│   └── feature_importance.png           # Feature importance
│
├── templates/
│   └── index.html                       # Web interface
│
├── static/
│   ├── style.css                        # Styling
│   └── script.js                        # Interactivity
│
├── telecom_churn.csv                    # Dataset
├── train.py                             # Main training script
├── app.py                               # Flask web application
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
├── PROJECT_SUMMARY.md                   # Project overview
└── SETUP.md                             # Setup instructions
```

## 📊 Dataset

The dataset contains **3,333 customer records** with 10 features:

| Feature | Description | Type |
|---------|-------------|------|
| **AccountWeeks** | Number of weeks with the company | Numeric |
| **ContractRenewal** | Contract renewal status (0=No, 1=Yes) | Binary |
| **DataPlan** | Data plan subscription (0=No, 1=Yes) | Binary |
| **DataUsage** | Data usage in GB | Numeric |
| **CustServCalls** | Number of customer service calls | Numeric |
| **DayMins** | Daytime minutes used | Numeric |
| **DayCalls** | Number of daytime calls | Numeric |
| **MonthlyCharge** | Monthly service charge ($) | Numeric |
| **OverageFee** | Overage charges ($) | Numeric |
| **RoamMins** | Roaming minutes | Numeric |
| **Churn** | Target variable (0=No, 1=Yes) | Binary |

## 🚀 Quick Start

See [SETUP.md](SETUP.md) for detailed installation and setup instructions.

### Basic Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model:**
   ```bash
   python train.py
   ```

3. **Run the web application:**
   ```bash
   python app.py
   ```

4. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## 📖 Usage Guide

### 1. Exploratory Data Analysis

Open the Jupyter notebook to explore the data:

```bash
jupyter notebook notebooks/01_EDA_and_Analysis.ipynb
```

The notebook includes:
- Data loading and inspection
- Statistical summaries
- Feature distributions and correlations
- Target variable analysis
- Outlier detection
- Feature engineering insights

### 2. Model Training

Run the training pipeline:

```bash
python train.py
```

This process will:
- Load and preprocess data
- Perform hyperparameter tuning with GridSearchCV
- Train the logistic regression model
- Evaluate performance on test data
- Generate visualization plots
- Save model artifacts

**Expected Output:**
- Model performance metrics
- Confusion matrix, ROC curve, and feature importance plots
- Saved model files in `models/` directory

### 3. Web Application

Start the Flask server:

```bash
python app.py
```

The application provides:
- Intuitive form for customer data input
- Real-time churn predictions
- Probability visualization
- Personalized retention recommendations

### 4. Making Predictions

#### Via Web Interface:
1. Navigate to `http://localhost:5000`
2. Fill in customer details
3. Click "Predict Churn"
4. View results with probability scores

#### Via API:
```python
import requests

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

response = requests.post(
    'http://localhost:5000/predict',
    json=customer_data,
    headers={'Content-Type': 'application/json'}
)

print(response.json())
```

## 📈 Model Performance

The model is evaluated using multiple metrics:

- **Accuracy**: Overall prediction correctness
- **Precision**: Accuracy of positive predictions
- **Recall**: Ability to identify all churning customers
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under the ROC curve

Performance visualizations are automatically generated and saved in the `models/` directory.

## 🔍 Key Insights

Based on exploratory data analysis, key churn indicators include:

1. **Customer Service Calls**: Strong positive correlation with churn
2. **Contract Renewal**: Non-renewal strongly indicates churn risk
3. **Account Tenure**: Longer tenure generally indicates lower risk
4. **Overage Fees**: Higher fees correlate with increased churn
5. **Data Plan**: Subscription patterns affect churn likelihood

## 🎨 Web Interface Features

- **Modern Design**: Clean, professional UI with responsive layout
- **Form Validation**: Real-time input validation with visual feedback
- **Interactive Elements**: Smooth animations and transitions
- **Visual Feedback**: Color-coded results and probability bars
- **Recommendations**: Personalized action items based on prediction
- **Mobile Responsive**: Works seamlessly on all device sizes

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

## 📚 Technologies Used

### Backend & ML
- **Python 3.10+**: Programming language
- **Flask 3.0.0**: Web framework
- **Scikit-learn 1.3.2**: Machine learning
- **Pandas 2.1.4**: Data manipulation
- **NumPy 1.24.3**: Numerical computing
- **Matplotlib 3.8.2**: Visualization
- **Seaborn 0.13.0**: Statistical plots

### Frontend
- **HTML5**: Structure
- **CSS3**: Modern styling
- **JavaScript (ES6+)**: Interactivity
- **Font Awesome**: Icons

## 🧪 Testing

Test the application with sample data:

**Low Churn Risk Customer:**
```
AccountWeeks: 128, ContractRenewal: 1, DataPlan: 1
DataUsage: 2.7, CustServCalls: 1, DayMins: 265.1
DayCalls: 110, MonthlyCharge: 89, OverageFee: 9.87
RoamMins: 10
```

**High Churn Risk Customer:**
```
AccountWeeks: 65, ContractRenewal: 0, DataPlan: 0
DataUsage: 0.29, CustServCalls: 4, DayMins: 129.1
DayCalls: 137, MonthlyCharge: 44.9, OverageFee: 11.43
RoamMins: 12.7
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Saai Sujit Chintala**
- GitHub: [SujitChintala](https://github.com/SujitChintala)
- LinkedIn: [Saai Sujit Chintala](https://www.linkedin.com/in/sujitchintala/)
- Email: sujitchintala@gmail.com

## 🙏 Acknowledgments

- Dataset source: Kaggle - Telecom customer dataset
- Inspiration: Customer retention in telecom industry
- Built as a portfolio project demonstrating end-to-end ML skills

## 🔮 Future Enhancements

- [ ] Add more ML models (Random Forest, XGBoost)
- [ ] Implement model comparison dashboard
- [ ] Add batch prediction functionality
- [ ] Include SHAP values for interpretability
- [ ] Deploy to cloud platform (AWS, Azure, Heroku)
- [ ] Add user authentication and history
- [ ] Implement A/B testing framework
- [ ] Create Docker container
- [ ] Add monitoring and logging
- [ ] Integrate CI/CD pipeline

## 📞 Support

For issues or questions:

1. Check the documentation
2. Search existing GitHub issues
3. Create a new issue with detailed description
4. Contact the author directly

---

**⭐ If you find this project helpful, please consider giving it a star!**
