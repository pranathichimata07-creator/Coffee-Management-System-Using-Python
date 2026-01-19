# Coffee Management System Using Python

#Menu items with prices

menu = {
    "Espresso":120,
    "Cappuccino":150,
    "Latte":180,
    "Mocha":200
}

# Stock available for each item 

stock = {
    "Espresso":20,
    "Cappuccino":20,
    "Latte":20,
    "Mocha":20
}

# Total sales for the day

total_sales = 0

#order history
order_history = []

#   Function to display coffee menu

def display_menu():
    print("\n---------COFFEE MENU----------")
    print("-----------------------------------")
    for item in menu:
        print(f"{item}\t${menu[item]}\t{stock[item]}")
    print("-------------------------------------------")


    # Function to take customer order

    def take_sales():
        global total_sales

        display_menu()

        item = input(" Enter coffee name:").title()

        if item not in menu:
            print("Sorry!Item not available.")
            return
        quantity = int(input("Enter quantity:"))

        if quantity<=0:
            print("Invaild quantity")
            return
        if stock[item]<quantity:
            print("Not enough stock available")
            return
        
        #Calculate bill


        bill_amount=menu[item]*quantity


        #Update stock

        stock[item]-=quantity

        #Update sales

        stock_sales+=bill_amount 

        #Save order details

        order_details={
            "Item":item,
            "quantity":quantity,
            "Bill":bill_amount
        }

        order_history.append(order_details)

        print("\nOrder Place Successfully!")
        print("Item:",item)
        print("Quanttity:,quantity")
        print("Total Bill:$.bill_amount")

        #Function to show order history
        def show_order_history():
            print("\n---------------ORDER HISTORY --------------")
            if not order_history:
                print("No orders placed yet")
                return
            
        for i , ordre in enumerate(order_history,start=1):
            print(f"{i}.{ordre['item']}-Qty:{ordre['Quantity']}-Bill:{ordre['Bill']}")

        #Function to save sales report 

        def save_sales_report():
            file = open("sales)report.txt","w")
            file.write("Coffee Management System - Daily Sales Report\n\n")

            for order in order_history:
                file.write(
            f"Item:{ordre['Item']}|Quantity:{ordre["Quantity"]}|Bill:{order["Bill"]}\n")   

                file.write(f"\nTotal Sales:${total_sales}")
                file.close()

                print("Sales report saved successfully")


                #Main program lopp

                while True:
                    print("\n=======COFFEE MANAGEMENT SYSTEM=======")
                    print("1.Display Menu")
                    print("2.Place Order")
                    print("3.View Order History")
                    print("4.View Total Sales")
                    print("5.Save Sales Report")
                    print("6.Exit")

                    choice = input("Enter your choice(1-6):")

                    if choice=="1":
                        display_menu()
                    
                    elif choice=="2":
                        take_sales()

                    elif choice=="3":
                        show_order_history()

                    elif choice=="4":
                        print("\nTotal Sales Today:$",total_sales)

                    elif choice=="5":
                        save_sales_report()

                    elif choice=="6":
                        print("\nThank you for using Coffee Mnagement System")

                        break

                    else:

                        print("Invaild choice ! Please try again.")        


                    

                        
            
     

                
                
            

        
        


   
            
                  
                

        
        


        
        

             



    
    
        
          