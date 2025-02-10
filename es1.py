'''

1)
Si dispone del file https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
Indicare quante password hanno:
	a) almeno 8 caratteri -- ok
	b) contengono caratteri alfabetici -- ok
	c) contengono numeri

'''
import re # to use regular expressions

# create a list and read the file , then split when we have \n and \r
list_password = open('password.txt').read().splitlines()
list_password_eigth_char_long = [password for password in list_password if len(password) >= 8]
password_longer_eight_char = len(list_password_eigth_char_long) # n = 349459

# for checking if the char is alphabetic --> re.search('[a-zA-Z]', the_string)
# double list comprehension [word for sentence in text for word in sentence]

list_password_with_alphabetic_char = [password for password in list_password if (re.search('[a-zA-Z]',password))]
password_contains_alphabetic_char = len(list_password_with_alphabetic_char) # 628061

# for checking if the char is numeric --> re.search('[0-9]', choosen_char)
list_password_with_numeric_digit = [password for password in list_password if (re.search('[0-9]', password))]
password_contains_numeric_digit = len(list_password_with_numeric_digit) # 473531

list_password_with_all_conditions = [password for password in list_password if len(password) >= 8 and (re.search('[a-zA-Z]',password)) and (re.search('[0-9]', password))]
password_with_all_condtions = len(list_password_with_all_conditions)

# printing the values
print(password_longer_eight_char) 
print(password_contains_alphabetic_char)
print(password_contains_numeric_digit)
print(password_with_all_condtions)