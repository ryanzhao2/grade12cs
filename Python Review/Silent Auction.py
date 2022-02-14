def calculate_auction():
    highest_bid = 0
    highest_bid_name = ''
    number_of_bids = int(input("Enter a number of bids greater than 0 and less than 101: "))
    for i in range(number_of_bids):
        bid_name = input("Enter your name: "))
        bid_amount = int(input("Enter an amount that is less or equal to 2000: "))
        while bid_amount > 2000:
            bid_amount = int(input("Enter an amount that is less or equal to 2000: "))
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bid_name = bid_name
    return highest_bid_name
get_bid = calculate_auction()
print(get_bid)