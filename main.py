from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import *

print(logo)

bid_info = {}

response = 'yes'
while response == 'yes' :

    name = input("What is your name ")
    amount = input("what is the bid amount ")
    response.lower() not in {"yes", "no"}
    response = input("Please enter yes or no: ")
    if response == 'yes':
      clear()

    for x in range(3):    
        new_key = name
        new_age = amount
        bid_info[new_key] = new_age

    else:
        for key, value in bid_info.items():
          highest = ''
          if value > highest:
            highest = value

    print(f'the highest bid is {key} {highest}')


print(bid_info)

