def ansambel(data, model, sign) -> tuple:
    """
    Возвращает кортеж из данных без целевого признака, данные о целевом признаке и предсказания
    """
    y = data[sign]
    x = data.drop(sign, axis=1)
    predict = model.predict(x)
    return x, y, predict
