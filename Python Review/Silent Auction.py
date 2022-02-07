def calculate_auction():
    highest_bid = 0
    number_of_bids = int(input("Enter a number of bids greater than 0 and less than 101: "))
    for i in range(number_of_bids):
        bid_name = str(input("Enter your name: "))
        bid_amount = int(input("Enter amount that is less than 2000: "))
        if bid_amount >= highest_bid:
            return bid_name

calculate_auction()
