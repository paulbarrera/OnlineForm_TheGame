import random
import datetime
import time


now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
variable_name = input("Please enter your Government Name: ")
print("Hi " + variable_name)
print("Welcome to your Quiz!")


seconds = int(input("Type 10 so quiz begins in 10 seconds "))

time.sleep(10)

print("BEGIN")


def get_tof_questions():

    questions = []
    questions.append(["Darth Vader said, Luke, I am your father", "F"])
    questions.append(["Tiger King Documentary is only on Hulu", "F"])
    questions.append(["Krystal is a Kardashian sister", "F"])
    questions.append(["Snow White was the first Disney Princess", "F"])
    questions.append(["Harry Potter was a Horcrux", "T"])
    questions.append(["Dolly Parton is Miley Cyrus godmother", "T"])
    questions.append(["Abraham Lincoln was born in Kentucky", "T"])
    questions.append(["Did Michael Crichton write Jurassic Park", "T"])
    questions.append(["There are fourteen Real Housewives shows", "T"])
    questions.append(["Yearly Americans eat 3 billion pizzas", "T"])
    
    return questions

def play_tof_quiz():

        tof_questions = get_tof_questions()

        random.shuffle(tof_questions)

#player score 
        score = 0
        
#create a for loop
        for q in tof_questions:

            print("True or false: " + q[0])
            guess = input("Enter T or F: ") 
     
            if guess.lower() == q[1].lower():
                print("Correct")

                score = score + 1

            else:
                print("Incorrect")

#print final score
        #     if score > 6:
        #         print("You Pass!: " + str(score))
                
        #     elif score < 5:
        #         print("You fail!: " + str(score))

        print("Your Citizenship Quiz Score is: " + str(score))
        
play_tof_quiz()
