import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv('SampleSuperstore.csv')

label_encoders = {}

categorical_columns = ['Ship Mode', 'Segment', 'City', 'State', 'Category', 'Sub-Category']

for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

joblib.dump(label_encoders, 'label_encoders.pkl')
