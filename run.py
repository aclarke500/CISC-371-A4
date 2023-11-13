from sympy import symbols, Eq, solve

lambda_symbol, w1, i, w2, j = symbols('lambda w1 i w2 j')
equation = Eq((-(-1*i/(2*lambda_symbol-1))**2-(-1*j/(2*lambda_symbol-1))**2+1), 0)
solution = solve(equation, lambda_symbol)

print(solution)
