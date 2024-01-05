import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, max_error
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score, f1_score
import pandas as pd
import numpy as np


def neural_network(data, model, param):
    if param == "fraud":
        for i in ["repeat_retailer", "used_chip", "used_pin_number", "online_order", "fraud"]:
            data[i] = data[i].astype(int)
    y = data[param]
    x = data.drop([param], axis=1)

    if param == "price":
        predict = model.predict(x)
        metric1 = f"mean_absolute_error: {mean_absolute_error(y, predict)}"
        metric2 = f"mean_squared_error: {mean_squared_error(y, predict)}"
        metric3 = f"r2_score: {r2_score(y, predict)}"
        metric4 = f"max_error: {max_error(y, predict)}"
    else:
        predict = model.predict(x)
        predict = predict.round()
        metric1 = f"f1_score: {f1_score(np.array(y), np.array(predict))}"
        metric2 = f"accuracy_score: {accuracy_score(y, predict)}"
        metric3 = f"roc_auc_score: {roc_auc_score(y, predict)}"
        metric4 = f"recall_score: {recall_score(y, predict)}"

    plt.plot(y.to_numpy()[:100], label="Actual")
    plt.plot(predict[:100], label="Prediction")
    plt.legend()

    predict = pd.concat([pd.DataFrame(predict, columns=["predict"]), pd.DataFrame(y)], axis=1)
    if param == "price":
        return x, y, predict, plt, metric1, metric2, metric3, metric4
    else:
        return x, y, predict, plt, metric1, metric2, metric3, metric4
