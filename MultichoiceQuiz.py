'''
This is a Python App that Runs a Quiz using Question Objects Created from a Question Class served into
a run_test fucntion in order to prompt users with questions after which the responses are evaluated instantly
and the results displayed to the user
I really want to learn how to use this Git Thingy
'''

#import the Question Class from which Question Objects will be formed for the Quiz
from Question import Question

#List of Questions and their corresponding answers that will be used to build the Question Objects
question_prompts = [
    ["Who is the President of the United States of Ameria?\n(a) Osama Bin Laden\n(b) Joe Biden\n(c) Masakela Travis\n(d) John Faray\n\n", "b"],
    ["What is the capital of Nigeria?\n(a) Cairo\n(b) Madagasca\n(c) Abuja\n(d) Harare\n\n", "c"],
    ["What color are African Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n(d) Pink\n\n", "d"],
    ["What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Green/Yellow\n(d) White\n\n", "c"],
    ["What is the capital of United States of America?\n(a) Brussels\n(b) Cairo\n(c) Washington DC\n(d) Ibadan\n\n", "c"],
    ["What do you call your father's brother?\n(a) Daddy\n(b) Bro\n(c) Uncle\n(d) Aunty\n\n", "c"],
    ["What color is portable water?\n(a) Cream\n(b) Marine Blue\n(c) Colourless\n(d) Ox Blood\n\n", "c"],
    ["Which part of Africa is Nigeria located?\n(a) West Africa\n(b) South Africa\n(c) East Africa\n(d) North Africa\n\n", "a"],
    ["When did Nigeria get it's Independence?\n(a) 1906\n(b) 1960\n(c) 800 BC\n(d) 2001\n\n", "b"],
    ["What are the colors of the Nigerian Flag?\n(a) Red and Green\n(b) Purple\n(c) Orange, Brown and Teal\n(d) Green, White and Green\n\n", "d"]
    ]

#This List will hold the Question Objects
questions = []
for elem in question_prompts:
    #Append Question Objects to the List
    questions.append(Question(elem[0], elem[1]))

#This function runs the Test/Quiz with supplied List containing Question Objects and Displays the Result
def run_test(question_list):
    score = 0
    for question in question_list:
        user_answer = input(question.prompt)
        if question.answer == user_answer:
            score += 1
    display_result = "You got " + str(score) + "/" + str(len(questions)) + " Correct in this Test"
    if score > len(questions)/2:
        display_result += "\nWow...Welldone, you did a Grest Job"
    else:
        display_result += "\nNot too good...You need to do better next time"
    print(display_result)

#Call the run_test() Function
run_test(questions)
