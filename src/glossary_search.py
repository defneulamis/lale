import csv

print("Welcome to Lale!🌷")
print("Turkish Game Localization Toolkit")

with open("data/glossary.csv", "r", encoding="utf-8") as file:
    glossary = list(csv.DictReader(file))

search_term = input("What term are you looking for? ")

found = False

for term in glossary:
    if term["English"].lower() == search_term.lower():
        print("English:", term["English"])
        print("Turkish:", term["Turkish"])
        print("Genre:", term["Genre"])
        print("Context:", term["Context"])
        print("Notes:", term["Notes"])

        found = True
if not found:
    print("Term not found in the glossary.")
