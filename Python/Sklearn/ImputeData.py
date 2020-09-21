import pandas as pd
from numpy import nan
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

X=[1,2,3,nan,5,nan,7,8,9,10]
y=[1,1,0,1,0,nan,1,0,0,nan]


#split_data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)

def impute(X_train,X_valid):
    """
        Impute example from kaggle, imputes the X_train and X_val
        datasets by fitting to the X_train
    """
    # Imputation
    my_imputer = SimpleImputer()
    imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
    imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

    # Imputation removed column names; put them back
    imputed_X_train.columns = X_train.columns
    imputed_X_valid.columns = X_valid.columns

    return (imputed_X_train,imputed_X_valid)

def simple_impute():
    """
        A more basic example of imputation on one data set alone.
    """
    imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp_mean.fit([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]])
    SimpleImputer()
    X = [[np.nan, 2, 3], [4, np.nan, 6], [10, np.nan, 9]]
    return imp_mean.transform(X)