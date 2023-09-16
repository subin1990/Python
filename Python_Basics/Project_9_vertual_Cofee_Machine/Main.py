import Menu
#import Balance_Cash_checker
import math
NOTES50=[5]
NOTES20=[5]
NOTES10=[5]
COFFEEPOWDER =[1000]
MILK= [1000]
WATER= [1000]
SUGAR= [200]
FLAVOURS =[200]

# Functions
# Balance Cash checker
def Cash_Checker(Customer_note10,Customer_note20,Customer_note50,Balance ):
    global Note_50_Stock
    global Note_20_Stock
    global Note_10_Stock
    Note_50_Stock = sum(NOTES50)
    Note_20_Stock = sum(NOTES20) # 80
    Note_10_Stock = sum(NOTES10) # 100
    Balance_to_Customer= Balance
    Note_50_Stock= Note_50_Stock+Customer_note50 # 0
    Note_20_Stock= Note_20_Stock+Customer_note20 # 5
    Note_10_Stock= Note_10_Stock+Customer_note10 # 14

    if Balance >= 50: # checking Balance amount if greater than 50 if Yes
        Count50 = math.floor(Balance/50) # Finding how many 50 notes in Balance
        if Count50<=Note_50_Stock: # checking 50 notes are available in Stock if yes
            Balance= Balance-(Count50*50) # Calculating Balance amount
            Note_50_Stock= Note_50_Stock-Count50 # deducting 50 notes in Stock

    if Balance >= 20:
        Count20 = math.floor(Balance/20)
        if Count20<=Note_20_Stock:
            Balance= Balance-(Count20*20)
            Note_20_Stock= Note_20_Stock- Count20
    if Balance >= 10:
        Count10 = math.floor(Balance/10)
        if Count10<=Note_10_Stock:
            Balance= Balance-(Count10*10)
            Note_10_Stock= Note_10_Stock-Count10

    #print(Note_50_Stock ,Note_20_Stock ,Note_10_Stock)
    #print(Balance)

    if Balance> 0:
        print(f"Balance Notes are not available. Here is your paid Amount Rs. 0000 and try again ")
        Note_50_Stock = Note_50_Stock - Customer_note50
        Note_20_Stock = Note_20_Stock - Customer_note20
        Note_10_Stock = Note_10_Stock - Customer_note10
        #print(f"Cash in Hand 50 notes: {Note_50_Stock},20 notes: {Note_20_Stock},10 notes: {Note_10_Stock} ")
        UserBalance_Fail = input("Press 1 for try again or any key to exit")
        if UserBalance_Fail == '1':
            Vertual_Cofee_Machine()
        else:
            exit("Exiting....")
    elif Balance==0:
        print(f"Payment Successful Your Balance is {Balance_to_Customer} Please collect it")
        #print(f"Cash in Hand 50 notes: {Note_50_Stock},20 notes: {Note_20_Stock},10 notes: {Note_10_Stock} ")
    return Note_10_Stock,Note_20_Stock,Note_50_Stock

# Function for collecting Payment from Customer
def Collecting_Payment():
    print("We accept only 10, 20 and 50 notes only\n")
    global Customer_note10
    global Customer_note20
    global Customer_note50
    Customer_note10 = int(input("Number of 10 Notes: "))
    Customer_note20 = int(input("Number of 20 Notes: "))
    Customer_note50 = int(input("Number of 50 Notes: "))
    #Note_100 = int(input("Number of 100 Notes: "))
    global User_Total_Amount
    User_Total_Amount = (Customer_note10*10+Customer_note20*20+Customer_note50*50)
    return User_Total_Amount, Customer_note10,Customer_note20,Customer_note50

def Final_Option():
    print("Here is your delicious coffee Thanks for using ")
    userchoice_continue = input("Press 1 for order more or press any key to off the machine").upper()
    if userchoice_continue=='1':
        Vertual_Cofee_Machine()
    elif userchoice_continue=='REPORTS':
        print("Cash reports")
        print(f'Total cash available:  {sum(NOTES10)*10+sum(NOTES20)*20+sum(NOTES50)*50}')
        print(f'Items left : Coffee Powder = {sum(COFFEEPOWDER)} Milk= {sum(MILK)} Water = {sum(WATER)} Sugar = {sum(SUGAR)} Flavours= {sum(FLAVOURS)}')
    else:
        exit('Machine turnoff-----')

        # Raw materials required
def Materials_Check(Latee, Expresso,Cappuccino):

    Coffee_powder_stock = sum(COFFEEPOWDER)
    Milk_stock = sum(MILK)
    Water_stock = sum(WATER)
    Sugar_stock = sum(SUGAR)
    Flavours_stock = sum(FLAVOURS)
    global CofeePowder_required
    global Milk_required
    global Water_required
    global Sugar_required
    global Flavours_required
    CofeePowder_required = Latee * Menu.Menu[0]['Coffee Powder'] + Expresso * Menu.Menu[1][
        'Coffee Powder'] + Cappuccino * Menu.Menu[2]['Coffee Powder']
    Milk_required = Latee * Menu.Menu[0]['Milk'] + Expresso * Menu.Menu[1]['Milk'] + Cappuccino * Menu.Menu[2][
        'Milk']
    Water_required = Latee * Menu.Menu[0]['Water'] + Expresso * Menu.Menu[1]['Water'] + Cappuccino * Menu.Menu[2][
        'Water']
    Sugar_required = Latee * Menu.Menu[0]['Sugar'] + Expresso * Menu.Menu[1]['Sugar'] + Cappuccino * Menu.Menu[2][
        'Sugar']
    Flavours_required = Latee * Menu.Menu[0]['Flavours'] + Expresso * Menu.Menu[1]['Flavours'] + Cappuccino * \
                        Menu.Menu[2]['Flavours']
    if Coffee_powder_stock > CofeePowder_required and Milk_stock > Milk_required and Water_stock > Water_required and Sugar_stock > Sugar_required and Flavours_stock > Flavours_required:
        print("Proceed")
        #return Coffee_powder_stock, Milk_stock, Milk_stock, Water_stock, Sugar_stock, Flavours_stock
    else:
        exit('Resources are out of Stock')

def Stock_deduction(CofeePowder_required,Milk_required,Water_required,Sugar_required,Flavours_required):
    COFFEEPOWDER[0]= COFFEEPOWDER[0]-CofeePowder_required
    MILK[0]= MILK[0]-Milk_required
    WATER[0]=WATER[0]-Water_required
    SUGAR[0]= SUGAR[0]-Sugar_required
    FLAVOURS[0]= FLAVOURS[0]-Flavours_required
    #print(f'Coffee Powder = {sum(COFFEEPOWDER)} Milk= {sum(MILK)} Water = {sum(WATER)} Sugar = {sum(SUGAR)} Flavours= {sum(FLAVOURS)}')


# Program starting

def Vertual_Cofee_Machine():
    print("Welcome to Karakootil Vertual Coffee Machine\n\n")

    print("Here is the Menu Item Name and Price\n")

    for i in range(3):
        print(f"{i+1} {Menu.Menu[i]['Name']}   {Menu.Menu[i]['Price']}")

    Quanity_Check= True
    while Quanity_Check:
        print("\n Enter Your Choice: Maximum 3 quantities are allowed per user")

        Latee = int(input("Latte: "))
        Expresso = int(input("Expresso: "))
        Cappuccino = int(input("Cappuccino: "))
        Total_Qty= Latee+Expresso+Cappuccino
        Price = (Latee * Menu.Menu[0]['Price'] + Expresso * Menu.Menu[1]['Price'] + Cappuccino * Menu.Menu[2]['Price'])


        if Total_Qty<=3:
                Materials_Check(Latee,Expresso,Cappuccino)
                print(f"Total Qauntity is {Total_Qty} and Price is {Price}")
                Quanity_Check= False
        else:
                print("Quanity Should be less than or equal to three")
                Quanity_Check= True
    Payment_Status = False
    while Payment_Status==False:
        #print( f'Payment received Rs. ')
        Collecting_Payment()
        Balance = User_Total_Amount-Price
        if Price >User_Total_Amount:
            Payment_Second_Chance =input('Payment Failed Not Enough Balance Press 1 to Pay again Press any key to exit')
            if Payment_Second_Chance=='1':
                Payment_Status= False
            else:
                exit('Exiting the application')
        elif Price< User_Total_Amount:
            Cash_Checker(Customer_note10, Customer_note20, Customer_note50, Balance)
            NOTES10[0]=Note_10_Stock
            NOTES20[0] = Note_20_Stock
            NOTES50[0] = Note_50_Stock
            Stock_deduction(CofeePowder_required,Milk_required,Water_required,Sugar_required,Flavours_required)
            #print(f"Cash in hand {Note_10_Stock}")
            Final_Option()
            Payment_Status=True
        elif Price == User_Total_Amount:
            print("Payment Successful")
            NOTES10[0]= NOTES10[0]+Customer_note10
            NOTES20[0]= NOTES20[0]+Customer_note20
            NOTES50[0] = NOTES50[0] + Customer_note50
            Stock_deduction(CofeePowder_required,Milk_required,Water_required,Sugar_required,Flavours_required)
            Payment_Status= True
            Final_Option()

Vertual_Cofee_Machine()

