import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv('SampleSuperstore.csv')

label_encoder = LabelEncoder()

categorical_columns = ['Ship Mode', 'Segment', 'City', 'State', 'Category', 'Sub-Category']

for column in categorical_columns:
    data[column] = label_encoder.fit_transform(data[column])

data['Profit'] = (data['Profit'] > 0).astype(int)

X = data[['Ship Mode', 'Segment', 'City', 'State', 'Category', 'Sub-Category', 'Sales', 'Quantity', 'Discount']]
y = data['Profit']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Replace RandomForestClassifier with XGBClassifier
model = xgb.XGBClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy}')

joblib.dump(model, 'profit_loss_model_xgb.pkl')
