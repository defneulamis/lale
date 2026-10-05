import csv

print("Welcome to Lale!🌷")
print("Turkish Game Localization Toolkit")

with open("data/glossary.csv", "r", encoding="utf-8") as file:
    glossary = list(csv.DictReader(file))

while True:
    search_term = input("\nWhat term are you looking for? ")

    if search_term.lower() == "exit":
        print("Goodbye! 🌷")
        break

    if search_term.lower() == "list":
        print("Listing all terms in the glossary:")

        for term in glossary:
            print("-----------------------------")
            print("English:", term["English"])
            print("Turkish:", term["Turkish"])
            print("Genre:", term["Genre"])
            print("Context:", term["Context"])
            print("Notes:", term["Notes"])
            print("-----------------------------")

        continue

    genre = input("What genre? (leave blank for all): ")
    match_count = 0

    for term in glossary:
        if (search_term.lower() in term["English"].lower()
                or search_term.lower() in term["Turkish"].lower()):

            if genre == "" or genre.lower() == term["Genre"].lower():
                print("-----------------------------")
                print("English:", term["English"])
                print("Turkish:", term["Turkish"])
                print("Genre:", term["Genre"])
                print("Context:", term["Context"])
                print("Notes:", term["Notes"])
                print("-----------------------------")

                match_count += 1

    if match_count == 0:
        print("No matching terms found.")
    else:
        print("Matches found:", match_count)

