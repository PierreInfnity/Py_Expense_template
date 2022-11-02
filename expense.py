import csv
from PyInquirer import prompt
from user import makelistuser , makelistfriends

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": makelistuser()
    },
]

expense_users = []


def new_expense(*args):
    expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": makelistuser()
    },
    {
        "type":"checkbox",
        "name":"friends_involved",
        "message":"Who did you pay for ?:",
        "choices": makelistfriends() 
    },
    ]
    infos = prompt(expense_questions)
    with open('expense_report.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=infos.keys())
        writer.writeheader()
        writer.writerow(infos)
    
    print(infos)
    if (len(infos["friends_involved"]) != 0):
        print("it means for each person : "  , int(infos["amount"]) / len(infos["friends_involved"]))

    print("Expense Added !")
    return True

def build_resume():
    users = makelistuser()
    res = []
    money = 0
    for element in users:
        my_dict = dict()   
        element = element + " doit " + str(money) + " a ..."
        my_dict.update({"name":  element})
        res.append(my_dict)
    print(res)
    return res

debt_payed_question = [
    {
        "type":"checkbox",
        "name":"debt_payed",
        "message":"If you want to mark a debt as payed , check it ?:",
        "choices": build_resume() 
    },
]

def view_resume():
    infos = prompt(debt_payed_question)
    print("Resume Actualised")
    return True







    