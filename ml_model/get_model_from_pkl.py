import joblib
import pathlib

dir_path = pathlib.Path.cwd()
rf = joblib.load(f'{dir_path}/ml_model/joblib_model.pkl')
