playerName = input("STATE YOUR NAME: ")
print ("")
print ("==============================================")
print ("")
print ("<<<<<<<<<<<<<<<<< Adventure of", playerName, ">>>>>>>>>>>>>>>>>>>>>")
print ("")
print ("Welcome to the Adventure of ", playerName, "!")
print ("")
print ("Are you a Male / Female? [M/F]")
gender = input(">>")

if gender == "M":
    print
else:
    if gender == "F":
        print
    else:
        print ("Please choose betweeen M or F")
            

print ("One day, a young adventurer named", playerName)
print ("Spawned in a peacefull Village of Orion")
print (playerName, "walked out of Village and see a slime jumping around.")
print ("")
print ("picked up a... (Sword/Bow)")

weapon = input ("")
if weapon == "Sword":
    print ("and attack the slime.")
    print ("the slime get sliced and died. adventurer gain a level")
else:
    if weapon == "Bow":
        print ("and shot the slime.")
        print ("the slime get shotted and died. adventurer gain a level")
    else:
        print ("Please choose between Sword or Bow")

print ("")

print (playerName, "The Adventurer, then run towards a chest that glows from the inside")
print ("PICK ONE!") 
print ("(Open/Walk)")
chest = input ("")
if chest == "Open":
    print ("The Adventurer Finds a Gold and brings it Home to the Village.")
else:
    if chest == "Walk":
        print ("The Adventurer walk pass the chest to the Village")
    else:
        print ("Please choose between Open or Walk")
print("")
print("as the advenure walks, he startd to feel more and more tired.")
print("take a [Taxi] / Keep [Walk]ing")
walkTaxi = input("")
if walkTaxi == "Taxi":
    print ("The Adventurer choose to walk.")
else:
    if walkTaxi == "Walk":
        print ("The Adventurer choose to take a taxi")
    else:
        print ("Please choose between Taxi or Walk")

print (playerName, "Arrivevd at the village and see RTX 3090 TI on sale")
print ("With the price of 1 gold")
print ("[Buy/Pass]")
rtx = input("")
if rtx == "Buy":
    print ("Congratulation you got RTX 3090 TI!")
else:
    if rtx == "Pass":
        print ("Sad, you dont get that RTX 3090 TI")
    else:
        print ("Choose between Buy/Pass")
