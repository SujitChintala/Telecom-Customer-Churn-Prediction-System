"""
Data Preprocessing Module
--------------------------
This module handles all data preprocessing tasks including:
- Data loading
- Missing value handling
- Feature encoding
- Feature scaling
- Train-test splitting
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os


class DataPreprocessor:
    """
    A class to handle all data preprocessing operations.
    """
    
    def __init__(self, data_path):
        """
        Initialize the preprocessor with data path.
        
        Parameters:
        -----------
        data_path : str
            Path to the CSV file containing the data
        """
        self.data_path = data_path
        self.scaler = StandardScaler()
        self.feature_names = None
        self.data = None
        
    def load_data(self):
        """
        Load data from CSV file.
        
        Returns:
        --------
        pd.DataFrame
            Loaded dataframe
        """
        print(f"Loading data from {self.data_path}...")
        self.data = pd.read_csv(self.data_path)
        print(f"Data loaded successfully! Shape: {self.data.shape}")
        return self.data
    
    def check_data_quality(self):
        """
        Check for missing values and duplicates.
        
        Returns:
        --------
        dict
            Dictionary containing data quality metrics
        """
        print("\n" + "="*80)
        print("DATA QUALITY CHECK")
        print("="*80)
        
        quality_metrics = {
            'missing_values': self.data.isnull().sum().sum(),
            'duplicates': self.data.duplicated().sum(),
            'total_rows': len(self.data),
            'total_columns': len(self.data.columns)
        }
        
        print(f"Total Rows: {quality_metrics['total_rows']}")
        print(f"Total Columns: {quality_metrics['total_columns']}")
        print(f"Missing Values: {quality_metrics['missing_values']}")
        print(f"Duplicate Rows: {quality_metrics['duplicates']}")
        
        if quality_metrics['missing_values'] == 0:
            print("✓ No missing values found!")
        
        if quality_metrics['duplicates'] == 0:
            print("✓ No duplicate rows found!")
        
        return quality_metrics
    
    def prepare_features_target(self):
        """
        Separate features and target variable.
        
        Returns:
        --------
        tuple
            (X, y) where X is features and y is target
        """
        print("\nPreparing features and target variable...")
        
        # Separate features and target
        X = self.data.drop('Churn', axis=1)
        y = self.data['Churn']
        
        # Store feature names
        self.feature_names = X.columns.tolist()
        
        print(f"Features shape: {X.shape}")
        print(f"Target shape: {y.shape}")
        print(f"Feature names: {self.feature_names}")
        
        # Check target distribution
        churn_dist = y.value_counts()
        churn_pct = y.value_counts(normalize=True) * 100
        print(f"\nTarget Distribution:")
        print(f"  Not Churned (0): {churn_dist[0]} ({churn_pct[0]:.2f}%)")
        print(f"  Churned (1): {churn_dist[1]} ({churn_pct[1]:.2f}%)")
        
        return X, y
    
    def split_data(self, X, y, test_size=0.2, random_state=42):
        """
        Split data into training and testing sets.
        
        Parameters:
        -----------
        X : pd.DataFrame
            Features
        y : pd.Series
            Target variable
        test_size : float
            Proportion of data for testing
        random_state : int
            Random seed for reproducibility
            
        Returns:
        --------
        tuple
            (X_train, X_test, y_train, y_test)
        """
        print(f"\nSplitting data (test_size={test_size}, random_state={random_state})...")
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
        
        print(f"Training set size: {len(X_train)} ({(1-test_size)*100:.0f}%)")
        print(f"Testing set size: {len(X_test)} ({test_size*100:.0f}%)")
        
        # Check stratification
        train_churn_pct = (y_train.sum() / len(y_train)) * 100
        test_churn_pct = (y_test.sum() / len(y_test)) * 100
        print(f"\nChurn rate in training set: {train_churn_pct:.2f}%")
        print(f"Churn rate in testing set: {test_churn_pct:.2f}%")
        
        return X_train, X_test, y_train, y_test
    
    def scale_features(self, X_train, X_test):
        """
        Scale features using StandardScaler.
        
        Parameters:
        -----------
        X_train : pd.DataFrame or np.ndarray
            Training features
        X_test : pd.DataFrame or np.ndarray
            Testing features
            
        Returns:
        --------
        tuple
            (X_train_scaled, X_test_scaled)
        """
        print("\nScaling features using StandardScaler...")
        
        # Fit scaler on training data and transform both sets
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        print(f"✓ Features scaled successfully!")
        print(f"  Mean of scaled training features: {X_train_scaled.mean():.6f}")
        print(f"  Std of scaled training features: {X_train_scaled.std():.6f}")
        
        return X_train_scaled, X_test_scaled
    
    def save_scaler(self, filepath='models/scaler.pkl'):
        """
        Save the fitted scaler to disk.
        
        Parameters:
        -----------
        filepath : str
            Path to save the scaler
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.scaler, filepath)
        print(f"\n✓ Scaler saved to {filepath}")
    
    def save_feature_names(self, filepath='models/feature_names.pkl'):
        """
        Save feature names to disk.
        
        Parameters:
        -----------
        filepath : str
            Path to save the feature names
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.feature_names, filepath)
        print(f"✓ Feature names saved to {filepath}")
    
    def preprocess_pipeline(self, test_size=0.2, random_state=42):
        """
        Complete preprocessing pipeline.
        
        Parameters:
        -----------
        test_size : float
            Proportion of data for testing
        random_state : int
            Random seed for reproducibility
            
        Returns:
        --------
        dict
            Dictionary containing all preprocessed data
        """
        print("\n" + "="*80)
        print("STARTING DATA PREPROCESSING PIPELINE")
        print("="*80)
        
        # Load data
        self.load_data()
        
        # Check data quality
        self.check_data_quality()
        
        # Prepare features and target
        X, y = self.prepare_features_target()
        
        # Split data
        X_train, X_test, y_train, y_test = self.split_data(X, y, test_size, random_state)
        
        # Scale features
        X_train_scaled, X_test_scaled = self.scale_features(X_train, X_test)
        
        # Save scaler and feature names
        self.save_scaler()
        self.save_feature_names()
        
        print("\n" + "="*80)
        print("✓ PREPROCESSING PIPELINE COMPLETED SUCCESSFULLY!")
        print("="*80)
        
        return {
            'X_train': X_train_scaled,
            'X_test': X_test_scaled,
            'y_train': y_train,
            'y_test': y_test,
            'feature_names': self.feature_names,
            'scaler': self.scaler
        }


if __name__ == "__main__":
    # Example usage
    preprocessor = DataPreprocessor('../telecom_churn.csv')
    data = preprocessor.preprocess_pipeline()
    
    print(f"\nData ready for model training!")
    print(f"X_train shape: {data['X_train'].shape}")
    print(f"X_test shape: {data['X_test'].shape}")
