import streamlit as st
import pandas as pd
import numpy as np

# app 실행법: streamlit run app.py

## Application 제목
st.title("Streamlit 첫경험")

## 텍스트 추가
st.write("샘플 텍스트")

## 데이터프레임 추가
df = pd.DataFrame({
    "first":[1,2,3,4],
    "second":[10,20,30,40]
})
st.write("데이터프레임 예시")
st.write(df)

## 선그래프 추가
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=["a","b","c"]
)
st.line_chart(chart_data)