"""
Model Training Module
---------------------
This module handles model training, evaluation, and saving.
Includes hyperparameter tuning and comprehensive performance metrics.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from datetime import datetime


class ChurnPredictor:
    """
    A class to handle logistic regression model training and evaluation.
    """
    
    def __init__(self, random_state=42):
        """
        Initialize the predictor.
        
        Parameters:
        -----------
        random_state : int
            Random seed for reproducibility
        """
        self.random_state = random_state
        self.model = None
        self.best_params = None
        self.feature_importance = None
        
    def train_model(self, X_train, y_train, hyperparameter_tuning=True):
        """
        Train logistic regression model with optional hyperparameter tuning.
        
        Parameters:
        -----------
        X_train : np.ndarray
            Training features
        y_train : np.ndarray or pd.Series
            Training target
        hyperparameter_tuning : bool
            Whether to perform hyperparameter tuning
            
        Returns:
        --------
        LogisticRegression
            Trained model
        """
        print("\n" + "="*80)
        print("TRAINING LOGISTIC REGRESSION MODEL")
        print("="*80)
        
        if hyperparameter_tuning:
            print("\nPerforming hyperparameter tuning using GridSearchCV...")
            
            # Define parameter grid
            param_grid = {
                'C': [0.001, 0.01, 0.1, 1, 10, 100],
                'penalty': ['l1', 'l2'],
                'solver': ['liblinear', 'saga'],
                'max_iter': [1000]
            }
            
            # Initialize base model
            base_model = LogisticRegression(random_state=self.random_state)
            
            # Grid search with cross-validation
            grid_search = GridSearchCV(
                estimator=base_model,
                param_grid=param_grid,
                cv=5,
                scoring='roc_auc',
                n_jobs=-1,
                verbose=1
            )
            
            # Fit grid search
            grid_search.fit(X_train, y_train)
            
            # Get best model and parameters
            self.model = grid_search.best_estimator_
            self.best_params = grid_search.best_params_
            
            print(f"\n✓ Best parameters found:")
            for param, value in self.best_params.items():
                print(f"  {param}: {value}")
            print(f"\n✓ Best cross-validation ROC-AUC score: {grid_search.best_score_:.4f}")
            
        else:
            print("\nTraining model with default parameters...")
            self.model = LogisticRegression(
                random_state=self.random_state,
                max_iter=1000
            )
            self.model.fit(X_train, y_train)
            print("✓ Model trained successfully!")
        
        return self.model
    
    def evaluate_model(self, X_test, y_test, feature_names=None):
        """
        Evaluate model performance on test data.
        
        Parameters:
        -----------
        X_test : np.ndarray
            Test features
        y_test : np.ndarray or pd.Series
            Test target
        feature_names : list
            Names of features for feature importance
            
        Returns:
        --------
        dict
            Dictionary containing all evaluation metrics
        """
        print("\n" + "="*80)
        print("MODEL EVALUATION")
        print("="*80)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred),
            'roc_auc': roc_auc_score(y_test, y_pred_proba),
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }
        
        # Print metrics
        print("\nPerformance Metrics:")
        print(f"  Accuracy:  {metrics['accuracy']:.4f}")
        print(f"  Precision: {metrics['precision']:.4f}")
        print(f"  Recall:    {metrics['recall']:.4f}")
        print(f"  F1-Score:  {metrics['f1_score']:.4f}")
        print(f"  ROC-AUC:   {metrics['roc_auc']:.4f}")
        
        # Confusion Matrix
        print("\nConfusion Matrix:")
        print(metrics['confusion_matrix'])
        
        # Classification Report
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, 
                                   target_names=['Not Churned', 'Churned']))
        
        # Feature importance
        if feature_names is not None:
            self.feature_importance = pd.DataFrame({
                'feature': feature_names,
                'coefficient': self.model.coef_[0]
            }).sort_values(by='coefficient', key=abs, ascending=False)
            
            print("\nTop 5 Most Important Features:")
            print(self.feature_importance.head())
        
        return metrics
    
    def plot_confusion_matrix(self, confusion_mat, save_path='models/confusion_matrix.png'):
        """
        Plot confusion matrix.
        
        Parameters:
        -----------
        confusion_mat : np.ndarray
            Confusion matrix
        save_path : str
            Path to save the plot
        """
        plt.figure(figsize=(8, 6))
        sns.heatmap(confusion_mat, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=['Not Churned', 'Churned'],
                   yticklabels=['Not Churned', 'Churned'])
        plt.title('Confusion Matrix', fontsize=14, fontweight='bold')
        plt.ylabel('Actual', fontsize=12)
        plt.xlabel('Predicted', fontsize=12)
        plt.tight_layout()
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"\n✓ Confusion matrix plot saved to {save_path}")
    
    def plot_roc_curve(self, X_test, y_test, save_path='models/roc_curve.png'):
        """
        Plot ROC curve.
        
        Parameters:
        -----------
        X_test : np.ndarray
            Test features
        y_test : np.ndarray or pd.Series
            Test target
        save_path : str
            Path to save the plot
        """
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='darkorange', lw=2, 
                label=f'ROC curve (AUC = {roc_auc:.4f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', 
                label='Random Classifier')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate', fontsize=12)
        plt.ylabel('True Positive Rate', fontsize=12)
        plt.title('Receiver Operating Characteristic (ROC) Curve', 
                 fontsize=14, fontweight='bold')
        plt.legend(loc="lower right")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✓ ROC curve plot saved to {save_path}")
    
    def plot_feature_importance(self, save_path='models/feature_importance.png'):
        """
        Plot feature importance.
        
        Parameters:
        -----------
        save_path : str
            Path to save the plot
        """
        if self.feature_importance is None:
            print("Feature importance not available. Run evaluate_model first.")
            return
        
        plt.figure(figsize=(10, 8))
        colors = ['red' if x < 0 else 'green' for x in self.feature_importance['coefficient']]
        plt.barh(self.feature_importance['feature'], 
                self.feature_importance['coefficient'], 
                color=colors, edgecolor='black')
        plt.xlabel('Coefficient Value', fontsize=12)
        plt.ylabel('Features', fontsize=12)
        plt.title('Feature Importance (Logistic Regression Coefficients)', 
                 fontsize=14, fontweight='bold')
        plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
        plt.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✓ Feature importance plot saved to {save_path}")
    
    def save_model(self, filepath='models/churn_model.pkl'):
        """
        Save the trained model to disk.
        
        Parameters:
        -----------
        filepath : str
            Path to save the model
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Save model with metadata
        model_data = {
            'model': self.model,
            'best_params': self.best_params,
            'feature_importance': self.feature_importance,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        joblib.dump(model_data, filepath)
        print(f"\n✓ Model saved to {filepath}")
    
    def load_model(self, filepath='models/churn_model.pkl'):
        """
        Load a trained model from disk.
        
        Parameters:
        -----------
        filepath : str
            Path to load the model from
        """
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.best_params = model_data.get('best_params')
        self.feature_importance = model_data.get('feature_importance')
        print(f"✓ Model loaded from {filepath}")
        return self.model
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Parameters:
        -----------
        X : np.ndarray
            Features to predict
            
        Returns:
        --------
        tuple
            (predictions, probabilities)
        """
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)
        return predictions, probabilities


if __name__ == "__main__":
    # This will be called from the main training script
    print("Model training module loaded successfully!")
