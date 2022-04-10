from catboost import CatBoostRegressor, Pool
import pandas as pd
import yaml

import pickle
import logging
# import src

config = yaml.safe_load(open('config/params.yaml'))
path_load = config['load']['path']['load']
path_write = config['load']['path']['write']
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

print(path_load)


def load_data() -> (pd.DataFrame, pd.DataFrame):
    train_data = pd.read_csv(f'{path_load}/ds_dask_data.csv', sep=';')
    labels = pd.read_csv(f'{path_load}/target.csv', sep=';')
    return train_data, labels


def transform_data():
    data, target = load_data()
    data.dt = pd.to_datetime(data.dt, format="%Y%m%d")
    target.dt = pd.to_datetime(target.dt, format="%Y%m%d")
    merged = data.merge(right=target, suffixes=("_caller", '_other'), on=['geo_h3_10', 'dt'], how='left')



