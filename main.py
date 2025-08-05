from manager import firstcsv, writecsv, readcsv, datefilter,catfilter
from expense import getdate,getcat,getdes,getamount

firstcsv()
numberofinputs = 0

while True:
    user_input = input("Please enter add, read or exit: ")
    if user_input == "add":
        numberofinputs += 1
        writecsv(getdate(), getcat(), getamount(), getdes())

    elif user_input == "read":
        next_command = input("Filtered by 'category' or 'date'? ")
        data, header= readcsv()
        if next_command == "date":
            datefilter(data,header)
        elif next_command == "category":
            catfilter(data,header)

    elif user_input == "exit":
        break
    else:
        print("Unknown command. Please type 'add', 'read', or 'exit'.")

from expense import catlist, explist, datelist

alreadycalled = {}
for i in range(len(catlist)):
    cat = catlist[i]
    amt = explist[i]
    if cat not in alreadycalled:
        alreadycalled[cat] = amt
    else:
        alreadycalled[cat] += amt

alreadycalled2 = {}
for i in range(len(catlist)):
    date = datelist[i]
    amt = explist[i]
    if date not in alreadycalled2:
        alreadycalled2[date] = amt
    else:
        alreadycalled2[date] += amt
        
from visualize import barchart, lineplot
barchart(alreadycalled)
alreadycalled2 = dict(sorted(alreadycalled2.items()))
lineplot(alreadycalled2)
from report import writetext
writetext(numberofinputs,alreadycalled)