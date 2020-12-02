import os
from pathlib import Path

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def parse_password(password: str) -> dict:
    return_dict = {}
    return_dict["char"] = password.split(":")[0].split(" ")[1]
    return_dict["pass_wd"] = password.split(":")[1].strip()
    char_range = password.split(":")[0].split(" ")[0].split("-")
    return_dict["range"] = {"min": int(char_range[0]), "max": int(char_range[1])}
    return return_dict


def is_password_valid(password_dict: dict) -> bool:
    if password_dict["char"] not in password_dict["pass_wd"]:
        return False
    elif password_dict["pass_wd"].count(password_dict["char"]) == password_dict["range"]["min"] \
            or password_dict["pass_wd"].count(password_dict["char"]) == password_dict["range"]["max"]:
        return True
    elif not password_dict["range"]["min"] < password_dict["pass_wd"].count(password_dict["char"]) < password_dict["range"]["max"]:
        return False
    else:
        return True


def main():
    passwords = Path(THIS_FOLDER).joinpath("input.txt").read_text().splitlines()
    
    valid = 0
    for password in passwords:
        valid += int(is_password_valid(parse_password(password)))
        
    print(f"valid passwords: {valid}\ninvalid passwords: {len(passwords) - valid}")


if __name__ == "__main__":
    main()
