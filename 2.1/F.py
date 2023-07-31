name = input()
price = int(input())
weight = int(input())
money = int(input())
result_1 = price * weight
result_2 = money - price * weight
print("Чек")
print(name, "-", str(weight) + "кг", "-", str(price) + "руб/кг")
print("Итого:", str(round(result_1)) + "руб")
print(f"Внесено: {money}руб")
print("Сдача:", str(round(result_2)) + "руб")
