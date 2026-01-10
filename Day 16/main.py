# # import another_module
# # print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("CornflowerBlue")
# timmy.left(90)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table_1 = PrettyTable()
table_1.field_names = ["Pokemon name ", "Type"]
table_1.add_row(["Pikachu", "Electric"])
table_1.add_row(["Squirtle", "Water"])
table_1.add_row(["Charmander", "Fire"])
print(table_1)
table_2 = PrettyTable()
table_2.add_column("Pokemon name", ["Pikachu", "Squirtle","Charmander"])
table_2.add_column("Type", ["Electric", "Water","Fire"])
table_2.align = "l"
print(table_2)
