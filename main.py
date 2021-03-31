from Question import Question
import random
import datetime
import time
#import requests

#Implement a regex
now = datetime.datetime.now()
print("America's current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

variable_name = input("Please enter your Government Name: ")
print("Hi " + variable_name)
print("Welcome to your Citizenship Test!")

seconds = int(input("Type 3 so test begins in 3 seconds "))

time.sleep(3)

print("BEGIN NOW")

question_prompts = [
    "Who said, Luke, I am your father\n(a) Han Solo\n(b) Emperor\n(c) Darth Vader\n",
    "Which celeb said this about COVID-19: It's a virus. I get it, I respect it\n(a) Vanessa Hudgens\n(b) Madonna\n(c) Miley Cyrus\n",
    "Which Kardashian owns a sock line\n(a) Khloe\n(b) Rob\n(c) Karen\n",
    "Who was the first Disney Princess\n(a) Snow White\n(b) Cinderella\n(c) Aurora\n",
    "Who lived in America before the Europeans arrived\n(a) Romulans\n(b) American Indians\n(c) No One\n",
    "Who is Miley Cyrus godmother\n(a) Loretta Lynn\n(b) Reba McEntire\n(c) Dolly Parton\n",
    "Which Famous President was born in Kentucky\n(a) Andrew Jackon\n(b) Thomas Jefferson\n(c) Abraham Lincoln\n",
    "Who directed Jurassic Park\n(a) Martin Scorcese\n(b) George Lucas\n(C) Steven Spielberg\n",
    "Who produces the Real Housewives shows\n(a) Andy Cohen\n(b) Mark Burnett\n(c) Simon Cowell\n",
    "Yearly Americans eat 3 billion of these\n(a) Hot Dogs\n(b) Pizza Slices\n(c) Tacos\n",
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
    #player score
    score = 0

    #create a for loop
    for question in questions:
        answer = input(question.prompt)
        if answer != question.answer:
            print("Sorry, that is incorrect")

        else: 
            print ("Great!")
            score += 1
        print("Your current score is: ", str(score) + " out of", len(questions))
    print("Thank you for your interest " + variable_name + ", we'll think about it and get back to you." )

run_test(questions)

#Calculate and display data based on an external factor 
deadline = datetime.date(2021, 4, 19) - datetime.date.today() 
print("Thank you for playing and the deadline for the next REAL US Citizenship test it is in : ", deadline)