import csv

print("Welcome to Lale!🌷")
print("Turkish Game Localization Toolkit")

with open("data/glossary.csv", "r", encoding="utf-8") as file:
    glossary = list(csv.DictReader(file))

search_term = input("What term are you looking for? ")

print("You searched for:", search_term)