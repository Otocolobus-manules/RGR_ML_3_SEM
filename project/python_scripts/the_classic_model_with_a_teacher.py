from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from imblearn.over_sampling import RandomOverSampler


def knn_predict(data, model) -> tuple:
    """
    Возвращает кортеж из данных без целевого признака, данные о целевом признаке и предсказания
    """
    y = data["fraud"]
    x = data.drop(["fraud"], axis=1)
    overs = RandomOverSampler(random_state=42)
    x_balanced, y_balanced = overs.fit_resample(x, y)
    scaler = StandardScaler()
    x_balanced = scaler.fit_transform(x_balanced)
    predict = model.predict(x_balanced)
    return x_balanced, y_balanced, predict


def polynomial_predict(data, model) -> tuple:
    """
    Возвращает кортеж из данных без целевого признака, данные о целевом признаке и предсказания
    """
    pf = PolynomialFeatures(5)
    y = data["price"]
    x = data.drop(["price"], axis=1)
    x = pf.fit_transform(x)

    predict = model.predict(x)
    return x, y, predict
