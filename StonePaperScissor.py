import random
while True:
    User_Action=input("Enter you choice(Stone,Paper,Scissor)")
    Possible_Action=["Stone","Paper","Scissor"]
    Computer_Action=random.choice(Possible_Action)
    print(f"\n You choose:{User_Action}  Computer Chose:{Computer_Action}\n")
    if User_Action==Computer_Action:
       print(f"\n Both players selected{User_Action}, its a tie")
    elif User_Action=="Stone":
        if Computer_Action=="Scissor":
            print("Stone smashes Scissors,You win")
        else:
            print("Paper captures Stone, You loose")
    elif User_Action=="Paper" :
        if Computer_Action=="Stone":
            print("Paper Captures Stone,You Win")
        else:
            print("Scissors cut paper, You loose")
    elif User_Action=="Scissor" :
        if Computer_Action=="Paper":
            print("Scissors cut paper,You Win")
        else:
            print("Rock smashes scissors, You loose")
    playInput=input("Play Again(Y/N)")
    if playInput!="Y":
       break