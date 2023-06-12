import joblib
import pandas as pd

rf = joblib.load('joblib_model.pkl')
d = {'region': 39, 'level': 3, 'levels': 5, 'rooms': 2, 'area': 50.0, 'kitchen_area': 10.0}
print(rf.predict(pd.DataFrame(data=d, index=[0])))


