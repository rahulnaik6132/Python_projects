questions = [
    ["What is my name\n", "rahul", "ajay", "kiran", "Rahul", "None", 1],
    [
        "What is my Full Name\n",
        "Rahul Ravikumar Naik",
        "ajay",
        "kiran",
        "Rahul",
        "None",
        1,
    ],
    ["What is my age\n", 21, 22, 25, 16, "None", 1],
    ["What is my fav-color\n", "red", "blue", "black", "white", "None", 2],
    ["What is my surname\n", "naik", "patil", "nayak", "thakur" "None", 1],
    ["Which is my fav_subject\n", "DSA", "OOSE", "OSD", "ALL", "None", 4],
    [
        "What i like most in food??\n",
        "Dal_rice",
        "Chicken",
        "Fish",
        "Potato",
        "None",
        3,
    ],
    ["How am I??", "silent", "Violent", "happy_soul", "depressed-boy", "None", 3],
    ["Who am i to you???", "Friend", "brother", "bf", "gf", "None", 2],
    ["Am I a boy or girl???", "boy", "girl", "dk", "a and b", "None", 1],
    [
        "What i wear regularly??",
        "Specs",
        "T-shirt",
        "Watch",
        "purse",
        "None",
        3,
    ],
    ["How is your bonding with me??", "Good", "Nice", "Bad", "Better", "None", 1],
    ["How Much money I borrowed from uh??", 0, "Nothing", 100, 200, "None", 2],
    ["How was the KBC??","Good","Best","Not Good","Great-time", "None", 4],
    ["How much u will rate for my KBC??", 7, 9, 8, 10, "None", 4],
]


levels = [
    1000,
    2000,
    3000,
    4000,
    5000,
    10000,
    20000,
    40000,
    60000,
    100000,
    320000,
    740000,
    1500000,
    4000000,
    10000000,
]

money = 0
print("\n\n\t\t             RAHUL'S LIFE         ")
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestions: {question[0]}")
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    reply = int(input("Enter your answer (1-4): "))
    if reply == question[-1]:
        print(f"\n\t\tCorrect answer you have won Rs {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
            print("\t\t1 Crore🥳🥳🥳")
    else:
        print("Wrong answer")
        break
print(f"\t\n\tTotal amount you can take home is: {money}\n")
