import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(os.path.join(THIS_FOLDER, "expense_report")),"r") as file:
    report = file.read().split("\n")

def main(num:str)->int:
    return int(str(num).strip())


# convert input to int & strip()
report = map(main,report)

# print sorted array
report = sorted(report)

last_num_index = 0
last_num = report[last_num_index]
index = 0

print(report)

#--> failed attempt <--#
# for num in report:
#     index += 1
#     number = num + last_num
#     if number == 2020:
#         print(f"({num}+{last_num}) = 2020")
#         exit()
#     if index >= len(report)-2:
#         index = 0
#         last_num_index += 1
#     print(number)
#-->                <--#

#working attempt:
for num in report:
    for beta_int in report:
        for delta_int in report:
            if num+beta_int+delta_int == 2020:  
                print(f"({num}+{beta_int}+{delta_int})=2020 | {num*beta_int*delta_int}")  