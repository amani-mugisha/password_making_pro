import re
strong_password = input("Enter strong password: ")
digits = re.findall('\\d', strong_password)
characters = re.findall(r'[a-zA-Z]', strong_password)
special_char = re.findall(r'[^a-zA-Z0-9]', strong_password)
if len(digits) == 0:
    print(f'This {strong_password} must contain at least 1 digits.')
elif len(characters) < 8 :
    print(f'This {strong_password} must contain at least 8 character.')
elif len(special_char) == 0 :
    print(f'This {strong_password} must contain at least 1 special character.')
else:
    print("Your password is made successfully")





