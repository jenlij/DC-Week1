
#tip calculator
# subtotal = float(raw_input("Subtotal: "))
# flag = True
# while flag == True:
#     service_level = raw_input("Level of Service (Good, Fair, Bad): ")
#     if service_level == "Good":
#         tip = subtotal * 0.2
#         flag = False
#     elif service_level == "Fair":
#         tip = subtotal * 0.15
#         flag = False
#     elif service_level == "Bad":
#         tip = subtotal * 0.1
#         flag = False
#     else: 
#         print "please select 'Good', 'Fair', or 'Bad'"
        
# total_bill = subtotal + tip
# split_by = int(raw_input("Split how many ways? "))  
# split_amount = total_bill / split_by
# print "Tip amount: %.2f" %tip
# print "Total amount: %.2f" %total_bill
# print "Amount per person: %.2f" %split_amount

#get subtotal from user
def get_subtotal():
    subtotal = float(raw_input("Subtotal: "))
    return subtotal

#get service level from user
def get_service_level():
    sl = raw_input("Level of Service (Good, Fair, Bad): ")
    return sl

#calculate tip amount
def calc_tip(subtotal, service_level):
    if service_level == "Good":
        tip = subtotal * 0.2
    elif service_level == "Fair":
        tip = subtotal * 0.15
    elif service_level == "Bad":
        tip = subtotal * 0.1
    else:
        tip = 0    
    return tip    

#calculate total bill
def calc_total(sub, tip_amount):
    total_bill = sub + tip_amount
    return total_bill

def main():
    sub = get_subtotal()
    service = get_service_level()
    tip = calc_tip(sub, service)
    total = calc_total(sub, tip)
    print "Tip: %.2f, Total: %.2f" %(tip, total)

main()    
#----------------------------------------------------------------------------

#how many coins
# coin_count = 0
# print "You have %d coins" %coin_count
# add = raw_input("Do you want another? ")  
# while add.lower() == "yes":
#     coin_count += 1
#     print "You have %d coins" %coin_count
#     add = raw_input("Do you want another? ")   
# print "Bye"

# #prints coin count
# def print_count(coin_count): 
#     print "You have %d coins" %coin_count

# #asks user if they want another coin, returns response
# def ask_question():
#     response = raw_input("Do you want another? ").lower()  
#     return response

# #adds a coin, returns new coin count
# def add_coins(initial_count):
#     new_count = initial_count + 1       
#     return new_count        

# #put it all together returns final coin count  
# def main():
#     coin_count = 0
#     print_count(coin_count)
#     while ask_question() == "yes":
#         coin_count = add_coins(coin_count)
#         print_count(coin_count)

# main()

#----------------------------------------------------------------------------

#leetspeak
# letters = ['A','E','G','I','O','S','T']
# leets = ['4','3','6','1','0','5','7']
# new_word = ""
# word = raw_input("Enter your word: ").upper()
# for x in word:
#     if x in letters: #this self-iterates
#         new_word += (leets[letters.index(x)])
#     else:        
#         new_word += x        
# print new_word

# def get_user_input():
#      return raw_input("Enter your word: ").upper()

# def leetspeak(user_input):
#     letters = ['A','E','G','I','O','S','T']
#     leets = ['4','3','6','1','0','5','7']
#     new_word = ""
#     for x in user_input:
#         if x in letters: 
#             new_word += (leets[letters.index(x)])
#         else:        
#             new_word += x
#     return new_word

# def main():
#     user_input1 = get_user_input()
#     return leetspeak(user_input1)

# print main()    