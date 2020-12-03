
import os
import glob
import argparse

from azureml.core.run import Run
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
# sklearn.externals.joblib is removed in 0.23
from sklearn import __version__ as sklearnver
from packaging.version import Version
if Version(sklearnver) < Version("0.23.0"):
    from sklearn.externals import joblib
else:
    import joblib

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--data-folder', type=str, help='training dataset')
args = parser.parse_args()

os.makedirs('./outputs', exist_ok=True)

base_path = args.data_folder

run = Run.get_context()

X = np.load(glob.glob(os.path.join(base_path, '**/features.npy'), recursive=True)[0])
y = np.load(glob.glob(os.path.join(base_path, '**/labels.npy'), recursive=True)[0])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)
data = {'train': {'X': X_train, 'y': y_train},
        'test': {'X': X_test, 'y': y_test}}

# list of numbers from 0.0 to 1.0 with a 0.05 interval
alphas = np.arange(0.0, 1.0, 0.05)

for alpha in alphas:
    # use Ridge algorithm to create a regression model
    reg = Ridge(alpha=alpha)
    reg.fit(data['train']['X'], data['train']['y'])

    preds = reg.predict(data['test']['X'])
    mse = mean_squared_error(preds, data['test']['y'])
    run.log('alpha', alpha)
    run.log('mse', mse)

    model_file_name = 'ridge_{0:.2f}.pkl'.format(alpha)
    with open(model_file_name, 'wb') as file:
        joblib.dump(value=reg, filename='outputs/' + model_file_name)

    print('alpha is {0:.2f}, and mse is {1:0.2f}'.format(alpha, mse))
