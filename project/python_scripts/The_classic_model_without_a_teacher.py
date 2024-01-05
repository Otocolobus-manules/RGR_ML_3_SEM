import matplotlib.pyplot as plt
from sklearn.metrics.cluster import rand_score
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
import pandas as pd


def cluster_process(data, model, param):
    """
    Возвращает датасет с целевым без целевого признака и признак, предсказания, график и метрики
    """
    if param == "fraud":
        if data.shape[0] >= 25000:
            data = data[:25000]
    y = data[param].to_numpy()
    x = data.drop([param], axis=1).to_numpy()
    if param == "price":
        predict = model.predict(x)
    else:
        predict = model.fit_predict(x)

    rnd_sc = f"rand score: {rand_score(predict, y)}"
    silho = f"силуэт: {silhouette_score(x, predict)}\n"
    indx_calin = f"индекс Калински-Харабаза: {calinski_harabasz_score(x, predict)}"
    indx_davis = f"индекс Дэвиса-Боулдина: {davies_bouldin_score(x, predict)}"
    plt.scatter(x[:, 0], x[:, 1], c=predict)
    if param == "price":
        plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], color='black')

    predict = pd.DataFrame(predict, columns=["predict"])
    return x, y, predict, plt, rnd_sc, silho, indx_calin, indx_davis