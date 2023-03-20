import os
from uuid import uuid4

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from tdt import TrustDataTools
from tdt.config.credentials import get_initialization_args
from tdt.models import TDTModelSignature
from tdt.models.model_calibration import (ModelCalibration_Isotonic,
                                          ModelCalibration_Platt,
                                          ModelCalibrationMetric,
                                          ModelCalibrationType,
                                          evaluate_metrics)
from tdt.steps.artifacts import TDTModelArtifact
from tdt.training_results import TrainingResults

tdt = TrustDataTools('mlflow')
tdt.initialize(**get_initialization_args('mlflow'))


inputs = [
    {"name": "fixed acidity", "type": "double"},
    {"name": "volatile acidity", "type": "double"},
    {"name": "citric acid", "type": "double"},
    {"name": "residual sugar", "type": "double"},
    {"name": "chlorides", "type": "double"},
    {"name": "free sulfur dioxide", "type": "double"},
    {"name": "total sulfur dioxide", "type": "double"},
    {"name": "density", "type": "double"},
    {"name": "pH", "type": "double"},
    {"name": "sulphates", "type": "double"},
    {"name": "alcohol", "type": "double"},
]
SIGNATURE = TDTModelSignature(inputs)  # Here, we are creating as a constant as it will be used across models


def sklearn_training_function(parameters: dict = None) -> TrainingResults:  # Method "signature" must follow this

    # The loading of the data can be done outside the training function and added to the parameters.
    data = pd.read_csv(
        'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=";")
    data['quality'] = (data['quality'] >= 6).astype(int)
    train, test = train_test_split(data)

    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    model_instance = LogisticRegression()  # Using default values
    model_instance.fit(train_x, train_y)

    predicted_qualities = model_instance.predict(test_x)

    return TrainingResults(model_instance,
                           flavor='sklearn',
                           signature=SIGNATURE,
                           input_data=train,
                           output_data=predicted_qualities)


tdt_sklearn_model = tdt.train(sklearn_training_function,
                              'TDT demo sklearn model logistic',
                              'sklearn')

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=";")
df['quality'] = (df['quality'] >= 6).astype(int)

sklearn_calib = ModelCalibration_Isotonic(
    input_model=tdt_sklearn_model,
    calibration_type="platt",
    inference_cols=["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                     "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"],
    output_cols=["quality"],
    df=df
)
sklearn_calib_model = sklearn_calib.train()
print(sklearn_calib_model)

df_metrics = evaluate_metrics(calibration_type="platt", model=sklearn_calib_model, df=df,
                              inference_cols=["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                                              "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"], output_cols=["quality"]
                              )

print(df_metrics)
