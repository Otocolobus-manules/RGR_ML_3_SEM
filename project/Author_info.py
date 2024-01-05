import streamlit as stm
from PIL import Image


image_logo = Image.open("project/data/images/logo.png")
stm.set_page_config(page_title="Об Авторе", page_icon=image_logo)
stm.sidebar.write("Основная информация об авторе")

stm.title("РАСЧЕТНО-ГРАФИЧЕСКАЯ РАБОТА ПО ДИСЦИПЛИНЕ «МАШИННОЕ ОБУЧЕНИЕ И БОЛЬШИЕ ДАННЫЕ».")
stm.markdown("---")
stm.header("Тема: «Разработка Web-приложения (дашборда) для инференса (вывода) моделей ML и анализа данных»")
stm.subheader("Выполнил: Абрамов Егор ФИТ-221")
stm.image("project/data/images/my_photo.png")
