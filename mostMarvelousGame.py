#Liam Gleeson and Aaron Tschumper
#Project: The Most Marvelous Game
#CSCI 141
#import random
import random

#give a brief backstory

print('Your castle is in ruins. Amidst your daily noble proceedings at the royal castle,')
print('you heard an ear piercing shriek coming from the sky. A dragon emerged from')
print('the clouds and engulfed the castle in flames. During the mighty fight against')
print('the dragon, it swooped in and kidnapped the princess!')
print('')
print("With the princess missing you head out on a quest to slay the dragon")
print('')
print("Along your treacherous and endearing travels you come across a tavern.")
print("You make your way up to the bar", end = " ")
#Prompt user for their name
userName = input('and the barkeeper asks, "What is your name?" ')
print("")
print('"Ahh', userName, 'its always a pleasure to meet royalty"')
print("After further discussion you ask the barkeep if he has any information")
print("on the location of the dragon. He says that the dragon just recently")
print("flew over heading north and points out the trail that is best to take.")
print("")
print("He warns that it is a treacherous journey and offers you to take a magical")
print("weapon set from his chest. The chest contains a sword and shield(1), and")
print("a set of daggers and throwing knives(2).")
userWeapon = int(input("Which do you choose? 1 or 2 "))
print("")
if userWeapon == 1:
    print('"You chose the sword and shield, strong and sturdy. Good choice."')
if userWeapon == 2:
    print('"Ahh the daggers and knives, sharp and deadly. Good choice."')
#Set user health to max to userHealth =  10 
#Give a brief description of where you are and your task at hand. You are given a key and see two chest in front of you, knowing you can only open one. Items are random so each time the weapon is in a different chest.
def userAttackGoblin(gHealth):
    if userWeapon == 1:
        userAtkChoice = int(input("Would you like to use attack 1 or attack 2? "))
        if userAtkChoice == 1:
            swordDamage = random.randint(3,5)
            gHealth = int(gHealth)
            goblinHealth = gHealth - swordDamage 
            print("You viciously swing your sword at the fowl creature and hit it for", swordDamage, "damage.")
            print("The goblin has", goblinHealth, "health remaining.")
            print("")
            return goblinHealth
        if userAtkChoice == 2:
            shieldDamage = random.randint(2,4)
            gHealth = int(gHealth)
            goblinHealth = gHealth - shieldDamage
            print("You charge at the goblin and bludgeon it with your shield for", shieldDamage, "damage.")
            print("The goblin has", goblinHealth, "health remaining.")
            print("")
            return goblinHealth
    if userWeapon == 2:
        userAtkChoice = int(input("Would you like to use attack 1 or attack 2? "))
        if userAtkChoice == 1:
            daggerDamage = random.randint(3,4)
            gHealth = int(gHealth)
            goblinHealth = gHealth - daggerDamage 
            print("You swiftly stride up to the goblin and stab it with your daggers for", daggerDamage, "damage.")
            print("The goblin has", goblinHealth, "health remaining.")
            print("")
            return goblinHealth
        if userAtkChoice == 2:
            knifeDamageOne = random.randint(1,2)
            knifeDamageTwo = random.randint(1,2)
            knifeDamageThree = random.randint(1,2)
            knifeDamageTotal = knifeDamageOne + knifeDamageTwo + knifeDamageThree
            gHealth = int(gHealth)
            goblinHealth = gHealth - knifeDamageTotal
            print("You throw your knives at the beast with pinpoint accuracy for", knifeDamageTotal, "damage.")
            print("The goblin has", goblinHealth, "health remaining.")
            print("")
            return goblinHealth
#Two weapons, each in a separate chest:
#Sword and shield 
#Dual daggers
#User continues journey and comes across their first monster, a goblin.
#User gets prompted to see what they want to do:
#Attack the goblin- has two different abilities with weapon.
#Set up two different moves for each weapon given to them from the chest.
#Or flee from goblin.
#If attack
#Goblin attacks back
def goblinAttack(uHealth):
    goblinAttackChoice = random.randint(1,2)
    if goblinAttackChoice == 1:
        gAttackValue = random.randint(1,2)
        userHealth = uHealth - gAttackValue
        print("The goblin swipes at your chest and you take",gAttackValue,"damage.")
        print('Your health is now at',userHealth)
        print("")
        return userHealth
        if userHealth == 0:
            userDeath()
    if goblinAttackChoice == 2:
        gAttackValue = random.randint(1,3)
        userHealth = uHealth - gAttackValue
        print("The goblin smashes its club against your head and you take",gAttackValue,"damage.")
        print('Your health is now at',userHealth)
        print("")
        return userHealth
        if userHealth == 0:
            userDeath()
            
def crossRoad(wepChoice):
    print("You come across a crossroad, which two pathways to choose from,")
    print("An old wooden bridge and a rope swing across a gorge (with aligators underneath).")
    crossRoadChoice = int(input("What path would you like to take: The bridge(1) or the rope swing(2) "))
    print("")
    if wepChoice == 1:
        if crossRoadChoice == 1:
            print("You start walking over the bridge and hear creaking from underneath. You make haste")
            print("over the bridge and successfully make it to the other side.")
            print("")
            return True
        if crossRoadChoice == 2:
            print("You get a hold of the rope swing and leap over the gorge, but due to your sword and shields weight, the")
            print("rope swing snaps from above, cauing you to plummet to your death.")
            print("")
            return False
    if wepChoice == 2:
        if crossRoadChoice == 1:
            print("You walk over the old wooden bridge and notice one of your knives is slipping off you. You try to grab it")
            print("but end up falling over the bridge with them, causing you to fall to death like the dunce you are. ")
            print("")
            return False
        if crossRoadChoice == 2:
            print("You get a hold of the rope swing and take a leap off. Due to the lightness of your weapons")
            print("you make it across the gorge successfully and continue onward with your journey.")
            print("")
            return True
        
def userAttackDragon(dHealth):
    dragonHealth = dHealth
    if userWeapon == 1:
        userAtkChoice = int(input("Would you like to use attack 1 or attack 2? "))
        if userAtkChoice == 1:
            swordDamage = random.randint(3,5)
            dragonHealth = dHealth - swordDamage 
            print("You heroically leap on your opposition and hack at the behemoth for", swordDamage, "damage.")
            print("The dragon has", dragonHealth, "health remaining.")
            return dragonHealth
        if userAtkChoice == 2:
            shieldDamage = random.randint(2,4)
            dragonHealth = dHealth - shieldDamage
            print("You tuck behind your shield and charge the dragon, slamming it for", shieldDamage, "damage.")
            print("The dragon has", dragonHealth, "health remaining.")
            return dragonHealth
    if userWeapon == 2:
        userAtkChoice = int(input("Would you like to use attack 1 or attack 2? "))
        if userAtkChoice == 1:
            daggerDamage = random.randint(3,4)
            dragonHealth = dHealth - daggerDamage 
            print("You leap and latch on to the dragon, plunging your daggers in its flank doing", daggerDamage, "damage.")
            print("The dragon has", dragonHealth, "health remaining.")
            return dragonHealth
        if userAtkChoice == 2:
            knifeDamageOne = random.randint(1,2)
            knifeDamageTwo = random.randint(1,2)
            knifeDamageThree = random.randint(1,2)
            knifeDamageTotal = knifeDamageOne + knifeDamageTwo + knifeDamageThree
            dragonHealth = dHealth - knifeDamageTotal
            print("You hurl your knives into the dragon's mouth as it opens to unleash fire dealing", knifeDamageTotal, "damage.")
            print("The dragon has", dragonHealth, "health remaining.")
            return dragonHealth
            
def dragonAttack(uHealth):
    userHealth = uHealth
    dragonAttackChoice = random.randint(1,3)
    if dragonAttackChoice == 1:
        if userHealth == 0:
            userDeath()
        if userWeapon == 1:
            print("The dragon opens its mouth and breathes fire at you, but since you have a shield you block it, causing zero damage to occur")
            print("")
            return userHealth
        if userWeapon == 2:
            dAttackValue = random.randint(3,4)
            userHealth = uHealth - dAttackValue
            print("The dragon opens its mouth and breathes fire at you, causing you to take",dAttackValue,"damage.")
            print('Your health is now at',userHealth)
            print("")
            return userHealth
    if dragonAttackChoice == 2:
        if userHealth == 0:
            userDeath()
        if userWeapon == 1:
            dAttackValue = random.randint(3,4)
            userHealth = uHealth - dAttackValue
            print("The dragon swings its tail against you and try to dodge it, but since you have a sword and shield you can't avoid it in time and")
            print("you take", dAttackValue, "damage")
            print("Your health is now at", userHealth)
            print("")
            return userHealth
        if userWeapon == 2:
            print("The dragon swings its tail against you and try to dodge it, and since you have daggers you drop to the ground, avoiding the hit")
            print("and causing zero damage to occur")
            print("")
            return userHealth
    if dragonAttackChoice == 3:
        dAttackValue = random.randint(1,3)
        userHealth = uHealth - dAttackValue
        if userHealth == 0:
            userDeath()
        if userWeapon == 1 or userWeapon == 2:
            print("The dragon scratches you with its claws and causes you to take",dAttackValue,"damage.")
            print('Your health is now at',userHealth)
            print("")
            return userHealth
            
#With one of two attacks randomly selected
#User continues onward on their journey until discovering a crossroad. 
#Robert frost appears and quotes The Road not Taken
#Robert shows a old wooden bridge and a rope swing across a gorge
#-Set up two different paths, a bridge and a rope swing, and make the two weapons interfere with the outcomes. 
#	- if wrong outcome occurs. Game Over
#	Else: 
#After successfully crossing the gorge, user encounter a dragon guarding the princess and you must defeat him to save the day!
#Prompt user to decide what move they want to do first
#Same damage rules set prior with monster
#Dragon responds by using one of three attacks
#Set up 3 different attacks with different responses due to user weapon. 
#If user runs out of health, Game over.
def userDeath():
    print('You have run out of health.')
    print('GAME OVER')
#	If dragon defeated
#		Print you saved the day! 
#		Print remaining health with the userName they supplied
#		Save remaining health into .txt file with the userName they supplied 
#			Saves in order from most health to least inside the text document

def main():
    #set all health values
    userHealth = 15
    goblinHealth = 15
    dragonHealth = 20
    print("With your newfound information and dragon-slaying weapons, you set out on your")
    print("quest. (Your health has been set to 15)")
    print("")
    print("After traveling down the path for a while you hear a rustling in the bushes")
    print("You lean in to investigate and a goblin hurtles out of the bush, blocking your path")
    print("")
    while goblinHealth > 0:
        if userHealth <= 0:
            userDeath()
        goblinHealth = userAttackGoblin(goblinHealth)
        if goblinHealth <= 0:
            break
        #prompt user attack
        userHealth = goblinAttack(userHealth)
        #prompt goblin attack
    if crossRoad(userWeapon) == True:
        print("You come across a cave and hear the princess screaming from within. You quickly take off towards it")
        print("and evade a wall of flames. You found the dragon. It's pissed. You draw your weapon and engage the dragon.")
        print("")
        while dragonHealth > 0 :
            if userHealth <= 0:
                userDeath()
                break
            dragonHealth = userAttackDragon(dragonHealth)
            if dragonHealth <= 0:
                break
            #prompt user attack
            userHealth = dragonAttack(userHealth)
            #prompt dragon attack
            if userHealth <= 0:
                userDeath()
                break
    if dragonHealth <=0:
        print("Victorious! You have slain the dragon and rescued your princess!")
        print("Congratulations!",userName,"won with", userHealth, "health!")
        scoreList = []
        scoreList.append(userName)
        scoreList.append(userHealth)
        scoreList = str(scoreList)
        highScores = open("highScores.txt",'w')
        highScores.write(scoreList)
        highScores.close()
                
    else:
        userDeath()
    #import score to text document as a list with [username, score]
main()
