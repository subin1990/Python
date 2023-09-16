import math
import Menu
COFFEEPOWDER =[1000]
MILK= [1000]
WATER= [1000]
SUGAR= [200]
FLAVOURS =[200]

global Coffee_powder_stock
global Milk_stock
global Water_stock
global Sugar_stock
global Flavours_stock

Coffee_powder_stock = sum(COFFEEPOWDER)
Milk_stock = sum(MILK)
Water_stock = sum(WATER)
Sugar_stock = sum(SUGAR)
Flavours_stock = sum(FLAVOURS)
print(Coffee_powder_stock)
print(Milk_stock)
print(Sugar_stock)
print(Flavours_stock)
Latee=1
Expresso=1
Cappuccino=1
CofeePowder_required = Latee * Menu.Menu[0]['Coffee Powder'] + Expresso * Menu.Menu[1][
        'Coffee Powder'] + Cappuccino * Menu.Menu[2]['Coffee Powder']
Milk_required = Latee * Menu.Menu[0]['Milk'] + Expresso * Menu.Menu[1]['Milk'] + Cappuccino * Menu.Menu[2][
        'Milk']
Water_required = Latee * Menu.Menu[0]['Water'] + Expresso * Menu.Menu[1]['Water'] + Cappuccino * Menu.Menu[2][
        'Water']
Sugar_required = Latee * Menu.Menu[0]['Sugar'] + Expresso * Menu.Menu[1]['Sugar'] + Cappuccino * Menu.Menu[2][
        'Sugar']
Flavours_required = Latee * Menu.Menu[0]['Flavours'] + Expresso * Menu.Menu[1]['Flavours'] + Cappuccino * \
                        Menu.Menu[2]['Flavours']
print(Milk_required)
print(Water_required)
print(Sugar_required)
print(Flavours_required)