import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
file_path = "churn_magic.csv"
churn_data = pd.read_csv(file_path, sep=';')

churn_data.rename(columns={'Unnamed: 0': 'row_index', 'magic_feature_0': 'Age',
                           'magic_feature_1': 'Gender', 'magic_feature_2': 'Passport',
                           'magic_feature_3': 'Location',
                           'magic_feature_4': 'Membership', 'magic_feature_5': 'Date of Registration',
                           'magic_feature_6' : 'Account Status',
                           'magic_feature_7': 'Customer ID', 'magic_feature_8': 'Payment',
                           'magic_feature_9': 'Platform', 'magic_feature_10': 'Internet',
                           'magic_feature_11': 'Total Time','magic_feature_14': 'Total Spend',
                            'magic_feature_16': 'Satisfaction',
                           'magic_feature_20': 'Task Completion',
                           'magic_feature_19' : 'Applicable User',
                           'magic_feature_21': 'Reason'}, inplace=True)



churn_data['Account Status'] = churn_data.apply(
    lambda row: 'Yes' if row['Customer ID'].startswith('CID') and row['Account Status'] == '?' else ('No' if row['Account Status'] == '?' else row['Account Status']),
    axis=1
)

churn_data['Satisfaction'] = churn_data['Satisfaction'].replace('', np.nan).astype(float)

churn_data['magic_feature_15'] = churn_data['magic_feature_15'].replace('Error', np.nan).astype(float)

churn_data['magic_feature_12'] = churn_data['magic_feature_12'].replace(-999, np.nan)

categorical_columns = [
    'Gender', 'Passport', 'Location', 'Membership', 'Date of Registration', 'Account Status', 'Customer ID',
    'Payment', 'Platform', 'Internet', 'magic_feature_12','magic_feature_13','Total Spend','magic_feature_15',
    'Satisfaction', 'magic_feature_17', 'magic_feature_18', 'Applicable User',
    'Task Completion', 'Reason'
]

label_encoder = LabelEncoder()
for col in categorical_columns:
    churn_data[col] = label_encoder.fit_transform(churn_data[col].astype(str))

numeric_data = churn_data.drop(['churn_risk_score', 'row_index'], axis=1).select_dtypes(include=[np.number])

desc_stats = numeric_data.describe()

print("\nDescriptive Statistics (mean, median, std) for numeric features:\n", desc_stats)

correlation = numeric_data.corrwith(churn_data['churn_risk_score']).sort_values(ascending=False)

print("\nCorrelation with churn_risk_score:\n", correlation)

top_features = correlation.abs().sort_values(ascending=False).head(5)
print("\nTop 5 features affecting churn risk:\n", top_features)






