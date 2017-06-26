# #upper case string
# input_string_1 = raw_input("Enter a string: ")
# uppercase_string = input_string_1.upper() 
# print uppercase_string

# #capitalized string
# input_string_2 = raw_input("Enter a string: ")
# captialized_string = input_string_2.capitalize()
# print captialized_string

#reverse string
# input_string_3 = raw_input("Enter a string: ")
# reversed_string = input_string_3[::-1]
# print reversed_string

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


#long long vowels
# vowels = ['a','e','i','o','u']
# word = raw_input("Enter your word: ").lower()
# new_word = ""
# for n in range(len(word)):
#     if word[n] in vowels and n < len(word)-1:
#         if word[n] == word[n+1]:
#             new_word += word[n] * 4 
#         else:
#             new_word += word[n] #this makes 5 total vowels
#     else:
#         new_word += word[n]                
# print new_word.capitalize()             


#caesar cipher
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#encryption = (x + k) % 26 
#decryption = (x - k) % 26
k = 13
new_letter = ""
sentence = "lbh zhfg hayrnea jung lbh unir yrnearq"
decrypted_sentence = ""

for x in sentence: 
    if x in alpha:
        new_letter = alpha[(alpha.index(x) - k) % 26]
    else: 
        new_letter = ' '    
    decrypted_sentence += new_letter
print decrypted_sentence
