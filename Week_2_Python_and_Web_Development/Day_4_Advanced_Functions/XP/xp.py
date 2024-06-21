#1
import random
def get_random_temp(season):
    if season=="Winter": return round(random.uniform(-10,10),1)
    if season=="Spring": return round(random.uniform(10,25),1)
    if season=="Summer": return round(random.uniform(25,40),1)
    if season=="Autumn": return round(random.uniform(5,20),1)
def main():
    month=int(input("Select month"))
    if month in [12,1,2]: season="Winter"
    elif month in [3,4,5]: season="Spring"
    elif month in [6,7,8]: season="Summer"
    elif month in [9,10,11]: season="Autumn"
    temperature=get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature<0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif temperature>=0 and temperature<16:
        print("Quite chilly! Don’t forget your coat")
    elif temperature>=16 and temperature<23:
        print("Nice weather! You should go for walk")
    elif temperature>=24 and temperature<32:
        print("Getting warmer! Summer is close")
    elif temperature>=32 and temperature<=40:
        print("Quite hot today! Don’t forget to drink water")
main()
#2
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def results(won,lost):
    if won>lost:
        print(f"Congatulations!!! You answerd {won} out of {len(data)} questions")
    else: print("You lost. Try another time")
  
def quiz():
    q_for_user=""
    won=0
    lost=0
    wrong_questions=[]
    for i in range(len(data)):
        q_for_user=input(f"{data[i]["question"]}")
        if q_for_user==data[i]["answer"]:
            print("That`s right")
            won+=1
        else: 
            print("That`s wrong answer")
            wrong_questions.append({"question":data[i]["question"],
                                "user_answer":q_for_user,
                                "answer":data[i]["answer"]})
            if lost<2: lost+=1   
            else: break 
    print(results(won,lost))
    if lost>0:
        print("Wrong answers:")
        for q in wrong_questions:
            print(f"Question: {q["question"]}\nYour answer: {q["user_answer"]}\nRight Answer: {q["answer"]}")
    else: print("There is no wrong answers")
quiz()
3
from datetime import datetime
retirement_age={"man":67,"woman":62}
def get_age():
    user_input=input("Please input your birthdate in form DD/MM/YYYY")
    today=datetime.today()
    birthdate=datetime.strptime(user_input,'%d/%m/%Y')
    users_age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.date))
    return(users_age)
def can_retire():
    age=get_age()
    user_input=input("Please input your gender")
    if retirement_age[user_input]>age:
        print(f"You are still young. Wait {retirement_age[user_input]-age} more year(s)")
        return False
    else: 
        print("You deserve it. Enjoy your retirement")
        return True
can_retire()
#4
def multiply(num):
    output=num+num*11+num*111+num*1111
    return(output)
print(multiply(7))