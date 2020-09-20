from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def get_random_forest_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    """
        Train Random Forest on a number of leaf nodes, evaluate with
        Mean Absolute Error.
    """
    forest_model = RandomForestRegressor(random_state=1)
    forest_model.fit(train_X, train_y)
    melb_preds = forest_model.predict(val_X)
    mae = mean_absolute_error(val_y, melb_preds)
    return(mae)