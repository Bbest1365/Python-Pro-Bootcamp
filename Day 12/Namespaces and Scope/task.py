enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# ## example
#
#
# def my_function():
#     my_local_var = 2
#
#
# # This will cause a NameErrorr
# print(my_local_var)
#
#
# my_global_var = 3
#
# def my_function():
#     # This works no problems
#     print(my_global_var)