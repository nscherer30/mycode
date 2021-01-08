#!/usr/bin/python3

import random
import time


class Game:
    def __init__(self, settings, game_name="Zork - Explorer's Edition"):
        self.settings = settings
        self.game_name = game_name
        self.bandits = []

    def start(self, room_list):
        self.display_game_details()
        self.place_bandits(room_list, self.settings.get_difficulty())

    def display_game_details(self):
        print(f"You are playing {self.game_name}")
        self.settings.display_settings()

    def place_bandits(self, room_list, difficulty):
        lowerVal = 0
        higherVal = 0
        maxVal = len(room_list) - 1
        if difficulty == "easy":
            lowerVal = maxVal - 4
            higherVal = maxVal - 3
        elif difficulty == "normal":
            lowerVal = maxVal - 3
            higherVal = maxVal - 2
        elif difficulty == "hard":
            lowerVal = maxVal - 2
            higherVal = maxVal - 1
        elif difficulty == "impossible":
            lowerVal = maxVal - 1
            higherVal = maxVal

        num_of_bandits = lowerVal
        if random.randint(1, 100) > 50:
            num_of_bandits = higherVal
        else:
            num_of_bandits = lowerVal

        for bandit in range(num_of_bandits):
            for key in room_list.keys():
                new_bandit = Bandit()
                self.bandits.append(new_bandit)
                self.set_bandit_to_room(room_list[key], new_bandit.get_id())

    def set_bandit_to_room(self, room, bandit_id):
        room["bandit"] = bandit_id


class Settings:
    def __init__(self, total_rooms, difficulty="normal"):
        self.difficulty = difficulty  # Possible values include easy, normal, hard, impossible
        self.bandage_heal_value = self.generate_bandage_heal_value(self.difficulty)
        self.total_rooms = total_rooms

    def generate_bandage_heal_value(self, difficulty):
        if difficulty == "easy":
            return random.randrange(75, 90)
        elif difficulty == "normal":
            return random.randrange(50, 70)
        elif difficulty == "hard":
            return random.randrange(30, 50)
        elif difficulty == "impossible":
            return random.randrange(15, 25)

    def get_bandage_heal_value(self):
        return self.bandage_heal_value

    def get_difficulty(self):
        return self.difficulty

    def get_total_rooms(self):
        return self.total_rooms

    def display_settings(self):
        print(f"Game Settings")
        print(f"Difficulty: {self.difficulty}")
        print(f"Bandages heal: {self.bandage_heal_value} hp")


class Player:
    def __init__(self, name="player", hp=100, bandages_count=1, xp=0):
        self.name = name
        self.hp = hp
        self.bandages_count = bandages_count
        self.xp = xp

    def heal(self, settings):
        self.hp += settings.get_bandage_heal_value()
        self.bandages_count -= 1

    def fight(self, bandit):
        while self.hp > 0:
            pass
            # TODO

    def flee(self, bandit):
        # TODO
        pass

    def raise_xp(self, gained_xp):
        self.xp += gained_xp

    def get_hp(self):
        return self.hp

    def get_xp(self):
        return self.xp

    def display_status(self):
        print(f"{self.name} current status:")
        print(f"  HP: {self.hp}")
        print(f"  Bandages: {self.bandages_count} current status:")


class Bandit(Player):
    def __init__(self, name="bandit", hp=100, bandages_count=1):
        super().__init__(name, hp, bandages_count)
        self.id = random.randint(1, 1000000)

    def get_id(self):
        return self.id

