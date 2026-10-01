import csv

print("Welcome to Lale!🌷")
print("Turkish Game Localization Toolkit")

with open("data/glossary.csv", "r", encoding="utf-8") as file:
    glossary = list(csv.DictReader(file))

search_term = input("What term are you looking for? ")
match_count = 0
for term in glossary:
    if search_term.lower() in term["English"].lower():
        print("English:", term["English"])
        print("Turkish:", term["Turkish"])
        print("Genre:", term["Genre"])
        print("Context:", term["Context"])
        print("Notes:", term["Notes"])
        print()

        match_count += 1

if match_count == 0:
    print("No matching terms found.")
else:
    print("Matches found:", match_count)

