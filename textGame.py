def checkInputForYesNo(answer):
    while answer != "yes" and answer != "no":
        print ("WRONG ANSWER") #question2Forest
        answer = input()



print ("You start at a house. Would you like to enter? (yes or no)") #question1House
answer1 = input()
checkInputForYesNo(answer1)


#while answer1 != "yes" and answer1 != "no": #check if person said yes, no
 #   print ("WRONG ANSWER") #question1House
 #   answer1 = input()



if answer1 == "no":
    print("you decline. would you rather go to the forest? (yes or no) ") #question1Forest
    answer2 = input()


    while answer2 != "yes" and answer2 != "no":
        print ("WRONG ANSWER") #question1Forest
        answer2 = input()
    
    if answer2 == "yes":
        print("you see a campfire, do you go? (yes or no)") #question2Forest
        answer3 = input()

        while answer3 != "yes" and answer3 != "no": 
            print ("WRONG ANSWER") #question2Forest
            answer3 = input()


        

    elif answer2 == "no":
        print("do u wanna go to the house then lazybones. (yes or no?) ")
        
    
