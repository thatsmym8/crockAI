from pkg.calculator import Calculator

calc = Calculator()

# Test the problematic expression
result = calc.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")

# Test other expressions
print(f"3 + 5 = {calc.evaluate('3 + 5')}")
print(f"10 - 4 = {calc.evaluate('10 - 4')}")
print(f"3 * 4 = {calc.evaluate('3 * 4')}")
print(f"10 / 2 = {calc.evaluate('10 / 2')}")
print(f"3 * 4 + 5 = {calc.evaluate('3 * 4 + 5')}")
print(f"2 * 3 - 8 / 2 + 5 = {calc.evaluate('2 * 3 - 8 / 2 + 5')}")
