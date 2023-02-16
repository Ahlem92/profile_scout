import pandas as pd

def select_columns(X:pd.DataFrame):
    X=X[['Similar Players','Known As','Value(in Euro)','Positions Played', 'Best Position',
              'Nationality', 'Image Link', 'Age','Height(in cm)', 'Weight(in kg)','Club Name',
              'Contract Until']]
    return X
