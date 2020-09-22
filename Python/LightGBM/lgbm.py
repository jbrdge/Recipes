import lightgbm as lgb
from sklearn import metrics


def lgbm(dataset):
    #split dataset into parts 80:10:10
    eighty_percent = floor(0.8*len(dataset))
    ninety_percent = floor(0.9*len(dataset))
    dtrain=dataset[:eighty_percent]
    dvalid=dataset[eighty_percent:ninety_percent]
    dtest=dataset[ninety_percent:]

    dtrain = lgb.Dataset(train[feature_cols], label=train['is_attributed'])
    dvalid = lgb.Dataset(valid[feature_cols], label=valid['is_attributed'])
    dtest = lgb.Dataset(test[feature_cols], label=test['is_attributed'])

    param = {'num_leaves': 64, 'objective': 'binary'}
    param['metric'] = 'auc'
    num_round = 1000
    bst = lgb.train(param, dtrain, num_round, valid_sets=[dvalid], early_stopping_rounds=10)

    ypred = bst.predict(test[feature_cols])
    score = metrics.roc_auc_score(test['is_attributed'], ypred)
    print(f"Test score: {score}")