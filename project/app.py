from st_pages import Page, show_pages, add_page_title, Section
import streamlit as stm
import json


emoji = json.load(open('project/data/emoji.json'))

add_page_title()
show_pages(
    [
        Page("project/page/Author_info.py", "Об авторе", emoji["home"]),

        Page("project/page/Datasets_info.py", "Информация о датасетах", emoji['red_book']),

        Page("project/page/Prediction.py", "Вывод ML моделей", emoji['green_book']),

        Page("project/page/Visualization.py", "Визуализации", emoji['blue_book']),

        Page("project/page/Z_dont_click_here.py", "Не тыкай суда, ради бога", emoji['orange_book']),
    ]
)
