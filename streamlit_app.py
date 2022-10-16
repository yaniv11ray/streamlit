import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/yaniv11ray/streamlit.svg?logo=github&style=social)](https://gitHub.com/yaniv11ray/streamlit)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Vinay Ray')

st.info('Technology Lead | Production Support Engineer | Data Analyst')

icon_size = 30


st_button('twitter', 'https://twitter.com/vinay11ray/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/vinay-ray/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://github.com/yaniv11ray', 'GitHub', icon_size)

