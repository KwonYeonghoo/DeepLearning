import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

# 입력받는 위젯
name = st.text_input("이름을 입력하세요: ")
if name:
    st.write(f"안녕 {name}!")

# slider 위젯
age = st.slider("나이를 선택하세요:",0,100,25)
st.write(f"{age}살이시군요!")

# 체크박스 위젯
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("가장 맘에 드는 언어를 고르세요:", options)
st.write(f"{choice}가 가장 편하시군요!")

# 데이터프레임
data = {
    "이름":["영후", "태준", "민곤", "남형"],
    "나이":[25, 26, 27, 28],
    "거주지":["서울", "말레이", "서울", "서울"]
}
df = pd.DataFrame(data)
st.write(df)
df.to_csv("sampleData.csv")

# 파일 업로드
uploaded_file = st.file_uploader("csv 파일을 선택하세요:", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)