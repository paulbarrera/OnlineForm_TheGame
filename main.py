from Question import Question
import random
import datetime
import time
# import requests

#Implement a regex
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%y-%m-%d %H:%M:%S"))


variable_name = input("Please enter your Government Name: ")
print("Hi " + variable_name)
print("Welcome to your Citizenship Test!")

seconds = int(input("Type 3 so test begins in 3 seconds "))

time.sleep(3)

print("BEGIN")

question_prompts = [
    "Who said, Luke, I am your father\n(a) Han Solo\n(b) Emperor\n(c) Darth Vader\n\\n",
    "Which celeb said this about COVID-19: It's a virus. I get it, I respect it\n(a) Vanessa Hudgens\n(b) Madonna\n(c) Miley Cyrus\n\\n",
    "Which Kardashian owns a sock line\n(a) Khloe\n(b) Rob\n(c) Karen\n\\n",
    "Who was the first Disney Princess\n(a) Snow White\n(b) Cinderella\n(c) Aurora\n\\n"
    "Who lived in America before the Europeans arrived\n(a) Romulans\n(b) American Indians\n(c) No One\n\\n",
    "Who is Miley Cyrus godmother\n(a) Loretta Lynn\n(b) Reba McEntire\n(c) Dolly Parton\n\\n",
    "Which Famous President was born in Kentucky\n(a) Andrew Jackon\n(b) Thomas Jefferson\n(c) Abraham Lincoln\n\\n",
    "Who directed Jurassic Park\n(a) Martin Scorcese\n(b) George Lucas\n(C) Steven Spielberg\n\\n",
    "Who produces the Real Housewives shows\n(a) Andy Cohen\n(b) Mark Burnett\n(c) Simon Cowell\n\\n",
    "Yearly Americans eat 3 billion of these\n(a) Hot Dogs\n(b) Pizza Slices\n(c) Tacos\n\\n",
]

#Create a dictionary or list. 
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
]

def run_test(questions):
    # player score
    score = 0
    # create a for loop
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got ", score + "out of", len(questions))

run_test(questions)

#Give the player there final score pass or fail.

#         else:
#             print("Incorrect")

#Print final score

#         if score > 6:
#                 print("You Pass!: " + str(score))

#         elif score < 5:
#                 print("You fail!: " + str(score))

#         print("Your Citizenship Quiz Score is: " + str(score))
