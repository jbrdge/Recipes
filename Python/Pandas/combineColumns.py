    import pandas as pd
    import itertools

    cat_features = ['col1', 'co2', 'col3', 'col4', 'col5']
 
    def combine_colums(df, cat_features)
        df_combine = pd.DataFrame(index=df.index)
        for colA, colB in itertools.combinations(cat_features, 2):
            new_col_name = '_'.join([colA, colB])

            # Convert to strings and combine
            new_values = clicks[colA].map(str) + "_" + clicks[colB].map(str)

            encoder = preprocessing.LabelEncoder()
            df_combine[new_col_name] = encoder.fit_transform(new_values)