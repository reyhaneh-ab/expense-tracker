import matplotlib.pyplot as plt
import numpy as np

def barchart(alreadycalled):
    x = np.array(list(alreadycalled.keys()))
    y= np.array(list(alreadycalled.values()))
    plt.bar(x,y, color="hotpink")
    plt.title("Expenses by category")
    plt.xlabel("Category")
    plt.ylabel("Expenses")
    plt.savefig("reports/category_spending_bar.png")
    plt.show()
    

def lineplot(alreadycalled2):
    x2 = np.array(list(alreadycalled2.keys()))
    y2= np.array(list(alreadycalled2.values()))
    plt.plot(x2,y2, color="r", ls= ":",  marker = '*', mec="red", mfc="red")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.title("Money spent on each day")
    plt.xlabel("Date")
    plt.ylabel("Expenses")
    plt.savefig("reports/daily_expense_line.png")
    plt.show()
    