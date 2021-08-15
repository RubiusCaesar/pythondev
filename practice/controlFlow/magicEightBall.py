import random

name = "John Doe"
question = "Does this program work?"
answer = ""

random_num = random.randint(1, 10)
# print(str(random_num))

if random_num == 1:
    answer = "Yes - definitely."
elif random_num == 2:
    answer = "It is decidedly so."
elif random_num == 3:
    answer = "Without a doubt."
elif random_num == 4:
    answer = "Reply hazy, try again."
elif random_num == 5:
    answer = "Ask again later."
elif random_num == 6:
    answer = "Better not tell you now."
elif random_num == 7:
    answer = "My sources say no."
elif random_num == 8:
    answer = "Outlook not so good."
elif random_num == 9:
    answer = "Very doubtful."
elif random_num == 10:
    answer = "Fr fr?"
else:
    answer = "Error"

if question != "":
    if name != "":
        print(name + " asks: " + question)
    else:
        print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
else:
    print("No question means no answer")
