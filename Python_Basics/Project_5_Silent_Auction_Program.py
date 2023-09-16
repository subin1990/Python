import os

def Bidder_result (User_data):
    Highest_bid = 0
    Winner = ''
    for i in User_data:
        Bid_price = User_data[i]
        if Bid_price > Highest_bid:
            Highest_bid = Bid_price
            Winner = i
    print(f'\n Auction participants are {User_data}')
    print(f"\n\nThe winner is {Winner} with a bid of Rupees {Highest_bid}/- Thanks for participating the Auction")


print("\n**** Welcome to Silent Auction Program ****\n")

Auction_data = {}
end_of_bidding =False

while not end_of_bidding:
    Name = input("What is your Name: ")
    Amount = int(input("What is your Bid: "))

    Auction_data[Name] = Amount
    User_option = input("Are there any other bidders ? Type 'Yes' or 'No': ")
    if User_option == "No":
        end_of_bidding= True
        Bidder_result(Auction_data)
    elif User_option=='Yes':
        os.system('cls')