import random

print("--- BR Randomizer ---")
print("")
user1 = int(input("Enter the number from which the random will start: "))
user2 = int(input("Enter the number before which the random will end: "))

random = random.randint(user1, user2)
print("")
print("Number fell out: ",random)
