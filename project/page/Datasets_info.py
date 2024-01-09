import streamlit as stm
from PIL import Image
import pandas as pd


image_logo = Image.open("project/data/images/logo.png")
stm.set_page_config(page_title="О датасетах", page_icon=image_logo)
stm.sidebar.write("Информация о датасетах")
dataset = stm.sidebar.radio("Датасеты", options=("Датасет для моделей регрессии", "Датасет для моделей классификации"))


if dataset == "Датасет для моделей регрессии":
    data = pd.read_csv("project/data/datasets/regression_data.csv")

    stm.title("Информация о датасете для моделей регресии")
    stm.markdown("---")
    stm.markdown("#### Краткая информация: ")
    stm.text("Данный датасет содержит информацию о ценах и других атрибутах бриллиантов. Целевой признак - "
             "стоимость бриллианта.")

    stm.markdown("#### Датасет:")
    stm.dataframe(data.head())

    stm.markdown("#### Информация о столбцах\n"
                 "- carat - Мера массы\n"
                 "- cut - Бриллиантовая огранка\n"
                 "- color - цвет\n"
                 "- clarity - прозрачность\n"
                 "- depth - глубина бриллианта\n"
                 "- table - верхняя плоская грань\n"
                 "- price - цена\n"
                 "- x - размер по х\n"
                 "- y - размер по у\n"
                 "- z - размер по z")

    stm.markdown("#### О процессе предобработки:\n"
                 "при выполнении предобработки данных были очищенны выбросы и все числовые признаки были приведены к"
                 " типу int или float, а нечисловые признаки были приведены к числовым для столбцов "
                 "cut, color и clarity по следующему принципу(слева указаны значения до, справа после):")
    stm.markdown("для столбца cut:\n"
                 "- Fair: 0\n"
                 "- Good: 1\n"
                 "- Very Good: 2\n"
                 "- Premium: 3\n"
                 "- Ideal: 4\n")
    stm.markdown("для столбца color:\n"
                 "- E: 0\n"
                 "- I: 1\n"
                 "- J: 2\n"
                 "- H: 3\n"
                 "- F: 4\n"
                 "- G: 5\n"
                 "- D: 6")
    stm.markdown("для столбца clarity:\n"
                 "- SI2: 0\n"
                 "- SI1: 1\n"
                 "- VS2: 2\n"
                 "- VS1: 3\n"
                 "- VVS2: 4\n"
                 "- VVS1: 5\n"
                 "- I1: 6\n"
                 "- IF: 7")

elif dataset == "Датасет для моделей классификации":
    data = pd.read_csv("project/data/datasets/classification_data.csv")

    stm.title("Информация о датасете для моделей класификации")
    stm.markdown("---")
    stm.markdown("#### Краткая информация: ")
    stm.text("Данный датасет содержит информацию о различных транзакциях и являлись ли они мошенническими. Целевой "
             "признак - является ли операция мошеннической.")

    stm.markdown("#### Датасет:")
    stm.dataframe(data.head())

    stm.markdown("#### Информация о столбцах:\n"
                 "- distance_from_home — Расстояние от дома, до места где произошла транзакция.\n"
                 "- distance_from_last_transaction — Расстояние от последней транзакции.\n"
                 "- Ratio_to_median_purchase_price — Отношение суммы покупки к медианной цене покупки.\n"
                 "- repeat_retailer — Произошла ли транзакция у того же продавца?\n"
                 "- Used_chip — Осуществляется ли транзакция через чип (кредитная карта).\n"
                 "- Used_pin_number — Произошла ли транзакция с использованием PIN-кода.\n"
                 "- online_order — Является ли транзакция онлайн-заказом?\n"
                 "- fraud – Является ли транзакция мошеннической?\n")

    stm.markdown("#### О процессе предобработки \n"
                 "В процессе предобработки были очищены выбросы также, все числовые признаки принимающие 0 либо 1 "
                 "были приведены к типу bool, все остальные к типу int или float")

stm.markdown("---")
