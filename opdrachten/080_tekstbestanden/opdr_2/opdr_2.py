import random
def checkCorrectNumber(number, list):
    if(number<1 or number >42 or number in list):
        print("Fout nummer. Geef een nummer tussen 1 en 42")
        return False
    else:
        return True
userNumbers = []
computerNumbers = []
#get the usernumbers
x = 1
while(x <= 6):
    try:
        number = int(input("Geef lotto nummer " + str(x) + ": " ))
        while(not checkCorrectNumber(number, userNumbers)):
            number = int(input("Geef lotto nummer " + str(x) + ": " ))        
        userNumbers.append(number)
        x += 1
    except ValueError:
        print("vul een geldige waarde in")
        
#get the random numbers
for x in range(1,7):
    number = random.randint(1,10)
    while(not checkCorrectNumber(number, computerNumbers)):
        number = random.randint(1,10)
    computerNumbers.append(number)
#sort the numbers
userNumbers.sort(key=int)
computerNumbers.sort(key=int)
#show the numbers
print("Je gekozen nummers zijn: " + ', '.join(map(str, userNumbers)))
print("De trekking cijfers zijn: " + ', '.join(map(str, computerNumbers)))
#create sets
user_set = set(userNumbers)
computer_set = set(computerNumbers)
common_numbers = user_set.intersection(computer_set)
matches = len(common_numbers)
#check price
prize_messages = {
    3: "3 juiste cijfers, Gefeliciteerd je wint 10 euro",
    4: "4 juiste cijfers, Gefeliciteerd je wint 1000 euro",
    5: "5 juist cijfers, Gefeliciteerd je wint 100.000 euro",
    6: "6 juiste cijfers, Gefeliciteerd je wint 10.000.000 euro",
}
print(prize_messages.get(matches, "Helaas geen prijs gewonnen"))
'''
if matches==3:
    print("3 juiste cijfers, Je wint 10 euro")
elif matches==4:
    print("4 juiste cijfers, je wint 1000 euro")
elif(matches==5):
    print("5 juist cijfers, je wint 100.000 euro")
elif (matches==6):
    print("6 juiste cijfers, je wint 10.000.000 euro")
else:
    print("Helaas geen prijs gewonnen")
'''