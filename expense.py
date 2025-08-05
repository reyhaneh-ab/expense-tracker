totalexp = 0  
explist = []  
datelist=[]
catlist = []

def getamount():
    amount = float(input("Amount (float) : "))
    if amount < 0:
        raise ValueError("Negative amounts are not allowed.")
    global totalexp
    totalexp += amount
    explist.append(amount)
    return amount


from datetime import datetime

def getdate():
    while True:
        user_input = input("Date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(user_input, "%Y-%m-%d")
            datelist.append(date.date())
            return date.date()
        except ValueError:
            print("Invalid format. Please enter the date as YYYY-MM-DD.")

def getcat():
    cat = input("Category (str) : ")
    catlist.append(cat)
    return cat                      

def getdes():
    des = input("Description (str) : ")
    return des