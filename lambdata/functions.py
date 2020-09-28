'''The functions and objects of the lambdata package
'''


import numpy as np
import pandas as pd
from scipy import stats


class MyDataFrame(pd.DataFrame):
    #Modified dataframe to include functions built previously
    def wrangle(self, cardinality=100):
        # A basic wrangle function that deletes columns of constant data
        # and columns that have more than an input number of unique object
        # data
        df = self
        df = df.drop([col for col in df if df[col].nunique() == 1],
                     axis=1)
        hc = [col for col in df.describe(include='object').columns
              if df[col].nunique() > cardinality]
        df = df.drop(hc, axis=1)
        return df

    def date_split(self):
        # A function to split datetime objects into separate month, day,
        # and year columns.
        df = self
        dates = [col for col in df if df[col].dtype == 'datetime64[ns]']
        for col in dates:
            df[col+'_month'] = list(df[col].dt.month)
            df[col+'_day'] = list(df[col].dt.day)
            df[col+'_year'] = list(df[col].dt.year)
        return df

    def cont_chi2(self, col1, col2):
        # A function that outputs the contengency table and resulting chi2
        # statistic information given two columns of the DataFrame
        contingency = pd.crosstab(col1, col2)
        print(contingency)
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
        print("chi2 statistic", chi2)
        print("p value", p_value)
        print("degrees of freedom", dof)
        print("expected frequencies table \n", expected)