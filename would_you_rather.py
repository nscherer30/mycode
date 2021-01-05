#!/usr/bin/env python3
import random
# Would you Rather Game for hobbies

class Player():
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.points = {
            "outdoor": 0,
            "sports": 0,
            "fitness": 0
        }

outdoor_values = {
    "hiking": 7,
    "running": 4,
    "backpacking": 8,
    "snowboarding": 5,
    "football": 3,
    "soccer": 3,
    "baseball": 2
}

sports_values = {
    "long distance running": 3,
    "track": 4,
    "basketball": 4,
    "tennis": 3,
    "football": 5,
    "soccer": 4,
    "baseball": 2
}

fitness_values = {
    "running": 3,
    "track": 4,
    "basketball": 4,
    "hiking": 3,
    "backpacking": 3
}

values = [outdoor_values, sports_values, fitness_values]

def check_for_bad_city(city):
    if city == "newark":
        print("Yikes, you live in Newark?!")
    elif city == "seattle":
        print("Another techie I see..")
    elif city == "new york city":
        print("Is it true people live in bathrooms in NYC?")
    elif city == "austin":
        print("Silicon Valley of Texas, I like it.")
    elif city == "atlanta":
        print("Heard it's humid there..")
    else:
        print(f"Never heard of {city} so I guess I will have to check it out.")

def adjust_points(user_answer, player):
    for hobby in values:
        if user_answer in hobby:
            # User answer is listed in this hobby
            if hobby == outdoor_values:
                player.points["outdoor"] = player.points["outdoor"] + 1
            elif hobby == sports_values:
                player.points["sports"] = player.points["sports"] + 1
            elif hobby == fitness_values:
                player.points["fitness"] = player.points["fitness"] + 1

def get_random_choices():
    while True:
        hobby_one = random.choice(values)
        hobby_two = random.choice(values)
        if hobby_one != hobby_two:
            activity_one = random.choice(list(hobby_one))
            activity_two = random.choice(list(hobby_two))
            if activity_one != activity_two:
                string = f"{activity_two} or {activity_one}"
                return string



if __name__ == '__main__':
    name = input("What is your name?").lower().strip()
    city = input("What city do you live in?").lower().strip()
    check_for_bad_city(city)
    player = Player(name, city)
    game_turns = 1
    while game_turns < 15:
        question_answer = input(f"What interests you more: {get_random_choices()}?")
        adjust_points(question_answer, player)
        game_turns = game_turns + 1

    print(f"Your most interested hobby seems to be {max(player.points, key=player.points.get)}")


