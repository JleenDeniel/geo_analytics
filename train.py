from catboost import CatBoostRegressor, CatBoost, Pool
import pandas as pd
import yaml

import pickle
import logging
import src

config = yaml.safe_load(open('config/params.yaml'))
path_load = config['load']['path']['load']
path_write = config['load']['path']['write']
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

