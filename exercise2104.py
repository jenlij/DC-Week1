# for x in range(1,11):
#     print x

# start = int(raw_input("Start from: "))
# end = int(raw_input("End on: ")) 
# for x in range(start,end+1):
#     print x

#odds
# for x in range(1,11,2):
#     print x

# for x in range(1,11):
#     if x%2 != 0:
#         print x

#how many coins
# coin_count = 0
# print "You have %d coins" %coin_count
# add = raw_input("Do you want another? ")  
# while add.lower() == "yes":
#     coin_count += 1
#     print "You have %d coins" %coin_count
#     add = raw_input("Do you want another? ")   
# print "Bye"

# #print square
# for x in range(5):
#     print "*****"


# print "-----------------------"
# for x in range(5):
#         print "*" * 5

# #print square 2  
# n = int(raw_input("Enter and integer: "))          
# for x in range(n):
#     print "*" * n

#print a box
# width = int(raw_input("Width? "))
# height = int(raw_input("Height? "))
# spaces = (width-2)*" "


# if height > 2 and width >= 2:
#     print "*" * width    
#     for x in range(height-2):
#         print "*"+spaces+"*"
#     print "*" * width
# elif height == 2:
#     print "*" * width
#     print "*" * width
# elif height == 1:
#     print "*" * width
# elif height > 2 and width == 1:
#     for y in range(height):
#         print "*"
# else:
#     print "no box"        

#print a triangle
# x = 1
# y = 7
# while x <= 7:
#     space = " " * (y/2)
#     print space + "*" * x
#     x += 2
#     y -= 2

# #print a triangle II
# x = 1
# height = int(raw_input("Enter a Height: "))
# y = height * 4
# while x <= y:
#     space = " " * (y/2)
#     print space + "*" * x
#     x += 2
#     y -= 2

#multiplication table
# for i in range(1,11):
#     for j in range(1,11):
#         print "%d x %d =" %(i,j), i * j


#print a banner
# text = raw_input("Enter Text: ")
# print "*" * (len(text) + 2)
# print "*" + text + "*"
# print "*" * (len(text) + 2)

#triangle numbers
# for x in range(101):
#     print (x * (x + 1)) / 2

#factor a number
# number = int(raw_input("Enter an integer: ")) 
# i = 1
# factors = []
# while i <= number:
#     if number % i == 0:
#         factors.append(i)
#     i+=1    
# print factors        

#Guess a number
#step 1
# secret_number = 5
# print "I am thinking of a number between 1 and 10."
# guess = int(raw_input("What is the number? "))
# while guess != secret_number:
#     print "Nope, try again."
#     guess = int(raw_input("What is the number? "))
# if guess == secret_number:
#     print "Yes! You Win!"

#step 2 Provide a high/low hint
# secret_number = 5
# print "I am thinking of a number between 1 and 10."
# guess = int(raw_input("What is the number? "))
# while guess != secret_number:
#     if guess < secret_number:
#         print "%d is too low" %guess
#     else:
#         print "%d is too high" %guess
#     guess = int(raw_input("What is the number? "))
# if guess == secret_number:
#     print "Yes! You Win!"

#step 3 randomly generated secret number
# import random
# secret_number = random.randint(1,10) 
# print secret_number
# guess = int(raw_input("What is the number? "))
# while guess != secret_number:
#     if guess < secret_number:
#         print "%d is too low" %guess
#     else:
#         print "%d is too high" %guess
#     guess = int(raw_input("What is the number? "))
# if guess == secret_number:
#     print "Yes! You Win!"

#step 4 limited number of guesses
# import random
# secret_number = random.randint(1,10) 
# print secret_number
# print "I am thinking of a number between 1 and 10."
# x = 0 
# guess = -1
# while guess != secret_number and x < 5:
#     print "You have %d guesses left." %(5-x)
#     guess = int(raw_input("What is the number? "))
#     if guess < secret_number:
#         print "%d is too low" %guess
#     elif guess > secret_number:
#         print "%d is too high" %guess           
#     x += 1 
# if guess == secret_number:
#     print "Yes! You Win!"
# if x == 5:
#     print "You ran out of guesses!" 

#Play again           
# import random
# play_again = "Y"
# while play_again == "Y":
#     secret_number = random.randint(1,10) 
#     print secret_number
#     print "I am thinking of a number between 1 and 10."
#     x = 0  
#     guess = -1
#     while guess != secret_number and x < 5:
#         print "You have %d guesses left." %(5-x)
#         guess = int(raw_input("What is the number? "))
#         if guess < secret_number:
#             print "%d is too low" %guess
#         elif guess > secret_number:
#             print "%d is too high" %guess           
#         x += 1 
#     if guess == secret_number:
#         print "Yes! You Win!"
#     if x == 5:
#         print "You ran out of guesses!" 
#     play_again = raw_input("Do you want to play again (Y or N): ")    
# print "Bye!"    

#Bonus exercises
#countdown
# x = 10
# while x >= 0:
#     print x
#     x -= 1
# print "Blast Off!"  

#user input
import time
x = int(raw_input("Enter a number to start your countdown (<=20): "))  
while x > 20:
    x = int(raw_input("Enter a number LESS than or EQUAL to 20: "))
while x >= 0 and x <= 20:
    print x
    x -= 1
time.sleep(1)    
print "Blast Off!"  