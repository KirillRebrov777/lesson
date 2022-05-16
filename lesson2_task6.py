# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

goods = []  # создание пустого списка для заполнения товарами
params = {'назавание': None, 'цена': None, 'количество': None, 'единица измерения': None}  # шаблон словаря
i = 1  # начальное значение порядкового номера товара

# цикло заполнения структуры данных
while True:
    quite = input("Для ввода товара нажмите Enter, чтобы закончить ввод введите q: ")
    if quite.lower() == 'q' or quite.lower() == 'й':  # условие выхода из цикла
        break
    new_params = params.copy()  # создание копии шаблона словаря для текущего товара
    for key in new_params.keys():  # перебор ключей словаря для заполнения
        new_params[key] = input(f'Введите характеристику товара - {key}: ')
    new_params['цена'] = float(new_params['цена'])  # цена как правило в формате: рублей.копеек
    new_params['количество'] = int(new_params['количество'])  # допустим, что товар продаем штуками, комплектами и т.д.
    goods.append((i, new_params))  # добавление кортежа из порядкового номера и словаря параметров в список
    i += 1  # увеличение порядкового номера товара

# вывод списка товаров
print('Список товаров')
print(goods)

# создание аналитики
analytics = {'назавание': [], 'цена': [], 'количество': [], 'единица измерения': []}  # шаблон словаря для аналитики
for good in goods:  # перебор товаров
    for key in good[1].keys():  # перебор параметров
        analytics[key].append(good[1].get(key))  # добавление значений в словарь аналитики

# вывод аналитики
print('Аналитика')
print(analytics)
