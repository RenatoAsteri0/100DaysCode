'''
1 - Print report
2 - Check resources sufficient?
3 - Process coins
4 - Check transaction succeful?
5 - Make Coffee
'''


'''from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
timmy.shape('turtle')
timmy.color('red')
timmy.forward(300)
print(my_screen.canvheight)
my_screen.exitonclick()'''
from textwrap import shorten

'''metodo = funcoes associadas ao objeto'''
from  prettytable import PrettyTable
# criar um objeto
table = PrettyTable() #objeto criado
print(table)

#table.add_column() > table = objeto, add_column = metodo

table.add_column("pokemon name", ["pikachu", "sceri", "Charm"])
table.add_column("type", ["Eletric", "water","fire"])
table.align = "l"
print(table.get_string(sortby = "pokemon name"))
print(table)