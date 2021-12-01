password = input("Enter password: ")

lowercase_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers_list = ["0","1","2","3","4","5","6","7","8","9"]
special_char_list = ["~","!","@","%","^","&","*","_","-","+",";","?","<",">",":",",","`","$","#","(",")","=","'","."]

lowercase = False
uppercase = False
numbers = False
special_char = False

for char in password:
    if char in lowercase_list:
        lowercase = True
    elif char in password:
        if char in uppercase_list:
            uppercase = True

for char in password:
    if char in numbers_list:
        numbers = True
    elif char in password:
        if char in special_char_list:
            special_char = True

if lowercase == False:
    print("Your password must contain at least one lowercase letter.")
if uppercase == False:
     print("Your password must contain at least one uppercase letter.")
if numbers == False:
    print("Your password must contain at least one number.")
if special_char == False:
    print("Your password must contain at least one special character.")
if len(password) < 15:
    print("Your password must have at least 15 characters.")
else:
    print("Your password is valid!")