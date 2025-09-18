

import streamlit as st
import sympy as sp

st.title("함수 연속성 판별 도구")
st.write("""
함수 수식과 판별할 지점을 입력하면, 해당 점에서 연속인지 자동으로 판별합니다.<br>
예시 수식: sin(x)/x, x**2, Abs(x), 1/x 등
""", unsafe_allow_html=True)

expr_str = st.text_input("함수 수식 f(x)=", value="sin(x)/x")
point = st.number_input("연속성 판별 지점 x=", value=0.0, format="%g")

if st.button("연속성 판별하기"):
    x = sp.symbols('x')
    try:
        expr = sp.sympify(expr_str)
        left = sp.limit(expr, x, point, dir='-')
        right = sp.limit(expr, x, point, dir='+')
        value = expr.subs(x, point)
        is_cont = sp.simplify(left - right) == 0 and sp.simplify(left - value) == 0
        st.write(f"좌극한: {left}")
        st.write(f"우극한: {right}")
        st.write(f"함수값: {value}")
        if is_cont:
            st.success(f"f(x)={expr_str}는 x={point}에서 연속입니다.")
        else:
            st.error(f"f(x)={expr_str}는 x={point}에서 연속이 아닙니다.")
    except Exception as e:
        st.error(f"입력 오류: {e}")
