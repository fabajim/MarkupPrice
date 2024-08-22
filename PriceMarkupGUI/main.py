import tkinter as tk
from tkinter import messagebox


class PriceMarkup:
    def __init__(self):
        root = tk.Tk()
        root.geometry("550x450")
        root.title("Price Markup")

        label = tk.Label(root, text="Find the Markup Price",
                         font=('Arial', 18))
        label.pack()

        frame = tk.Frame(root)
        frame.pack()

        # input variables
        self.purchased_at = tk.StringVar()
        self.units = tk.StringVar()
        self.percent_markup = tk.StringVar()

        # calculated variables
        self.cost = tk.StringVar()
        self.sell_price = tk.StringVar()

        # get product purchase price and unit cost
        product_info_frame = tk.LabelFrame(frame, text="Product Info",
                                           font=('Arial', 14))
        product_info_frame.grid(row=0, column=0, padx=20, pady=10)

        purchase_price_label = tk.Label(product_info_frame,
                                        text="Purchase Price",
                                        font=('Arial', 14))
        purchase_price_label.grid(row=0, column=0)

        units_label = tk.Label(product_info_frame, text="Units or Weight",
                               font=('Arial', 14))
        units_label.grid(row=0, column=1)

        purchase_price_entry = tk.Entry(product_info_frame,
                                        textvariable=self.purchased_at,
                                        font=('Arial', 14))
        purchase_price_entry.grid(row=1, column=0)

        units_entry = tk.Entry(product_info_frame,
                               textvariable=self.units,
                               font=('Arial', 14))
        units_entry.grid(row=1, column=1)

        for widget in product_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # get markup percent
        markup_percent_frame = tk.LabelFrame(frame,
                                             text="Markup Percent",
                                             font=('Arial', 14))
        markup_percent_frame.grid(row=1, column=0, sticky="news",
                                  padx=20, pady=10)

        markup_percent_label = tk.Label(markup_percent_frame,
                                        text="Enter Percent Markup",
                                        font=('Arial', 14))
        markup_percent_label.grid(row=0, column=0)

        markup_percent_entry = tk.Entry(markup_percent_frame,
                                        textvariable=self.percent_markup,
                                        font=('Arial', 14))
        markup_percent_entry.insert(-1, '35')
        markup_percent_entry.grid(row=0, column=1, padx=10, pady=5)

        # submit button
        submit_button = tk.Button(frame, text="Submit",
                                  command=self.getData,
                                  font=('Arial', 14))
        submit_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        # Display output
        output_frame = tk.LabelFrame(frame,
                                     text="Calculated Data",
                                     font=('Arial', 14))
        output_frame.grid(row=4, column=0, sticky="news", padx=10, pady=15)

        cost_label = tk.Label(output_frame,
                              text="Product unit cost: ",
                              font=('Arial', 14))
        cost_label.grid(row=0, column=0, sticky="W")
        show_cost_label = tk.Label(output_frame,
                                   textvariable=self.cost,
                                   font=('Arial', 14))
        show_cost_label.grid(row=0, column=1, sticky="E")

        markup_label = tk.Label(output_frame,
                                text="Markup Sell Price:",
                                font=('Arial', 14))
        markup_label.grid(row=1, column=0, sticky="W")
        show_markup_price = tk.Label(output_frame,
                                     textvariable=self.sell_price,
                                     font=('Arial', 14))
        show_markup_price.grid(row=1, column=1, sticky="E")

        # window loop
        root.mainloop()

    def getData(self):
        price = self.purchased_at.get()
        unit = self.units.get()
        percent = self.percent_markup.get()
        if self.validate_data(price, unit, percent):
            self.set_calculated_data(price, unit, percent)

    def isNumber(self, num):
        try:
            float(num)
        except ValueError:
            return False
        return True

    def validate_data(self, price, units, markup):
        """Validate entered data"""
        pack = [price, units, markup]
        for data in pack:
            if len(data) == 0:
                tk.messagebox.showwarning(title="Error",
                                          message="All fields must be filled")
                return False
            if not self.isNumber(data):
                tk.messagebox.showwarning(title="Error",
                                          message="Numbers Only")
                return False
            if float(data) <= 0:
                tk.messagebox.showwarning(title="Error",
                                          message="No zero or negative values")
                return False
        return True

    def set_calculated_data(self, price, units, markup):
        price, units, markup = float(price), float(units), float(markup)
        cost = price / units
        percent = markup / 100
        sell_price = cost * percent + cost
        cost = "{:.2f}".format(cost)
        sell_price = "{:.2f}".format(sell_price)
        self.cost.set(str(cost))
        self.sell_price.set(str(sell_price))


if __name__ == '__main__':
    PriceMarkup()
