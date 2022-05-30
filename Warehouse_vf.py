##TODO:
#add license statement

##Questions:
#get number of stock of a certain type and search if a stock is available are very similar functionalities
#What is meant by "Provide input parameters and its functionality."?
#Can we choose an arbitrary set of values for the three items in our warehouse? What to do if no input is provided?

#Define Stock Class
class Stock:
    def __init__(self, type: str, quantity: int = 0, price: float = 0) -> None:
        #Defining Characteristics for each product in the stock
        self.type = type
        self.quantity = quantity
        self.price = price

    def add_stock(self, new_stock: int = 0) -> None:
        #add stock of specific type
        self.new_stock = new_stock
        self.quantity = self.quantity + self.new_stock 
        
    def remove_stock(self, removed_stock: int = 0) -> None:
        #remove stock of specific type
        self.removed_stock = removed_stock
        self.quantity = self.quantity - self.removed_stock 

#Create class Whisky
class Whisky(Stock):
    def __init__(self, type: str, quantity = 0, price = 0) -> None:
        super().__init__(type, quantity, price) #calling the parent's init method

#Create class Gin
class Gin(Stock):
    def __init__(self, type: str, quantity: int = 0, price = 0) -> None:
        super().__init__(type, quantity, price) #calling the parent's init method

#Create class Vodka
class Vodka(Stock):
    def __init__(self, type: str, quantity: int = 0, price: float = 0) -> None:
        super().__init__(type, quantity, price) #calling the parent's init method



#create class Warehouse
class Warehouse(Stock):
    def __init__(self) -> None:
        #Define inital parameters for the three types of stock. Define (name, quantity available, price)
        self.whisky = Whisky("Whisky", 500, 20) 
        self.gin = Gin("Gin", 2000, 50)
        self.vodka = Vodka("Vodka", 0, 15)

    def get_stock_report(self) -> dict:
        #return dictionary with the availble stock for all three classes
        report = {self.whisky.type: self.whisky.quantity,
                self.gin.type: self.gin.quantity,
                self.vodka.type: self.vodka.quantity}
        return report


    def get_stock(self) -> str:
        #get available quantity for specific stock choice. Let the user choose which type of stock they'd like to investigate.
        
        input_correct = False
        while input_correct == False:
            #validate that the user has entered an integer value. Loop keeps running until valid number is entered.
            try:
                product_type = int(input("What product are you interested in? (1: Whisky, 2: Gin, 3: Vodka)\n"))
                input_correct = True
            except:
                print("Please make sure to enter and integer between 1 and 3 for your product selection!\n")

        #Returns the available stock for the user input. If integer outside of 1-3 was entered, print explanation and function breaks.
        if product_type == 1:
            print(f"I have {self.whisky.quantity} bottles of Whisky in my Warehouse!")
        elif product_type == 2:
            print(f"I have {self.gin.quantity} bottles of Gin in my Warehouse!\n")
        elif product_type == 3:
            print(f"I have {self.vodka.quantity} bottles of Vodka in my Warehouse!\n")
        else:
            print("Sorry, I think you entered a wrong stock number!\n")

    def is_available(self) -> bool:
        #Check if specific stock is available in the warehouse
        input_correct = False
        while input_correct == False:
            #validate that the user has entered an integer value. Loop keeps running until valid number is entered.
            try:
                product_type = int(input("For which liquor would you like to check the availabilty? (1: Whisky, 2: Gin, 3: Vodka)\n"))
                input_correct = True
            except:
                print("Please make sure to enter and integer between 1 and 3 for your product selection!\n")
        #Returns the available stock for the user input. If integer outside of 1-3 was entered, print explanation and function breaks.
        #Returns True if stock is available and False is stock is not available.
        if product_type == 1 and self.whisky.quantity > 0:
            print(f"Great Success! I have {self.whisky.quantity} bottles of Whisky available!\n")
            return True
        elif product_type == 2 and self.gin.quantity > 0:
            print(f"Great Success! I have {self.gin.quantity} bottles of Gin available!\n")
            return True
        elif product_type == 3 and self.vodka.quantity > 0:
            print(f"Great Success! I have {self.vodka.quantity} bottles of Vodka available!\n")
            return True
        else:
            print(f"Sorry, I don't have any items of that type available!\n")
            return False



if __name__ == "__main__":
    warehouse = Warehouse()
    warehouse.whisky.remove_stock(50)
    warehouse.gin.add_stock(200)
    print(warehouse.get_stock_report())
    warehouse.get_stock()
    warehouse.is_available()

