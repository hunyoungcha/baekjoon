num1, num2, num3 = map(int, input().split())

if num1 + num2 == num3 : print(f"{num1}+{num2}={num3}")
elif num1 - num2 == num3 : print(f"{num1}-{num2}={num3}")
elif num1 * num2 == num3 : print(f"{num1}*{num2}={num3}")
elif num1 // num2 == num3 : print(f"{num1}/{num2}={num3}")

elif num1 == num2 + num3 : print(f"{num1}={num2}+{num3}")
elif num1 == num2 - num3 : print(f"{num1}={num2}-{num3}")
elif num1 == num2 * num3 : print(f"{num1}={num2}*{num3}")
elif num1 == num2 // num3 : print(f"{num1}={num2}/{num3}")
