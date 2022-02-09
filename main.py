from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

#print the ascii art for the program
#print(logo)

participants = {}
more_participants = True

while more_participants == True:
    name = input("Please enter your name: ").lower()
    bid_price = int(input("Please enter a bid proce: "))

    def add_participant(p_name, bid):
        participants[p_name] = bid

    add_participant(p_name = name, bid = bid_price)

    keep_going = input("Are there more participants who would like to bid? Enter (yes or no): ").lower()

    if keep_going == 'no':
        more_participants = False

    clear()

temp = 0
winner = "name"

for person, bid in participants.items():
    if bid > temp:
        temp = bid
        winner = person


print(winner)
print(participants)

