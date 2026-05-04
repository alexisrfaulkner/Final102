"""
Defuse the Bomb: Rainforest Binary Toggle Phase
Capybara says HELP: player converts to 4-bit binary
"""

import os
import platform

#Image 
image_path = os.path.join(os.path.dirname(__file__), "rainforest image.png")

if platform.system() == "Darwin":
    os.system(f'open "{image_path}"')
elif platform.system() == "Windows":
    os.startfile(image_path)
else:
    os.system(f'xdg-open "{image_path}"')

#Correct 4-bit Binary 
correct_code = [
    "0100", "1000",
    "0100", "0101",
    "0100", "1100",
    "0101", "0000"
]

#Prompt
print("Rainforest Binary Phase")
print()
print("You are deep in the rainforest.")
print("Your arm burns after touching a strange plant.")
print("A capybara appears and makes a strange sound.")
print()
print('The capybara is trying to say: "HELP"')
print()
print("Look at the image that opened.")
print("Convert HELP into ASCII, then into 4-bit binary.")
print("Enter each 4-bit chunk using the toggles.")
print("Example: 0100")
print()

#Input
player_code = []

for i in range(8):
    while True:
        entry = input(f"Toggle group {i+1} (4 bits): ")
        
        if len(entry) == 4 and all(bit in "01" for bit in entry):
            player_code.append(entry)
            break
        else:
            print("Enter exactly 4 bits (0 or 1). Example: 0101")

print()

#Check
if player_code == correct_code:
    print("Correct!")
    print("The capybara understands your binary signal.")
    print("Rainforest phase defused.")
else:
    print("Incorrect code.")
    print("The rainforest phase is still active.")