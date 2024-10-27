# import another_module
# from turtle import Turtle, Screen
#
#
# print(another_module.another_variable)
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color("Orangered1")
# timmy.forward(15)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtie","Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

print(table)