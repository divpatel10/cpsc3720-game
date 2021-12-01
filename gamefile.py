import requests
from requests.auth import HTTPBasicAuth
import json

print("Welcome to Animal Charades, where you act out an animal doing a certain activity!")
verb = ["running", "walking", "sleeping", "dancing", "jumping", "singing", "swimming", "triping", "fighting", "crying", "laughing", "shouting", "cycling", "driving", "eating", "programming", "exercising", "cooking"]
while(True):
    animal_response = requests.get("https://random-word-form.herokuapp.com/random/animal")

    # print(animal_response.json())

    animal = animal_response.json()[0]

    max_num = len(verb) -1
    number_response = requests.get( f"http://www.randomnumberapi.com/api/v1.0/random?max={max_num}");

    number = number_response.json()[0]

    # print(number_response.json())

    print(f"Your animal and its activty is: A {verb[number]} {animal}\n\nPress Enter to generate another or type quit to end the game")

    playerInput = input()
    if(playerInput == "quit"):
        break
