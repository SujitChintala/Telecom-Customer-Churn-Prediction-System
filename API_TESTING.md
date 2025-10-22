# API Testing Examples

This document provides examples for testing the API endpoints.

## Prerequisites

Make sure the Flask server is running:
```bash
python app.py
```

## Testing with cURL

### 1. Health Check
```bash
curl http://localhost:5000/health
```

Expected Response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "scaler_loaded": true
}
```

### 2. Model Information
```bash
curl http://localhost:5000/api/info
```

Expected Response:
```json
{
  "success": true,
  "model_type": "Logistic Regression",
  "features": ["AccountWeeks", "ContractRenewal", ...],
  "num_features": 10,
  "best_params": {...},
  "timestamp": "2024-XX-XX XX:XX:XX"
}
```

### 3. Make Prediction - Low Churn Risk
```bash
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"AccountWeeks\": 128, \"ContractRenewal\": 1, \"DataPlan\": 1, \"DataUsage\": 2.7, \"CustServCalls\": 1, \"DayMins\": 265.1, \"DayCalls\": 110, \"MonthlyCharge\": 89, \"OverageFee\": 9.87, \"RoamMins\": 10}"
```

### 4. Make Prediction - High Churn Risk
```bash
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"AccountWeeks\": 65, \"ContractRenewal\": 0, \"DataPlan\": 0, \"DataUsage\": 0.29, \"CustServCalls\": 4, \"DayMins\": 129.1, \"DayCalls\": 137, \"MonthlyCharge\": 44.9, \"OverageFee\": 11.43, \"RoamMins\": 12.7}"
```

## Testing with Python

### Using requests library

```python
import requests
import json

# Base URL
BASE_URL = "http://localhost:5000"

# Test 1: Health Check
response = requests.get(f"{BASE_URL}/health")
print("Health Check:", response.json())

# Test 2: Model Info
response = requests.get(f"{BASE_URL}/api/info")
print("\nModel Info:", json.dumps(response.json(), indent=2))

# Test 3: Prediction - Low Churn Risk
low_churn_customer = {
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
    f"{BASE_URL}/predict",
    json=low_churn_customer,
    headers={'Content-Type': 'application/json'}
)
print("\nLow Churn Risk Prediction:")
print(json.dumps(response.json(), indent=2))

# Test 4: Prediction - High Churn Risk
high_churn_customer = {
    "AccountWeeks": 65,
    "ContractRenewal": 0,
    "DataPlan": 0,
    "DataUsage": 0.29,
    "CustServCalls": 4,
    "DayMins": 129.1,
    "DayCalls": 137,
    "MonthlyCharge": 44.9,
    "OverageFee": 11.43,
    "RoamMins": 12.7
}

response = requests.post(
    f"{BASE_URL}/predict",
    json=high_churn_customer,
    headers={'Content-Type': 'application/json'}
)
print("\nHigh Churn Risk Prediction:")
print(json.dumps(response.json(), indent=2))
```

## Testing with Postman

1. Create a new request
2. Set method to POST
3. Set URL to `http://localhost:5000/predict`
4. Go to Headers tab and add:
   - Key: `Content-Type`
   - Value: `application/json`
5. Go to Body tab, select `raw` and `JSON`
6. Paste the customer data JSON
7. Click Send

### Sample JSON for Postman Body:
```json
{
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
```

## Error Testing

### Missing Fields
```python
incomplete_data = {
    "AccountWeeks": 128,
    "ContractRenewal": 1
    # Missing other required fields
}

response = requests.post(f"{BASE_URL}/predict", json=incomplete_data)
print(response.json())
# Expected: Error message about missing features
```

### Invalid Values
```python
invalid_data = {
    "AccountWeeks": "not_a_number",  # Should be numeric
    "ContractRenewal": 1,
    ...
}

response = requests.post(f"{BASE_URL}/predict", json=invalid_data)
print(response.json())
# Expected: Error message about invalid value
```

## Batch Testing Script

Save this as `test_api.py`:

```python
import requests
import json

BASE_URL = "http://localhost:5000"

test_cases = [
    {
        "name": "Low Churn Risk - Long tenure, renewed contract",
        "data": {
            "AccountWeeks": 150,
            "ContractRenewal": 1,
            "DataPlan": 1,
            "DataUsage": 3.5,
            "CustServCalls": 0,
            "DayMins": 200,
            "DayCalls": 100,
            "MonthlyCharge": 95,
            "OverageFee": 5,
            "RoamMins": 8
        }
    },
    {
        "name": "High Churn Risk - Many service calls, no renewal",
        "data": {
            "AccountWeeks": 50,
            "ContractRenewal": 0,
            "DataPlan": 0,
            "DataUsage": 0.5,
            "CustServCalls": 5,
            "DayMins": 150,
            "DayCalls": 120,
            "MonthlyCharge": 40,
            "OverageFee": 15,
            "RoamMins": 15
        }
    }
]

for test in test_cases:
    print(f"\n{'='*80}")
    print(f"Test: {test['name']}")
    print('='*80)
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=test['data'],
        headers={'Content-Type': 'application/json'}
    )
    
    result = response.json()
    
    if result.get('success'):
        print(f"Prediction: {result['prediction_label']}")
        print(f"Churn Probability: {result['probability']['churn']}%")
        print(f"Not Churn Probability: {result['probability']['not_churn']}%")
    else:
        print(f"Error: {result.get('error')}")

print("\n" + "="*80)
print("Testing completed!")
```

Run with:
```bash
python test_api.py
```
