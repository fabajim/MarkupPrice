import tkinter as tk
from tkinter import messagebox


def isNumber(num):
    try:
        float(num)
    except ValueError:
        return False
    return True


def validate_data(price, units, markup):
    """Validate entered data"""
    pack = [price, units, markup]
    for data in pack:
        if len(data) == 0:
            tk.messagebox.showwarning(title="Error",
                                      message="All fields must be filled")
            return False
        if not isNumber(data):
            tk.messagebox.showwarning(title="Error",
                                      message="Numbers Only")
            return False
        if float(data) <= 0:
            tk.messagebox.showwarning(title="Error",
                                      message="No zero or negative values")
            return False
    return True


def getMarkup(price, units, markup):
    """get and show the markup"""
    price, units, markup = float(price), float(units), float(markup)
    cost = price / units
    percent = markup / 100
    sell_price = cost * percent + cost
    # format sell price and cost
    sell_price = "{:.2f}".format(sell_price)
    cost = "{:.2f}".format(cost)
    message = f"Cost per unit: ${cost}, Sell Price: ${sell_price} with a {markup}% markup"
    tk.messagebox.showinfo(title="Sell Price", message=message)


def get_data():
    """Get data from GUI"""
    purchasePrice = purchase_price_entry.get()
    units = units_entry.get()
    markupPercent = markup_percent_entry.get()
    if validate_data(purchasePrice, units, markupPercent):
        getMarkup(purchasePrice, units, markupPercent)


root = tk.Tk()
root.geometry("400x300")
root.title("Price Markup")

label = tk.Label(root, text="Find the Markup Price", font=('Arial', 18))
label.pack()

frame = tk.Frame(root)
frame.pack()

# get product purchase price and unit cost
product_info_frame = tk.LabelFrame(frame, text="Product Info")
product_info_frame.grid(row=0, column=0, padx=20, pady=10)

purchase_price_label = tk.Label(product_info_frame,
                                text="Purchase Price")
purchase_price_label.grid(row=0, column=0)

units_label = tk.Label(product_info_frame, text="Units or Weight")
units_label.grid(row=0, column=1)

purchase_price_entry = tk.Entry(product_info_frame)
purchase_price_entry.grid(row=1, column=0)

units_entry = tk.Entry(product_info_frame)
units_entry.grid(row=1, column=1)

for widget in product_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# get markup percent
markup_percent_frame = tk.LabelFrame(frame, text="Markup Percent")
markup_percent_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

markup_percent_label = tk.Label(markup_percent_frame,
                                text="Enter Percent Markup")
markup_percent_label.grid(row=0, column=0)

markup_percent_entry = tk.Entry(markup_percent_frame)
markup_percent_entry.insert(-1, '35')
markup_percent_entry.grid(row=0, column=1, padx=10, pady=5)

# submit button
submit_button = tk.Button(frame, text="Submit", command= get_data)
submit_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# window loop
root.mainloop()