pureMsg = 'Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven'
numbers = {
    'Zero' : '0',
    'One' : '1',
    'Two': '2',
    'Three' : '3',
    'Four' : '4',
    'Five' : '5',
    'Six': '6',
    'Seven' : '7',
    'Eight' : '8',
    'Nine' : '9',
    'Ten' : '10',
    'Dash' : '-',
} 
msg = pureMsg.split()

for word in msg:
    print(numbers.get(word, word[0]), end='')



# ANOTHER WAY_____________________________

# result=''

# for i in msg:
#     if i in numbers:
#         result += numbers[i]
#     else:
#       result += i[0]

# print(result)