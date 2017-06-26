# You'll write a program to help you track which restaurants near ATV you have gone to for lunch.



# Basic features:

# - Show a menu of three restaurants (for example: 1. chipotle, 2. farm burger, and 3. ru san's)

# - Prompt the user to choose one (for example by typing the number 1 for chipotle).

# - Keep track of the user's choice and print out a message that tells them what they chose.


def choose_restaurant():
    choice = int(raw_input("Choose a restaurant: \n1. Naan Stop \n2. Chipotle \n3. Farm Burger \nEnter your number: "))
    return choice
def main():
    restaurants = ["none", "Naan Stop", "Chipotle", "Farm Burger"]
    rounds = 0
    while rounds < 5:
        number = choose_restaurant()
        if number != 0:
            print "You chose %d. %s" %(number, restaurants[number])
            rounds += 1
        else:
            print "exiting program"
            break
#main()

# Intermediate features:

# - Keep prompting them until they choose 0, or until they've finished 5 rounds.

# - Keep track of the number of times they choose each restaurant.

# - If they choose a single restuarant more than 3 times, make them choose another.


def main_function_intermed():
    restaurants = ["none", "Naan Stop", "Chipotle", "Farm Burger"]
    rounds = 0  
    naan_stop = 0
    chipotle = 0
    farm_burger = 0
    while rounds < 5:
        number = choose_restaurant()
        if number == 0:
            print "Exiting program"
            break
        elif number == 1 and naan_stop < 3:
            print "You chose 1. Naan Stop"
            rounds += 1
            naan_stop += 1    
        elif number == 2 and chipotle < 3:
            print "You chose 2. Chipotle"
            rounds += 1
            chipotle += 1
        elif number == 3 and farm_burger < 3:
            print "You chose 3. Farm Burger"
            rounds += 1
            farm_burger += 1
        elif number < 0 or number > 3:
            print "That is not a choice, please enter again"
        else:
            print "You've chosen that restaurant more than 3 times, please choose another."    
    print "Done!"

#main_function_intermed()

def ask_add_remove():
    action = raw_input("Would you like to add or remove a restaurant? (add, remove) ").lower()
    return action

def add_restaurant(menu):
    adding = menu.append(raw_input("Enter a restaurant to add: ").lower())
    return adding

def remove_restaurant(menu):
    entry = raw_input("Enter a restaurant to remove: ").lower()
    if entry in menu and len(menu) != 0:
        removing = menu.remove(entry)
        return removing
    else:
        print "Your entry is not currently part of the menu."
        return menu    

def modify_menu():
    restaurants = ["naan stop", "chipotle", "farm burger"]
    menu_updates = ask_add_remove()
    while menu_updates == "add" or menu_updates == "remove":
        if menu_updates == "add":
            add_restaurant(restaurants)
        elif menu_updates == "remove":
            remove_restaurant(restaurants)  
        menu_updates = ask_add_remove()
    return restaurants

def ask_choice(menu):
    user_choice = raw_input("Choose a restaurant: %s" %menu)
    return user_choice    




# Advanced features:

# - let them add/remove restaurants ******

# - provide an option to sort the restaurants by least/most frequently visited

# - separate the restaurant list from the "manage restaurants" menu

# - clear the screen as they move from menu to menu

# - make each "round" correspond to a day of the week, and then record which days they go to which restaurants

# - you'll want to update the prompt to mention the day ("Monday", "Tuesday", etc.)

# - keep track of more than 5 days - that is, allow them to record multiple weeks of restaurant visits

# - after 5 days, make sure to reset the day counter so that it prompts them to choose a restaurant for "Monday" again










# Super bonus features:

# - use the gnuplot package to draw a bar graph showing restaurant popularity

# - let the user choose which week to graph

# - then, let the user choose multiple weeks to graph