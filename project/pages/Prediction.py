import streamlit as stm
from PIL import Image
import sklearn.metrics as metrics
import pickle
from sklearn.metrics import f1_score
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('project/python_scripts')
from DataPreprocessing import data_preprocessing as dtp
from the_classic_model_with_a_teacher import polynomial_predict as plmpr
from the_classic_model_with_a_teacher import knn_predict as knnpr
from ansambel import ansambel as ans
from line_predict import line_predict_regression, line_predict_classification
from The_classic_model_without_a_teacher import cluster_process


def plot_func(y, predct):
    plt.plot(y.to_numpy()[:400], label="Actual")
    plt.plot(predct[:400], label="Prediction")
    plt.legend()
    stm.pyplot(plt)


def ansambel_output(dt, sign, _model):
    try:
        x, y, predict = ans(dt, _model, sign)
        df_pred = pd.concat([pd.DataFrame(predict, columns=["predict"]), pd.DataFrame(y)], axis=1)
        stm.markdown("#### список полученных предсказаний")
        stm.dataframe(df_pred)

        if sign == "price":
            stm.markdown(f"Средняя абсолютная ошибка: {metrics.mean_absolute_error(y, predict)}")
            stm.markdown(f"R^2: {metrics.r2_score(y, predict)}")

        elif sign == "fraud":
            stm.markdown(f"значение f1: {f1_score(y, predict)}")

        plot_func(y, predict)

    except:
        stm.markdown('_Возникла ошибка_')


def bool_ratio(result):
    if result == "Да":
        return True
    else:
        return False


image_logo = Image.open("project/data/images/logo.png")
stm.set_page_config(page_title="Предсказания", page_icon=image_logo)
stm.sidebar.write("Получение предсказаний для моделей классификации и регресии")
model = stm.sidebar.radio("Модели", options=("Модель регресии", "Модель классификации",
                                             "Получение предсказания по строчке данных"))

if model == "Модель регресии":
    stm.title("Модель регресии")
    stm.markdown("---")
    file = stm.file_uploader("Загрузите файл с данными")
    data = dtp(file)

    if data is "Except":
        stm.markdown("_Возникла ошибка при работе с файлом_")

    elif data is not None:
        stm.sidebar.write("Получение предсказаний для модели регрессии")
        model = stm.sidebar.radio("Модели", options=("Информационное окно",
                                                     "Модель классического обучения"
                                                     " с учителем(Полиномиальная регрессия)",
                                                     "Модель классического обучения без учителя(метод К соседей)",
                                                     "Ансамблевая модель Boosting",
                                                     "Ансамблевая модель Stacking",
                                                     "Ансамблевая модель Bagging",
                                                     "Полносвязная нейронная сеть"))
        stm.markdown("#### Загруженный датафрейм")
        stm.dataframe(data)

        match model:
            case "Информационное окно":
                stm.markdown("#### Далее вы можете выбрать одну из 6 моделей для получения предсказаний."
                             "На получение предсказаний от некоторых моделей требуется немало времени,"
                             "поэтому сразу приносим извенения за ожидание)")

            case "Модель классического обучения с учителем(Полиномиальная регрессия)":
                filename = "project/models/polynomial_regression.sav"
                model = pickle.load(open(filename, "rb"))
                try:
                    x, y, predict = plmpr(data, model)
                    df_pred = pd.concat([pd.DataFrame(predict, columns=["predict"]), pd.DataFrame(y)], axis=1)
                    stm.markdown("#### список полученных предсказаний")
                    stm.dataframe(df_pred)
                    stm.markdown(f'R^2: {model.score(x, y)}')
                    plot_func(y, predict)
                except:
                    stm.markdown('_При работе с датасетом возникла ошибка_')

            case "Модель классического обучения без учителя(метод К соседей)":
                model = pickle.load(open("project/models/cluster_regression_kmeans.sav", "rb"))
                try:
                    x, y, predict, plt, *args = cluster_process(data, model, "price")

                    stm.markdown("#### Полученные кластеры:  ")
                    stm.dataframe(predict)

                    stm.markdown("#### Метрики и визуализация")
                    for metric in args:
                        stm.markdown(metric)
                    stm.pyplot(plt)
                except:
                    stm.markdown('_При работе с датасетом возникла ошибка_')

            case "Ансамблевая модель Boosting":
                model = pickle.load(open("project/models/boosting_regression.sav", "rb"))
                ansambel_output(data, "price", model)

            case "Ансамблевая модель Stacking":
                model = pickle.load(open("project/models/stacking_regression.sav", "rb"))
                ansambel_output(data, "price", model)

            case "Ансамблевая модель Bagging":
                model = pickle.load(open("project/models/bagging_regression.sav", "rb"))
                ansambel_output(data, "price", model)

            case "Полносвязная нейронная сеть":
                model = pickle.load(open(filename, "rb"))

elif model == "Модель классификации":
    stm.title("Модель классификации")
    stm.markdown("---")
    file = stm.file_uploader("Загрузите файл с данными")
    data = dtp(file)

    if data is "Except":
        stm.markdown("_Возникла ошибка при работе с файлом_")

    elif data is not None:
        stm.sidebar.write("Получение предсказаний для модели классификации")
        model = stm.sidebar.radio("Модели", options=("Информационное окно",
                                                     "Модель классического обучения с учителем",
                                                     "Модель классического обучения без учителя",
                                                     "Ансамблевая модель Boosting",
                                                     "Ансамблевая модель Stacking",
                                                     "Ансамблевая модель Bagging",
                                                     "Полносвязная нейронная сеть"))
        stm.markdown("#### Загруженный датафрейм")
        stm.dataframe(data)

        match model:
            case "Информационное окно":
                stm.markdown("#### Далее вы можете выбрать одну из 6 моделей для получения предсказаний."
                             "На получение предсказаний от некоторых моделей требуется немало времени,"
                             "поэтому сразу приносим извенения за ожидание)")

            case "Модель классического обучения с учителем(KNN)":
                filename = "project/models/knn_model.sav"
                model = pickle.load(open(filename, "rb"),  encoding='ASCII')
                try:
                    x, y, predict = knnpr(data, model)
                    df_pred = pd.concat([pd.DataFrame(predict, columns=["predict"]), pd.DataFrame(y)], axis=1)
                    stm.markdown("#### список полученных предсказаний")
                    stm.dataframe(df_pred)
                    stm.markdown(f"значение f1: {f1_score(y, predict)}")
                    plot_func(y, predict)
                except:
                    stm.markdown('_При работе с датасетом возникла ошибка_')

            case "Модель классического обучения без учителя(Иерархическая кластеризация)":
                model = pickle.load(open("project/models/cluster_classification_ierarh.sav", "rb"))
                try:
                    x, y, predict, plt, *args = cluster_process(data, model, "fraud")

                    stm.markdown("#### Полученные кластеры:  ")
                    stm.dataframe(predict)

                    stm.markdown("#### Метрики и визуализация")
                    for metric in args:
                        stm.markdown(metric)
                    stm.pyplot(plt)
                except:
                    stm.markdown('_При работе с датасетом возникла ошибка_')

            case "Ансамблевая модель Boosting":
                model = pickle.load(open("project/models/boosting_classification.sav", "rb"))
                ansambel_output(data, "fraud", model)

            case "Ансамблевая модель Stacking":
                model = pickle.load(open("project/models/stacking_classification.sav", "rb"))
                ansambel_output(data, "fraud", model)

            case "Ансамблевая модель Bagging":
                model = pickle.load(open("project/models/bagging_classification.sav", "rb"))
                ansambel_output(data, "fraud", model)

            case "Полносвязная нейронная сеть":
                stm.markdown(model)

elif model == "Получение предсказания по строчке данных":
    stm.title("Получение предсказания")
    stm.markdown("---")
    stm.sidebar.write("Выбор модели")
    model = stm.sidebar.radio("Модели", options=("Модель регресии",
                                                 "Модель классификации"))
    if model == "Модель регресии":
        carat = stm.text_input("carat(мера массы)")
        cut = stm.text_input("cut(бриллиантовая огранка) принимает значения от 0 до 4 где: ( "
                             "Fair: 0, "
                             "Good: 1, "
                             "Very Good: 2, "
                             "Premium: 3, "
                             "Ideal: 4 )")

        color = stm.text_input("color(цвет) принимает значения от 0 до 6 где: ( "
                               "E: 0, "
                               "I: 1, "
                               "J: 2, "
                               "H: 3, "
                               "F: 4, "
                               "G: 5, "
                               "D: 6 )")

        clarity = stm.text_input("clarity(прозрачность)принимает значения от 0 до 7 где: ( "
                                 "SI2: 0, "
                                 "SI1: 1, "
                                 "VS2: 2, "
                                 "VS1: 3, "
                                 "VVS2: 4, "
                                 "VVS1: 5, "
                                 "I1: 6, "
                                 "IF: 7 )")

        depth = stm.text_input("depth(Глубина бриллианта)")

        table = stm.text_input("table(верхняя плоская грань)")

        x = stm.text_input("x(размер по х)")

        y = stm.text_input("y(размер по у)")

        z = stm.text_input("z(размер по z)")

        data = [carat, cut, color, clarity, depth, table, x, y, z]
        if "" not in data:
            try:
                model = pickle.load(open("project/models/bagging_regression.sav", "rb"))
                predict = line_predict_regression(data, model)
                stm.markdown(f"#### Предсказанное значение: {predict}")
            except:
                stm.markdown("Одно или несколько значений введены некорректны")

    elif model == "Модель классификации":
        distance_from_home = stm.text_input("Расстояние от дома, до места где произошла транзакция.")

        distance_from_last_transaction = stm.text_input("Расстояние от последней транзакции.")

        Ratio_to_median_purchase_price = stm.text_input("Отношение суммы покупки к медианной цене покупки.")

        repeat_retailer = stm.radio("Произошла ли транзакция у того же продавца?", options=("Да", "Нет"))
        repeat_retailer = bool_ratio(repeat_retailer)

        Used_chip = stm.radio("Осуществляется ли транзакция через чип (кредитная карта).", options=("Да", "Нет"))
        Used_chip = bool_ratio(Used_chip)

        Used_pin_number = stm.radio("Произошла ли транзакция с использованием PIN-кода.", options=("Да", "Нет"))
        Used_pin_number = bool_ratio(Used_pin_number)

        online_order = stm.radio("Является ли транзакция онлайн-заказом?", options=("Да", "Нет"))
        online_order = bool_ratio(online_order)

        data = [distance_from_home, distance_from_last_transaction, Ratio_to_median_purchase_price,
                repeat_retailer, Used_chip, Used_pin_number, online_order]
        if "" not in data:
            try:
                model = pickle.load(open("project/models/bagging_classification.sav", "rb"))
                predict = line_predict_classification(data, model)
                predict = "Транзакция мошенническая" if predict else "Транзакция не является мошеннической"
                stm.markdown(f"#### Предсказанное значение: {predict}")
            except:
                stm.markdown("Одно или несколько значений введены некорректны")

stm.markdown("---")
