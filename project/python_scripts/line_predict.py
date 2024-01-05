from pandas import DataFrame as Df


def line_predict_regression(data, model):
    """
    Возвращает предсказанное значение
    """
    data = [float(x) for x in data]
    df = Df(data).T
    predict = model.predict(df)
    return predict[0]


def line_predict_classification(data, model):
    """
    Возвращает предсказанное значение
    """
    for i in range(3):
        data[i] = float(data[i])
        df = Df(data).T
        predict = model.predict(df)
        return predict[0]
