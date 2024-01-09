import streamlit as stm
from PIL import Image


image_logo = Image.open("project/data/images/logo.png")
stm.set_page_config(page_title="НЕ НАЖИМАЙ СУДА", page_icon=image_logo)

stm.title("Топ смешных картинок")
stm.markdown("---")

stm.markdown("#### 1. Смешной котик который ничего не понимает.")
stm.image("project/data/images/funny_pictures/1.png")
stm.markdown("---")

stm.markdown("#### 2. Глупышка котик не знающий даже основ математики.")
stm.image("project/data/images/funny_pictures/2.png")
stm.markdown("---")

stm.markdown("#### 3. Смешные капибары(их много).")
stm.image("project/data/images/funny_pictures/3.png")
stm.markdown("---")

stm.markdown("#### 4. Котик))).")
stm.image("project/data/images/funny_pictures/4.png")
stm.markdown("---")

stm.markdown("#### 5. Недовольная жабка :/.")
stm.image("project/data/images/funny_pictures/5.png")
stm.markdown("---")

stm.markdown("#### 6. Плачущий котик(((.")
stm.image("project/data/images/funny_pictures/6.png")
stm.markdown("---")

stm.markdown("#### 7. Котик который от всего устал(((.")
stm.image("project/data/images/funny_pictures/7.png")
stm.markdown("---")

stm.markdown("#### 8. Серьезный котик с серьезным взглядом на будущее.")
stm.image("project/data/images/funny_pictures/8.png")
stm.markdown("---")

stm.markdown("#### 9. Котик который хочет спать.")
stm.image("project/data/images/funny_pictures/9.png")
stm.markdown("---")

stm.markdown("#### 10. Котик попавший в забавную ситуацию.")
stm.image("project/data/images/funny_pictures/10.png")
stm.markdown("---")
