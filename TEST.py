import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from streamlit_dynamic_filters import DynamicFilters
from PIL import Image

st.set_page_config(page_title = '기구/LCM 3S',
                   layout='wide',
                   initial_sidebar_state='auto',
                   menu_items={'About': 'HDH'})

st.title('테스트 페이지')
