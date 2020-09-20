from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_decision_tree_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    """
        Train decision tree on a number of leaf nodes, evaluate with
        Mean Absolute Error.
    """
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, 
                                  random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)