# sum = [2*n for n in range(1,5)]
#
# print(sum)
#
#
# names = ['Alex','Beth','Caroline','Dave','Elanor','Freddie']
# short_names = [name.upper() for name in names if len(name)>5]
# print(short_names)
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [ int(numbers) for numbers in list_of_strings]
#
# result = [i for i in numbers if i%2 ==0]
# print(result)


# Data Overlap
with open('file1.txt') as file1:
    i = [int(i) for i in file1.readlines()]

with open('file2.txt') as file2:
    j = [int(j) for j in file2.readlines()]

result = []
for number1 in i:
    for number2 in j:
        if number1 == number2:
            if number1 not in result:
                result.append(number2)

print(result)