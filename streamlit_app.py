

import streamlit as st
import sympy as sp

st.title("🧮 간단 계산기")

num1 = st.number_input("첫 번째 숫자", value=0.0, format="%g")
num2 = st.number_input("두 번째 숫자", value=0.0, format="%g")
operation = st.selectbox("연산 선택", ["덧셈 (+)", "뺄셈 (-)", "곱셈 (*)", "나눗셈 (/)"])

result = None
if st.button("계산하기"):
    if operation == "덧셈 (+)":
        result = num1 + num2
    elif operation == "뺄셈 (-)":
        result = num1 - num2
    elif operation == "곱셈 (*)":
        result = num1 * num2
    elif operation == "나눗셈 (/)":
        if num2 == 0:
            st.error("0으로 나눌 수 없습니다.")
        else:
            result = num1 / num2

if result is not None:
    st.success(f"결과: {result}")
