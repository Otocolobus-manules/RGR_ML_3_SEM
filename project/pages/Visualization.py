import streamlit as stm
from PIL import Image


image_logo = Image.open("project/data/images/logo.png")
stm.set_page_config(page_title="Предсказания", page_icon=image_logo)
stm.sidebar.write("Визуализация зависимостей")
dataset = stm.sidebar.radio("Датасеты", options=("Датасет для моделей регрессии", "Датасет для моделей классификации"))


if dataset == "Датасет для моделей регрессии":
    stm.title("Визуализация различных зависимостей для датасета регрессии")
    stm.markdown("---")

    stm.markdown("#### 1. Столбиковый график (Bar Plot)")
    stm.image("project/data/images/pyplot/bar_plot_regression.png")
    stm.text("")

    stm.markdown("#### 2. Диаграмма рассеяния (Scatter Plot)")
    stm.image("project/data/images/pyplot/scatter_plot_regression.png")
    stm.text("")

    stm.markdown("#### 3. Гистограмма (Histogram)")
    stm.image("project/data/images/pyplot/histogram_regression.png")
    stm.text("")

    stm.markdown("#### 4. Скрипичный сюжет (Violin Plot)")
    stm.image("project/data/images/pyplot/violin_plot_regression.png")
    stm.text("")

    stm.markdown("#### 5. Коробчатый график (Box Plot)")
    stm.image("project/data/images/pyplot/box_plot_regression.png")
    stm.text("")

    stm.markdown("#### 6. Тепловая карта (Heatmap)")
    stm.image("project/data/images/pyplot/heatmap_regression.png")
    stm.text("")

    stm.markdown("#### 7. Точечный график (Point Plot)")
    stm.image("project/data/images/pyplot/point_plot_regression.png")
    stm.text("")

    stm.markdown("#### 8. График плотности (Density Plot)")
    stm.image("project/data/images/pyplot/density_plot_regression.png")
    stm.text("")

    stm.markdown("#### 9. Счетный участок (Count Plot)")
    stm.image("project/data/images/pyplot/count_plot_regression.png")
    stm.text("")

    stm.markdown("#### 10. График роя (Swarm Plot)")
    stm.image("project/data/images/pyplot/swarm_plot_regression.png")
    stm.text("")

    stm.markdown("#### 11. Парный график (Pair Plot)")
    stm.image("project/data/images/pyplot/pair_plot_regression.png")
    stm.text("")

    stm.markdown("#### 12. График совместного распределения (Joint Distribution Plot)")
    stm.image("project/data/images/pyplot/joint_distribution_plot_regression.png")
    stm.text("")

    stm.markdown("#### 13. Cat Plot (Categorical Plot)")
    stm.image("project/data/images/pyplot/categorical_plot_regression.png")
    stm.text("")

elif dataset == "Датасет для моделей классификации":
    stm.title("Визуализация различных зависимостей для датасета классификации")
    stm.markdown("---")

    stm.markdown("#### 1. Столбиковый график (Bar Plot)")
    stm.image("project/data/images/pyplot/bar_plot_classification.png")
    stm.text("")

    stm.markdown("#### 2. Диаграмма рассеяния (Scatter Plot)")
    stm.image("project/data/images/pyplot/scatter_plot_classification.png")
    stm.text("")

    stm.markdown("#### 3. Гистограмма (Histogram)")
    stm.image("project/data/images/pyplot/histogram_classification.png")
    stm.text("")

    stm.markdown("#### 4. Линейный график (Line Plot)")
    stm.image("project/data/images/pyplot/line_plot_classification.png")
    stm.text("")

    stm.markdown("#### 5. Скрипичный сюжет (Violin Plot)")
    stm.image("project/data/images/pyplot/violin_plot_classification.png")
    stm.text("")

    stm.markdown("#### 6. Коробчатый график (Box Plot)")
    stm.image("project/data/images/pyplot/box_plot_classification.png")
    stm.text("")

    stm.markdown("#### 7. Тепловая карта (Heatmap)")
    stm.image("project/data/images/pyplot/heatmap_classification.png")
    stm.text("")

    stm.markdown("#### 8. Точечный график (Point Plot)")
    stm.image("project/data/images/pyplot/point_plot_classification.png")
    stm.text("")

    stm.markdown("#### 9. График плотности (Density Plot)")
    stm.image("project/data/images/pyplot/density_plot_classification.png")
    stm.text("")

    stm.markdown("#### 10. Счетный участок (Count Plot)")
    stm.image("project/data/images/pyplot/count_plot_classification.png")
    stm.text("")

    stm.markdown("#### 11. Парный график (Pair Plot)")
    stm.image("project/data/images/pyplot/pair_plot_classification.png")
    stm.text("")

    stm.markdown("#### 12. График совместного распределения (Joint Distribution Plot)")
    stm.image("project/data/images/pyplot/joint_distribution_plot_classification.png")
    stm.text("")

stm.markdown("---")
