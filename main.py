from art import logo
import os

# print the ascii art for the program

participants = {}
more_participants = True

while more_participants:
    print(logo)
    name = input("Please enter your name: ").lower()
    bid_price = int(input("Please enter a bid proce: "))

    def add_participant(p_name, bid):
        """
        first docstring practice: this can be used to add documentation to functions.
        this function takes a name and a bid as parameters and adds that information
        to the participants{}
        """
        participants[p_name] = bid

    add_participant(p_name=name, bid=bid_price)

    keep_going = input("Are there more participants who would like to bid? Enter (yes or no): ").lower()

    if keep_going == 'no':
        more_participants = False

    os.system("clear")

temp = 0
winner = "name"
for person, bid in participants.items():
    if bid > temp:
        temp = bid
        winner = person

print(logo)
print(f"The winner is: {winner}")

