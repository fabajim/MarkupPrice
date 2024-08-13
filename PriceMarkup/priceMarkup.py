import sys
from datetime import datetime


class Get_Markup:

    def __init__(self):
        # List to contain comments and date/time of entry
        self.comments = []

        # load comments from txt file and append to comments[]
        with open('PriceMarkup/COMMENTS.txt', 'a+') as filehandle:
            for line in filehandle:
                # keeps from '\n' added to list
                currentComment = line[:-1]
                self.comments.append(currentComment)

    def the_markup(self):
        """User inputs cost price and units
        User inputs the mark up percentage"""
        try:
            cost = float(input("\nEnter item's cost: "))
            units = float(input("Enter items units or total weight:  "))
            markUp = float(input("Enter markup percent: %"))
            # check if inputs are valid
            if cost >= 0 and units > 0 and markUp >= 0: 
                # set sell price with the marked up amount
                sell_price = (cost/units) * (markUp/100)
                sell_price = sell_price + (cost/units)
                # formats unit cost and sell price to two decimal places
                formatted_cost = "{:.2f}".format(cost/units)
                formatted_price = "{:.2f}".format(sell_price)
                print("\n**********************************************"
                      "\n* Cost per unit: $", formatted_cost, ""
                      "\n* Sell price with a", markUp, "% Markup: $", ""
                      "", formatted_price, ""
                      "\n**********************************************")
            else:
                # invalid entry clause
                print("\n**********Invalid Entry********\n"
                      "*The cost cannot be negative\n"
                      "*Units must be greater than 0\n"
                      "*Percent cannot be negative\n"
                      "**********************************\n")
        # control to only accept float inputs
        except ValueError:
            print("\n***Numbers Only!***"
                  "\n*******************")

    def makeComment(self):
        """User can leave a note"""
        add_note = input("\nEnter a message:\n")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # add note to comments[] with a time stamp
        self.comments.append(dt_string)
        self.comments.append(add_note)
        self.save_comments()

    def print_comments(self):
        for i in self.comments:
            print(i)
        delete = input("\nClear Comments? y/n ")
        if delete == 'y' or delete == 'Y':
            self.clear_comments()

    def clear_comments(self):
        """Admin User can delete comments"""
        n = len(self.comments) + 1
        del self.comments[1:n]
        self.save_comments()

    def save_comments(self):
        with open('PriceMarkup/COMMENTS.txt', 'w') as filehandle:
            for listitem in self.comments:
                filehandle.write('%s\n' % listitem)


if __name__ == '__main__':
    markup_val = Get_Markup()
    print("*******Get Markup Price*******\n")
    menu = ""
    # menu used a loop control, 4 exits
    while menu != '3':
        menu = input("\n*           MENU             *"
                     "\n******************************"
                     "\n* 1 To get price markup      *"
                     "\n* 2 To leave a message       *"
                     "\n* 3 To Exit                  *"
                     "\n******************************"
                     "\n\nSelect and enter a number: ")        
        # 1 calls the mark up function
        if menu == '1':
            continueLoop = True
            while continueLoop:
                markup_val.the_markup()

                # exit out of mark up loop with n or N
                runAgain = input("\nContinue? y/n ")
                if runAgain == 'n' or runAgain == 'N':
                    continueLoop = False
        elif menu == '2':
            markup_val.makeComment()
        elif menu == 'view notes':
            markup_val.print_comments()
        else:
            # invalid entry clause
            if menu != '3':
                print("\nInvalid Entry\n")
    # Clears comments[]
    markup_val.comments.clear()
    # end of program
    sys.exit()
