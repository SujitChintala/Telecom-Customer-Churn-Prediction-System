# Setup Guide

This guide provides step-by-step instructions to set up and run the Telecom Customer Churn Prediction System.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package manager (usually comes with Python)
- **Git** (optional): For cloning the repository

## Installation Steps

### Step 1: Get the Project

#### Option A: Clone from GitHub
```bash
git clone https://github.com/yourusername/Logistic_Regression_Project.git
cd Logistic_Regression_Project
```

#### Option B: Download ZIP
1. Download the project as a ZIP file
2. Extract to your desired location
3. Navigate to the project directory

### Step 2: Create a Virtual Environment (Recommended)

Creating a virtual environment keeps your project dependencies isolated.

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt, indicating the virtual environment is active.

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Scikit-learn (machine learning)
- Pandas (data manipulation)
- NumPy (numerical computing)
- Matplotlib (visualization)
- Seaborn (statistical plots)
- And other dependencies

**Installation time:** Approximately 2-3 minutes

### Step 4: Verify Installation

Check that all packages are installed correctly:

```bash
python -c "import flask, sklearn, pandas, numpy, matplotlib, seaborn; print('All packages installed successfully!')"
```

If you see "All packages installed successfully!", you're ready to proceed.

## Training the Model

Before running the web application, you need to train the machine learning model.

### Run the Training Script

```bash
python train.py
```

**What happens during training:**

1. **Data Loading**: Loads `telecom_churn.csv` dataset
2. **Data Preprocessing**: 
   - Validates data quality
   - Splits data into training and test sets (80-20)
   - Scales features using StandardScaler
3. **Hyperparameter Tuning**:
   - Tests different parameter combinations
   - Uses GridSearchCV with 5-fold cross-validation
   - Selects best parameters
4. **Model Training**:
   - Trains Logistic Regression with optimal parameters
5. **Model Evaluation**:
   - Calculates performance metrics
   - Generates visualization plots
6. **Saves Model Artifacts**:
   - `models/churn_model.pkl`
   - `models/scaler.pkl`
   - `models/feature_names.pkl`
   - `models/confusion_matrix.png`
   - `models/roc_curve.png`
   - `models/feature_importance.png`

**Expected duration:** 2-3 minutes

**Expected output:**
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
✓ Best parameters found...

[STEP 3/4] Model Evaluation
Performance Metrics:
  Accuracy:  0.XXXX
  Precision: 0.XXXX
  Recall:    0.XXXX
  F1-Score:  0.XXXX
  ROC-AUC:   0.XXXX

[STEP 4/4] Saving Model
✓ Model saved successfully
✓ Training pipeline completed!
```

## Running the Web Application

After training the model, start the Flask web server:

```bash
python app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
 * Running on http://localhost:5000
Press CTRL+C to quit
```

The application is now running locally on your machine.

## Accessing the Application

1. Open your web browser
2. Navigate to: **http://localhost:5000**
3. You should see the Churn Prediction interface

## Using the Application

### Making a Prediction

1. **Fill in the customer details** in the form:
   - Account Weeks
   - Contract Renewal (Yes=1, No=0)
   - Data Plan (Yes=1, No=0)
   - Data Usage (GB)
   - Customer Service Calls
   - Day Minutes
   - Day Calls
   - Monthly Charge ($)
   - Overage Fee ($)
   - Roaming Minutes

2. **Click "Predict Churn"**

3. **View the results**:
   - Prediction (Churn or Not Churn)
   - Probability percentages
   - Personalized recommendations

### Sample Test Data

**Low Churn Risk Customer:**
```
Account Weeks: 128
Contract Renewal: 1 (Yes)
Data Plan: 1 (Yes)
Data Usage: 2.7
Customer Service Calls: 1
Day Minutes: 265.1
Day Calls: 110
Monthly Charge: 89
Overage Fee: 9.87
Roaming Minutes: 10
```

**High Churn Risk Customer:**
```
Account Weeks: 65
Contract Renewal: 0 (No)
Data Plan: 0 (No)
Data Usage: 0.29
Customer Service Calls: 4
Day Minutes: 129.1
Day Calls: 137
Monthly Charge: 44.9
Overage Fee: 11.43
Roaming Minutes: 12.7
```

## Exploring the Notebook (Optional)

To view the exploratory data analysis:

1. **Install Jupyter** (if not already installed):
   ```bash
   pip install jupyter
   ```

2. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook notebooks/01_EDA_and_Analysis.ipynb
   ```

3. **Run the cells** to see:
   - Data exploration
   - Statistical analysis
   - Visualizations
   - Feature correlations
   - Insights

## Troubleshooting

### Issue: "Model not found" Error

**Cause:** The model hasn't been trained yet.

**Solution:**
```bash
python train.py
```

### Issue: "Port 5000 already in use"

**Cause:** Another application is using port 5000.

**Solution 1:** Stop the other application

**Solution 2:** Change the port in `app.py`:
```python
# At the bottom of app.py, change:
app.run(debug=True, host='0.0.0.0', port=5001)  # Use port 5001
```

Then access: `http://localhost:5001`

### Issue: "Module not found" Error

**Cause:** Dependencies not installed or virtual environment not activated.

**Solution:**
```bash
# Make sure virtual environment is active
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Python not recognized"

**Cause:** Python not in system PATH.

**Solution:**
- Reinstall Python and check "Add Python to PATH" during installation
- Or use full path to Python executable

### Issue: Permission Denied on Windows

**Cause:** PowerShell execution policy.

**Solution:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Virtual Environment Won't Activate on Windows

**Solution:**
```bash
# Use this instead:
.venv\Scripts\Activate.ps1
```

## Verifying Setup

Run these commands to verify everything is working:

```bash
# 1. Check Python version
python --version

# 2. Check if packages are installed
pip list

# 3. Check if model files exist
# On Windows:
dir models

# On macOS/Linux:
ls -la models

# 4. Test the API (while app.py is running)
curl http://localhost:5000/health
```

## Next Steps

After successful setup:

1. **Explore the EDA notebook** to understand the data
2. **Test the web application** with different customer profiles
3. **Review the code** in `src/`, `train.py`, and `app.py`
4. **Check model visualizations** in the `models/` directory
5. **Read the documentation** in `README.md` and `PROJECT_SUMMARY.md`

## Running in Production (Advanced)

For production deployment, consider:

### Using Gunicorn (Linux/macOS)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Waitress (Windows)

```bash
pip install waitress
waitress-serve --port=5000 app:app
```

### Docker Container (All Platforms)

Create a `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t churn-prediction .
docker run -p 5000:5000 churn-prediction
```

## Updating the Project

To update dependencies:

```bash
pip install --upgrade -r requirements.txt
```

To retrain the model with new data:

1. Replace `telecom_churn.csv` with new data
2. Run: `python train.py`

## Deactivating Virtual Environment

When finished working:

```bash
deactivate
```

## Uninstalling

To remove the project:

1. Deactivate virtual environment (if active)
2. Delete the project folder
3. That's it! (Virtual environment is self-contained)

## Additional Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Scikit-learn Documentation**: https://scikit-learn.org/stable/
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **Python Documentation**: https://docs.python.org/3/

## Getting Help

If you encounter issues:

1. Check this troubleshooting section
2. Review error messages carefully
3. Search for similar issues online
4. Check the project's GitHub issues (if applicable)
5. Contact the project maintainer

## Quick Reference Commands

```bash
# Setup
python -m venv .venv
.venv\Scripts\activate                    # Windows
source .venv/bin/activate                 # macOS/Linux
pip install -r requirements.txt

# Train model
python train.py

# Run application
python app.py

# View notebook
jupyter notebook notebooks/01_EDA_and_Analysis.ipynb

# Deactivate environment
deactivate
```

---

**You're all set!** Enjoy exploring the Telecom Customer Churn Prediction System! 🚀
