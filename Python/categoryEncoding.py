import category_encoders as ce
import pandas as pd
from sklearn.datasets import load_boston

def countEncode(data):
    cat_features = ['CHAS', 'RAD']

    # Count Encoding
    count_enc = ce.CountEncoder()

    # Transform the features, rename the columns with the _count suffix, and join to dataframe
    count_encoded = count_enc.fit_transform(ks[cat_features])
    data = data.join(count_encoded.add_suffix("_count"))

    # Train a model 
    train, valid, test = get_data_splits(data)
    train_model(train, valid)

def targetEncode(data):
    # prepare some data
    bunch = load_boston()
    y_train = bunch.target[0:250]
    y_test = bunch.target[250:506]
    X_train = pd.DataFrame(bunch.data[0:250], columns=bunch.feature_names)
    X_test = pd.DataFrame(bunch.data[250:506], columns=bunch.feature_names)

    # use target encoding to encode two categorical features
    enc = TargetEncoder(cols=['CHAS', 'RAD'])

    # transform the datasets
    training_numeric_dataset = enc.fit_transform(X_train, y_train)
    testing_numeric_dataset = enc.transform(X_test)