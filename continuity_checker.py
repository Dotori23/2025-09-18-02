import sympy as sp

def is_continuous_at(expr, var, point):
    """
    expr: sympy 수식 (예: sp.sin(x)/x)
    var: sympy 기호 (예: x)
    point: 판별할 점 (숫자)
    """
    left = sp.limit(expr, var, point, dir='-')
    right = sp.limit(expr, var, point, dir='+')
    value = expr.subs(var, point)
    return sp.simplify(left - right) == 0 and sp.simplify(left - value) == 0

if __name__ == "__main__":
    x = sp.symbols('x')
    # 예시: f(x) = sin(x)/x, x=0에서 연속성 판별
    expr = sp.sin(x)/x
    point = 0
    result = is_continuous_at(expr, x, point)
    print(f"f(x) = sin(x)/x, x=0에서 연속성: {result}")
