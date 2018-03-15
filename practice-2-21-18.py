# company_list = ["starbucks", "snapchat", "target"]
#
# def printers(company_list):
#     for company in company_list:
#         print(company)
# # printers(company_list)
#
# def get_initials(company_list):
#     answer = ""
#
#     for company in company_list:
#         answer += company[0]
#
#     return answer

# print(get_initials(company_list))

def is_best_number():
    user_input = input("What is the best number ever? ")
    if user_input is 27:
        return True
    else:
        return False

answer = is_best_number()

if answer:
    print("they got the best number")
else:
    print("bad number")
