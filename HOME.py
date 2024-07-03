# 실행코드
# streamlit run PROJECT\HOME.py

############################## 페이지 기본 세팅 ##############################
# TV선행기구모듈러팀 DX LV2 과제 (3S 통합 관리 시스템)
# 2024.6.27 ~
# 코드 작성 : 한동희
#############################################################################

############################## 페이지 기본 세팅 ##############################
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


############################## 첨부파일 불러오기 ##############################


################################### 사이드바 ###################################
st.sidebar.header('아이템별 페이지 바로가기')

# 대분류 5개 (인터페이스, 부자재, 부품, 소재, 포장)
def inter() :
    x1 = st.sidebar.selectbox('인터페이스', ['선택하세요', 'Screw', 'Foam Tape', 'Wire Assy/FFC'])
    if x1 != '선택하세요' :
        dict_x1[x1]()
def sub() :
    x2 = st.sidebar.selectbox('부자재', ['선택하세요', 'PET Tape', 'Rubber', '보호 Film', '부직포', 'Sponge'])
    if x2 != '선택하세요' :
        dict_x2[x2]()
def part() :
    x3 = st.sidebar.selectbox('부품', ['선택하세요', 'Side AV Bracket', 'Wi-Fi Bracket', 'IR/Key Bracket', 'Mount Bracket', 'Wall Mount', '절연 Sheet', 'PEM-nut', 'LED Array 하위부품', 'DPS', 'S-PCB Holder', 'Cover Bottom 수량', 'Cover Bottom 소재'])
    if x3 != '선택하세요' :
        dict_x3[x3]()
def material() :
    x4 = st.sidebar.selectbox('소재', ['선택하세요', 'Resin', 'Press', 'Paint'])
    if x4 != '선택하세요' :
        dict_x4[x4]()
def packing() :
    x5 = st.sidebar.selectbox('포장', ['선택하세요', 'Box', 'Bag'])
    if x5 != '선택하세요' :
        dict_x5[x5]()

# 인터페이스류 (총3개)
def screw() :
    st.switch_page('pages/1_Screw.py')
def foam() :
    st.switch_page('pages/2_foam.py')
def wire() : # 관리대상 아님
    st.switch_page('pages/3_wire.py')

# 부자재류 (총5개)
def pet() :
    st.switch_page('pages/4_pet.py')
def rubber() :
    st.switch_page('pages/5_rubber.py')
def film() :
    st.switch_page('pages/6_film.py')
def bujik() :
    st.switch_page('pages/7_bujik.py')
def sponge() :
    st.switch_page('pages/8_sponge.py')

# 부품류 (총12개)
def side() : #금기태C 과제완료
    st.switch_page('pages/9_side.py')
def wifi() :
    st.switch_page('pages/10_wifi.py')
def ir() : #박충석C 과제완료
    st.switch_page('pages/11_ir.py')
def mount() :
    st.switch_page('pages/12_mount.py')
def wall() :
    st.switch_page('pages/13_wall.py')
def insul() : # 권세진C 과제완료
    st.switch_page('pages/14_insul.py')
def pemnut() :
    st.switch_page('pages/15_pemnut.py')
def led() :
    st.switch_page('pages/16_led.py')
def dps() :
    st.switch_page('pages/17_dps.py')
def spcb() :
    st.switch_page('pages/18_spcb.py')
def cb_q() :
    st.switch_page('pages/19_cb_q.py')
def cb_m() :
    st.switch_page('pages/20_cb_m.py')

# 소재류 (총3개)
def resin() :
    st.switch_page('pages/21_resin.py')
def press() :
    st.switch_page('pages/22_press.py')
def paint() :
    st.switch_page('pages/23_paint.py')

# 포장류 (총2개)
def box() :
    st.switch_page('pages/24_box.py')
def bag() :
    st.switch_page('pages/25_bag.py')

dict_x0 = {'인터페이스' : inter, '부자재' : sub, '부품' : part, '소재' : material, '포장' : packing}
dict_x1 = {'Screw' : screw, 'Foam Tape' : foam, 'Wire Assy/FFC' : wire}
dict_x2 = {'PET Tape' : pet, 'Rubber' : rubber, '보호 Film' : film, '부직포' : bujik, 'Sponge' : sponge}
dict_x3 = {'Side AV Bracket' : side, 'Wi-Fi Bracket' : wifi, 'IR/Key Bracket' : ir, 'Mount Bracket' : mount, 'Wall Mount' : wall, '절연 Sheet' : insul, 'PEM-nut' : pemnut, 'LED Array 하위부품' : led, 'DPS' : dps, 'S-PCB Holder' : spcb, 'Cover Bottom 수량' : cb_q, 'Cover Bottom 소재' : cb_m}
dict_x4 = {'Resin' : resin, 'Press' : press, 'Paint' : paint}
dict_x5 = {'Box' : box, 'Bag' : bag}

x0 = st.sidebar.selectbox('대분류', ['선택하세요', '인터페이스', '부자재', '부품', '소재', '포장'])
if x0 != '선택하세요' :
    dict_x0[x0]()
    
################################# 메인 페이지 #################################
# >>>>>>>>>>>>>>>>>>>>>>>>>>> 연도마다 제목 수정 <<<<<<<<<<<<<<<<<<<<<<<<<<<
st.title('25년 기구/LCM 통합 3S')

empty1, top_left_01, epmty2 = st.columns([0.1, 1.0, 0.1])
with top_left_01:
    image = Image.open('PROJECT/HOME_image.jpg')
    st.image(image, width = 1000)
