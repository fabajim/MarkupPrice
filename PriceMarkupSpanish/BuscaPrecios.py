import sys
from datetime import datetime


class Busca_Precios:

    def __init__(self):
        # List to contain comments and date/time of entry
        self.comments = []

        # load comments from txt file and append to comments[]
        with open('PriceMarkupSpanish/COMMENTS.txt', 'a+') as filehandle:
            for line in filehandle:
                # keeps from '\n' added to list
                currentComment = line[:-1]
                self.comments.append(currentComment)

    def the_markup(self):
        """User inputs cost price and units
        User inputs the mark up percentage"""
        try:
            cost = float(input("\nIngresar El Costo: "))
            units = float(input("Ingresar Los Unidades o el Peso:  "))
            markUp = float(input("Ingresar El Porcentaje de Aumento: "))

            # check if inputs are valid
            if cost >= 0 and units > 0 and markUp >= 0: 
                # set sell price with the marked up amount
                sell_price = (cost/units) * (markUp/100)
                sell_price = sell_price + (cost/units)

                # formats unit cost and sell price to two decimal places
                formatted_cost = "{:.2f}".format(cost/units)
                formatted_price = "{:.2f}".format(sell_price)
                print("\n**************************************************"
                      "\n* El Costo por unidad: $" , formatted_cost ,"                   *"
                      "\n* El precio con el aumento de %" , markUp , " es: $",formatted_price, "*"
                      "\n**************************************************")
            else:
                # invalid entry clause
                print("\n**********Entrada Invalida************\n"
                      "*El Costo no puede ser negativo      *\n"
                      "*Los Unidades no puede ser 0 o menos *\n"
                      "*El porcentaje no puede ser negaitvo *\n"
                      "**************************************\n")  
        # control to only accept float inputs
        except ValueError:
            print("\n***Solo usa numeros***"
                  "\n**********************")

    def makeComment(self):
        """User can leave a note"""
        add_note = input("\nIngrese un mensaje:\n")
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
        with open('PriceMarkupSpanish/COMMENTS.txt', 'w') as filehandle:
            for listitem in self.comments:
                filehandle.write('%s\n' % listitem)

    def print_groups(self):
        # Displays linked group numbers
        print("\n**********************"
              "\n* 1 - Produce        *"
              "\n* 2 - Grocery        *"
              "\n* 3 - Taxed Grocery  *"
              "\n* 4 - Carne          *"
              "\n* 5 - Lecheria       *"
              "\n* 6 - Panaderia      *"
              "\n* 7 - Refrescos      *"
              "\n* 8 - Licor          *"
              "\n* 9 - Cerveza/Vino   *"
              "\n* 11 - Health/Beauty *"
              "\n**********************\n")


if __name__ == '__main__':
    precio = Busca_Precios()
    print("*******BUSCAR EL PRECIO*******\n")
    menu = ""
    # menu used a loop control, 4 exits
    while menu != '4':
        menu = input("\n*           MENU             *"
                     "\n******************************"
                     "\n* 1 Para sacar un precio    *"
                     "\n* 2 Para dejar un mensaje    *"
                     "\n* 3 Para mostrar los codigos *"
                     "\n* 4 Para salir               *"
                     "\n******************************"
                     "\n\nIngresa un numero: ")        
        # 1 calls the mark up function
        if menu == '1':
            while True:
                precio.the_markup()

                # exit out of mark up loop with n or N
                runAgain = input("\nContinuar? s/n ")
                if runAgain == 'n' or runAgain == 'N':
                    break
        elif menu == '2':
            precio.makeComment()
        elif menu == '3':
            precio.print_groups()
        elif menu == 'view notes':
            precio.print_comments()
        else:
            # invalid entry clause
            if menu != '4':
                print("\nENTRADA INVALIDA\n")
    # Clears comments[]
    precio.comments.clear()
    # end of program
    sys.exit()
