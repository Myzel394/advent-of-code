import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(THIS_FOLDER, "passwords"), "r") as file:
    passwords = file.read().split("\n")
# passwords = ["2-9 c: ccccccccc","1-3 a: abcde","1-3 b: cdefg"]
    
def password_work(password:str)->dict:
    """
    {
        'raw': '3-4 t: tttt',
        'char': 't',
        'pass_wd': 'tttt',
        'index': {
            '0': 3, 
            '1': 4
            }
    }
    """
    return_dict = {}
    return_dict["char"] = password.split(":")[0].split(" ")[1]
    return_dict["pass_wd"] = password.split(":")[1].strip()
    char_index = password.split(":")[0].split(" ")[0].split("-")
    return_dict["index"] = {"0":int(char_index[0])-1,"1":int(char_index[1])-1}
    return return_dict

def validity_check(password_dict:dict)->bool:
    """
    True/False
    """
    if password_dict["char"] not in password_dict["pass_wd"]:
        return False
    elif len(password_dict["pass_wd"]) < password_dict["index"]["1"]:
        if password_dict["pass_wd"][password_dict["index"]["0"]] == password_dict["char"]:
            return True
    elif password_dict["pass_wd"][password_dict["index"]["0"]] == password_dict["char"] and password_dict["pass_wd"][password_dict["index"]["1"]] == password_dict["char"]:
        return False
    elif password_dict["pass_wd"][password_dict["index"]["0"]] == password_dict["char"] or password_dict["pass_wd"][password_dict["index"]["1"]] == password_dict["char"]:
        return True

invalid = 0
valid = 0
for password in passwords:
    if validity_check(password_work(password)):
        valid += 1
    else:
        invalid += 1
print(f"valid passwords: {valid}\ninvalid passwords: {invalid}")