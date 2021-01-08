#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget
from pprint import pprint


def main():
    pokemon = input("Enter a pokemon name [try Pikachu] >").strip().lower()
    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()

    # Print image link and download
    url = pokeapi["sprites"]["front_default"]
    print(f"Image url: {url}")
    wget.download(url, './')
    print(f"{pokemon} image downloaded")

    # Get pokemon moves
    moves = pokeapi["moves"]
    print(f"Here are {pokemon} moves")

    # Add all move names to a list
    move_name_list = []
    for move in moves:
        move_name_list.append(move["move"]["name"])
    # Print the list
    pprint(move_name_list)

    # Find number of games based on how long game_indices is
    num_of_games = len(pokeapi["game_indices"])
    print(f"{pokemon} was in {num_of_games} number of pokemon games")

main()
