#!/usr/bin/env python3
import requests

def main():
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json")

    # print number of people
    num_people_in_space = r.json()["number"]
    print(f"People in space: {num_people_in_space}")

    # print each person and their craft
    for person in r.json()["people"]:
        print(f"{person['name']} on the {person['craft']}")

main()
