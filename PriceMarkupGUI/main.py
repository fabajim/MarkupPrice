import tkinter as tk
from tkinter import messagebox


class PriceMarkup:
    def __init__(self):
        root = tk.Tk()
        root.geometry("400x350")
        root.title("Price Markup")

        label = tk.Label(root, text="Find the Markup Price", font=('Arial', 18))
        label.pack()

        frame = tk.Frame(root)
        frame.pack()

        # input variables
        self.purchased_at = ""
        self.units = ""
        self.percent_markup = ""

        # calculated variables
        self.cost = ""
        self.sell_price = ""

        # get product purchase price and unit cost
        product_info_frame = tk.LabelFrame(frame, text="Product Info")
        product_info_frame.grid(row=0, column=0, padx=20, pady=10)

        purchase_price_label = tk.Label(product_info_frame,
                                        text="Purchase Price")
        purchase_price_label.grid(row=0, column=0)

        units_label = tk.Label(product_info_frame, text="Units or Weight")
        units_label.grid(row=0, column=1)

        purchase_price_entry = tk.Entry(product_info_frame,
                                        textvariable=self.purchased_at)
        purchase_price_entry.grid(row=1, column=0)

        units_entry = tk.Entry(product_info_frame, textvariable=self.units)
        units_entry.grid(row=1, column=1)

        for widget in product_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # get markup percent
        markup_percent_frame = tk.LabelFrame(frame, text="Markup Percent")
        markup_percent_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        markup_percent_label = tk.Label(markup_percent_frame,
                                        text="Enter Percent Markup")
        markup_percent_label.grid(row=0, column=0)

        markup_percent_entry = tk.Entry(markup_percent_frame,
                                        textvariable=self.percent_markup)
        markup_percent_entry.insert(-1, '35')
        markup_percent_entry.grid(row=0, column=1, padx=10, pady=5)

        # submit button
        submit_button = tk.Button(frame, text="Submit" """command=self.get_data""")
        submit_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        # Display output
        output_frame = tk.LabelFrame(frame, text="Calculated Data")
        output_frame.grid(row=4, column=0, sticky="news", padx=10, pady=15)
        
        cost_label = tk.Label(output_frame,
                              text="Product unit cost: ")
        cost_label.grid(row=0, column=0, sticky="W")
        show_cost_label = tk.Label(output_frame, textvariable=self.cost)
        show_cost_label.grid(row=0, column=1, sticky="E")

        markup_label = tk.Label(output_frame, text="Markup Sell Price:")
        markup_label.grid(row=1, column=0, sticky="W")
        show_markup_price = tk.Label(output_frame,
                                     textvariable=self.sell_price)
        show_markup_price.grid(row=1, column=1, sticky="E")

        # window loop
        root.mainloop()


PriceMarkup()

        
    #     def isNumber(self, num):
    #         try:
    #             float(num)
    #         except ValueError:
    #             return False
    #         return True


    #     def validate_data(price, units, markup):
    #         """Validate entered data"""
    #         pack = [price, units, markup]
    #         for data in pack:
    #             if len(data) == 0:
    #                 tk.messagebox.showwarning(title="Error",
    #                                         message="All fields must be filled")
    #                 return False
    #             if not isNumber(data):
    #                 tk.messagebox.showwarning(title="Error",
    #                                         message="Numbers Only")
    #                 return False
    #             if float(data) <= 0:
    #                 tk.messagebox.showwarning(title="Error",
    #                                         message="No zero or negative values")
    #                 return False
    #         return True


    # def getMarkup(price, units, markup):
    #     """get and show the markup"""
    #     price, units, markup = float(price), float(units), float(markup)
    #     cost = price / units
    #     percent = markup / 100
    #     sell_price = cost * percent + cost
    #     # format sell price and cost
    #     sell_price = "{:.2f}".format(sell_price)
    #     cost = "{:.2f}".format(cost)
    #     message = f"Cost per unit: ${cost}, Sell Price: ${sell_price} with a {markup}% markup"
    #     # tk.messagebox.showinfo(title="Sell Price", message=message)


    # def get_data():
    #     """Get data from GUI"""
    #     purchasePrice = purchase_price_entry.get()
    #     units = units_entry.get()
    #     markupPercent = markup_percent_entry.get()
    #     if validate_data(purchasePrice, units, markupPercent):
    #         getMarkup(purchasePrice, units, markupPercent)

    