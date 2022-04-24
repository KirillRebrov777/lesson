income = int(input("Введите значение выручки: "))
outcome = int(input("Введите значение издержек: "))
profit = income - outcome

if profit > 0:
    
    print("Фирма отработала с прибылью")

    profitability = profit / income   
    print('Рентабильность составила {:.2f}'.format(profitability))

    employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / employees  
    print('Прибыль фирмы в расчете на одного сотрудника составила {:.2f}'.format(profit_per_employee))

elif profit == 0:
    print("Фирма не получила прибыль, но и не понесла убытки")

else:
    print("Фирма отработала в убыток")
outcome = int(input("Введите значение издержек: "))

profit = income - outcome

if profit > 0:
    ь
    print("Фирма отработала с прибылью")

    profitability = profit / income   
    print('Рентабильность составила {:.2f}'.format(profitability))

    employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / employees  
    print('Прибыль фирмы в расчете на одного сотрудника составила {:.2f}'.format(profit_per_employee))

elif profit == 0:
    
    print("Фирма не получила прибыль, но и не понесла убытки")

else:
    print("Фирма отработала в убыток")
