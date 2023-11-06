import pyautogui

# Move the mouse to the coordinates (100, 200) and click
pyautogui.moveTo(1000, 500)
pyautogui.click()

# Type out the string "Hello, world!"
pyautogui.typewrite("""
# Initialize a dictionary to store the votes for each meal
votes = {}

# Ask each friend to cast their vote
while True:
    # Ask the user to enter their name and vote
    name = input("Enter your name: ")
    vote = input("Enter your preferred meal: ")

    # Add the vote to the dictionary
    if vote in votes:
        votes[vote] += 1
    else:
        votes[vote] = 1

    # Ask the user if they want to continue casting votes
    more_votes = input("Do you want to continue casting votes (yes/no)? ")
    if more_votes.lower() != "yes":
        break

# Determine the meal with the most votes
most_votes = 0
final_meal = ""
for meal, num_votes in votes.items():
    if num_votes > most_votes:
        most_votes = num_votes
        final_meal = meal

# Check if more than 50% of the friends agreed on the same meal
if most_votes > len(votes) / 2:
    print("The final meal for the picnic is:", final_meal)
else:
    print("There was no consensus among the friends. No meal will be prepared.")


""")

