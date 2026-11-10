from pkg.calculator import Calculator

calc = Calculator()

# Test the complex expression
expr = "2 * 3 - 8 / 2 + 5"
result = calc.evaluate(expr)
print(f"{expr} = {result}")

# Test simpler expressions to isolate the issue
print(f"2 * 3 - 8 = {calc.evaluate('2 * 3 - 8')}")
print(f"8 / 2 + 5 = {calc.evaluate('8 / 2 + 5')}")
print(f"2 * 3 = {calc.evaluate('2 * 3')}")
print(f"8 / 2 = {calc.evaluate('8 / 2')}")
print(f"- 8 / 2 = {calc.evaluate('- 8 / 2')}")
print(f"+ 5 = {calc.evaluate('+ 5')}")
