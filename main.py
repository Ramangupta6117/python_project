import random
list = ['rock','paper','scissor']
cpu_score=0
user_score=0
while True:
    user_choice=(input("rock, paper or  scissor? : "))
    cpu_choice = random.choice(list)

    if user_choice == 'exit':
        print("The game has ended")
        if user_score > cpu_score:
            print("CONGRATS! YOU HAVE WON!!!")
        elif user_score < cpu_score:
            print("ALAS! THE CPU HAS WON!!!")
        else:
            print("IT'S A TIE!!!!")
        break
        #==============================================
    if user_choice not in list:
        print("Invalid input")
        print("Please give a valid input!")
        print("USER : ", user_score)
        print("CPU : ", cpu_score)
        #===============================================
    if user_choice == "rock": #ROCK
        print("The CPU's choice was :", cpu_choice)
        if cpu_choice == "rock":
            print("TIE!")
            print("USER : ",user_score)
            print("CPU : ",cpu_score)
        elif cpu_choice == "paper":
            print("CPU wins! Paper covers rock!")
            cpu_score+=1
            print("USER : ", user_score)
            print("CPU : ", cpu_score)
        elif cpu_choice == "scissor":
            print("You win! Rock smashes Scissor!")
            user_score+=1
            print("USER : ", user_score)
            print("CPU : ", cpu_score)
        #================================================
    elif user_choice == "paper": #PAPER
            print("The CPU's choice was :", cpu_choice)
            if cpu_choice == "paper":
                print("TIE!")
                print("USER : ", user_score)
                print("CPU : ", cpu_score)
            elif cpu_choice == "rock":
                print("You win! Paper covers Rock!")
                user_score += 1
                print("USER : ", user_score)
                print("CPU : ", cpu_score)
            elif cpu_choice == "scissor":
                print("CPU wins! Scissor cuts Paper!")
                cpu_score+=1
                print("USER : ", user_score)
                print("CPU : ", cpu_score)
            #=============================================
    elif user_choice == "scissor": #SCISSOR
            print("The CPU's choice was :", cpu_choice)
            if cpu_choice == "scissor":
                print("TIE!")
                print("USER : ", user_score)
                print("CPU : ", cpu_score)
            elif cpu_choice == "paper":
                print("You win! Scissor cuts Paper!")
                user_score+=1
                print("USER : ", user_score)
                print("CPU : ", cpu_score)
            elif cpu_choice == "rock":
                print("CPU wins ! Rock smashes Scissor")
                cpu_score+=1
                print("USER : ", user_score)
                print("CPU : ", cpu_score)
            #===============================================
print("Final scores are :")
print("USER : ",user_score)
print("CPU : ",cpu_score)