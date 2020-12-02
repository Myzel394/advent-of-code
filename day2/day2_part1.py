import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(THIS_FOLDER, "passwords"), "r") as file:
    passwords = file.read().split("\n")
    
def password_work(password:str)->dict:
    """
    {
        'raw': '3-4 t: tttt',
        'char': 't',
        'pass_wd': 'tttt',
        'range': {
            'min': 3, 
            'max': 4
            }
    }
    """
    return_dict = {}
    return_dict["char"] = password.split(":")[0].split(" ")[1]
    return_dict["pass_wd"] = password.split(":")[1].strip()
    char_range = password.split(":")[0].split(" ")[0].split("-")
    return_dict["range"] = {"min":int(char_range[0]),"max":int(char_range[1])}
    return return_dict

def validity_check(password_dict:dict)->bool:
    """
    True/False
    """
    if password_dict["char"] not in password_dict["pass_wd"]:
        return False
    elif password_dict["pass_wd"].count(password_dict["char"]) == password_dict["range"]["min"] or password_dict["pass_wd"].count(password_dict["char"]) == password_dict["range"]["max"]:
        return True
    elif not password_dict["range"]["min"] < password_dict["pass_wd"].count(password_dict["char"]) < password_dict["range"]["max"]:
        return False
    else:
        return True

invalid = 0
valid = 0
for password in passwords:
    if validity_check(password_work(password)):
        valid += 1
    else:
        invalid += 1
print(f"valid passwords: {valid}\ninvalid passwords: {invalid}")