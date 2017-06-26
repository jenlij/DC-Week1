#Day of the week
# day = int(raw_input('Day (0-6)?'))
# weekday = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# print weekday[day]
# if day == 0 or day == 6:
#     print 'Sleep in!'
# else:
#     print 'Go to Work'

#temp conversion
# celsius = float(raw_input('Temperature in C?'))
# farenheight = celsius * 1.8 + 32
# print '%.2f F' %farenheight


#tip calculator
subtotal = float(raw_input("Subtotal: "))
flag = True
while flag == True:
    service_level = raw_input("Level of Service (Good, Fair, Bad): ")
    if service_level == "Good":
        tip = subtotal * 0.2
        flag = False
    elif service_level == "Fair":
        tip = subtotal * 0.15
        flag = False
    elif service_level == "Bad":
        tip = subtotal * 0.1
        flag = False
    else: 
        print "please select 'Good', 'Fair', or 'Bad'"
        
total_bill = subtotal + tip
split_by = int(raw_input("Split how many ways? "))  
split_amount = total_bill / split_by
print "Tip amount: %.2f" %tip
print "Total amount: %.2f" %total_bill
print "Amount per person: %.2f" %split_amount
