from expense import totalexp
def writetext(numberofinputs, alreadycalled):
    with open("report.txt", "w") as file:
        file.write(f"Total Expenses: {totalexp}\n")
        file.write("By Category:\n")
        file.write(str(alreadycalled) + "\n")
        file.write(f"Daily Average: {totalexp/numberofinputs}\n")
