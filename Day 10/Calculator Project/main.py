import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8
def subtraction(n1, n2):
    return n1 - n2
my_favourite_calculation = subtraction
my_favourite_calculation(3, 5)  # Will return 8
def multiplication(n1, n2):
    return n1 * n2
my_favourite_calculation = multiplication
my_favourite_calculation(3, 5)  # Will return 8
def division(n1, n2):
    return n1 / n2
my_favourite_calculation = division
my_favourite_calculation(3, 5)  # Will return 8
n1 = float(input('What\'s the first number? '))
# loop = True
while True:
    # n1 = float(input('What\'s the first number? '))
    print('+')
    print('-')
    print('*')
    print('/')
    operation = input('Pick and operation: ')
    n2 = float(input('What\'s the next number?: '))

    if operation == "+":
        print(f'{n1} + {n2} = {add(n1,n2)}')
        calculate = (add(n1,n2))
    elif operation == "-":
        print(f'{n1} + {n2} = {subtraction(n1,n2)}')
        calculate = subtraction(n1,n2)
    elif operation == '*':
        print(f'{n1} + {n2} = {multiplication(n1,n2)}')
        calculate = multiplication(n1,n2)
    elif operation == '/':
        print(f'{n1} + {n2} = {division(n1,n2)}')
        calculate = division(n1,n2)
    yes_or_no = input(f'Type \'y\' to continue calculating with {calculate}, or type \'n\' to start new calculation: ').lower()

    if yes_or_no == 'y':
        n1 = calculate
    elif yes_or_no == 'n':
        print('\n'*20)
        n1 = float(input('What\'s the first number? '))
