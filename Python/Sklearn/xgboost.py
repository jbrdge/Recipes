from xgboost import XGBRegressor

my_model = XGBRegressor()
my_model.fit(X_train, y_train)