# 🚀 Quick Start Guide

## Installation and Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Train the Model
```bash
python train.py
```

Wait for the training to complete (~2-3 minutes). You'll see:
- Data preprocessing progress
- Hyperparameter tuning progress
- Final model metrics
- Saved model files

### Step 3: Run the Web App
```bash
python app.py
```

### Step 4: Open in Browser
Navigate to: **http://localhost:5000**

## Sample Customer Data for Testing

### Example 1: Low Churn Risk Customer
```
Account Weeks: 128
Contract Renewal: Yes (1)
Data Plan: Yes (1)
Data Usage: 2.7
Customer Service Calls: 1
Day Minutes: 265.1
Day Calls: 110
Monthly Charge: 89
Overage Fee: 9.87
Roaming Minutes: 10
```

### Example 2: High Churn Risk Customer
```
Account Weeks: 65
Contract Renewal: No (0)
Data Plan: No (0)
Data Usage: 0.29
Customer Service Calls: 4
Day Minutes: 129.1
Day Calls: 137
Monthly Charge: 44.9
Overage Fee: 11.43
Roaming Minutes: 12.7
```

## Troubleshooting

### Model not found error?
**Solution**: Run `python train.py` first to train and save the model.

### Port 5000 already in use?
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Import errors?
**Solution**: Make sure you're in the virtual environment and all packages are installed.

## File Checklist

After training, you should have these files:
- ✅ `models/churn_model.pkl`
- ✅ `models/scaler.pkl`
- ✅ `models/feature_names.pkl`
- ✅ `models/confusion_matrix.png`
- ✅ `models/roc_curve.png`
- ✅ `models/feature_importance.png`

## Next Steps

1. Explore the EDA notebook for data insights
2. Experiment with different customer profiles
3. Check model performance visualizations
4. Customize the frontend appearance
5. Add this to your portfolio/resume!
