import pandas as pd
from typing import List, Tuple
from joblib import Parallel, delayed


from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, cross_val_score


def preprocessor(columns: List[str]) -> ColumnTransformer:
    """
    Create a preprocessing pipeline for numeric data.
    
    This function creates a scikit-learn pipeline that handles missing values
    and scales numeric features. The pipeline consists of:
    1. Imputation of missing values using median strategy
    2. Robust scaling to handle outliers
    
    Parameters
    ----------
    X : pd.DataFrame
        Input dataframe containing features to be preprocessed
        
    Returns
    -------
    ColumnTransformer
        A transformer that applies the numeric preprocessing pipeline to all columns
    """
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', RobustScaler())
    ])
    
    return ColumnTransformer(
        transformers=[('num', numeric_transformer, columns)]
    )
    

def preprocess(X_train: pd.DataFrame, X_test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Preprocess the training and test sets.
    
    This function preprocesses the training and test sets using the preprocessor
    function. It fits the preprocessor on the training set and transforms both
    sets.
    
    Parameters
    ----------
    X_train : pd.DataFrame
        Training set
    X_test : pd.DataFrame
        Test set
        
    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame]
        Preprocessed training and test sets
    """
    columns = X_train.columns
    preprocessor_ = preprocessor(columns)
    
    X_train = preprocessor_.fit_transform(X_train)
    X_test = preprocessor_.transform(X_test)
    
    return X_train, X_test



def train_and_evaluate_model(model_name, model, X_train, y_train, X_test, y_test, min_cv_mean_score):
    """Train a single model and return evaluation results."""
    cv_results = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    
    print(f"\n{model_name.upper()}: CV mean R²: {cv_results.mean():.4f} ± {cv_results.std():.4f}\n")
    
    if cv_results.mean() > min_cv_mean_score:
        model.fit(X_train, y_train)
        
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        
        return {
            'status': 'trained',
            'message': 'Model trained successfully',
            'data': {
                'model_name': model_name,
                'model': model,
                'cv_test_score_mean': cv_results.mean(),
                'cv_test_score_std': cv_results.std(),
                'train_score': train_score,
                'test_score': test_score
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Model did not pass cross-validation threshold',
            'data': {
                'model_name': model_name,
                'model': model,
                'cv_test_score_mean': cv_results.mean(),
                'cv_test_score_std': cv_results.std(),
                'train_score': None,
                'test_score': None
            }
        }

def train_models_parallel(models, X_train, y_train, X_test, y_test, min_cv_mean_score=0.5, n_jobs=-1):
    """Train multiple models in parallel."""
    return Parallel(n_jobs=n_jobs)(
        delayed(train_and_evaluate_model)(
            model_name, model, X_train, y_train, X_test, y_test, min_cv_mean_score
        )
        for model_name, model in models.items()
    )


def run(X: pd.DataFrame, y: pd.Series, models: dict, min_cv_mean_score = 0.5) -> pd.DataFrame:
    """
    Preprocess the input data.
    
    This function preprocesses the input data by applying the preprocessor
    to all columns.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input data to be preprocessed
        
    Returns
    -------
    pd.DataFrame
        Preprocessed data
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train, X_test = preprocess(X_train, X_test)
    
    return train_models_parallel(models, X_train, y_train, X_test, y_test, min_cv_mean_score, n_jobs=-1)
        
