
# XGBoost did pretty good here..

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

from xgboost import XGBRegressor
import joblib

df = pd.read_csv ( "WineQT.csv" )

df = df.drop ( columns = ["Id"] )

X = df.drop ( columns = ["quality"] )
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split ( X, y, test_size = 0.2, random_state = 42 )

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform ( X_train )
X_test_scaled  = scaler.transform ( X_test )

model = XGBRegressor (
    n_estimators = 500,
    max_depth = 4,
    learning_rate = 0.05,
    subsample = 0.8,
    colsample_bytree = 0.8,
    objective = "reg:squarederror",
    random_state = 42,
    n_jobs = -1
)

model.fit ( X_train_scaled, y_train )

y_pred = model.predict ( X_test_scaled )

rmse = np.sqrt ( mean_squared_error ( y_test, y_pred ) )
mae  = mean_absolute_error ( y_test, y_pred )

print ( "RMSE: {}; MAE: {}".format ( str ( rmse ), str ( mae ) ) )

joblib.dump ( model, "wine_model.pkl" )
joblib.dump ( scaler, "scaler.pkl" )

print ( "Done" )
