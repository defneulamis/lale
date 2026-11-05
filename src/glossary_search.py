import difflib
import csv

def normalize_english(text):
    return text.lower()


def normalize_turkish(text):
    text = text.replace("İ", "i")
    text = text.replace("I", "ı")
    return text.lower()

def display_term(term):
    print("-----------------------------")
    print("ID:", term["ID"])
    print("English:", term["English"])
    print("Turkish:", term["Turkish"])
    print("Genre:", term["Genre"])
    print("Context:", term["Context"])
    print("Part of Speech:", term["Part_of_Speech"])
    print("Notes:", term["Notes"])
    print("-----------------------------")



def find_similar_terms(search_term, glossary, genre):
    matches = []

    for term in glossary:

        # Apply the genre filter before checking similarity
        if genre != "" and genre.lower() != term["Genre"].lower():
            continue

        english_score = difflib.SequenceMatcher(
            None,
            normalize_english(search_term),
            normalize_english(term["English"])
        ).ratio()

        turkish_score = difflib.SequenceMatcher(
            None,
            normalize_turkish(search_term),
            normalize_turkish(term["Turkish"])
        ).ratio()

        # Keep whichever language gives the higher score
        score = max(english_score, turkish_score)

        if score >= 0.75:
            matches.append((term, score))

    # Remove exact duplicate records
    unique_matches = []

    for term, score in matches:
        already_added = False

        for existing_term, existing_score in unique_matches:
            if term == existing_term:
                already_added = True
                break

        if not already_added:
            unique_matches.append((term, score))

    # Sort from highest similarity to lowest
    unique_matches.sort(key=lambda item: item[1], reverse=True)

    return unique_matches



def add_term():
    term_id = input("Enter the ID: ")
    english = input("Enter the English term: ")
    turkish = input("Enter the Turkish term: ")
    genre = input("Enter the genre: ")
    context = input("Enter the context: ")
    part_of_speech = input("Enter the part of speech: ")
    notes = input("Enter any notes: ")

    new_term = {
        "ID": term_id,
        "English": english,
        "Turkish": turkish,
        "Genre": genre,
        "Context": context,
        "Part_of_Speech": part_of_speech,
        "Notes": notes
    }

    with open("data/glossary.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "ID", "English", "Turkish", "Genre",
                "Context", "Part_of_Speech", "Notes"
            ]
        )
        writer.writerow(new_term)

    glossary.append(new_term)
    print("Term added successfully!")

print("Welcome to Lale!🌷")
print("Turkish Game Localization Toolkit")

with open("data/glossary.csv", "r", encoding="utf-8") as file:
    glossary = list(csv.DictReader(file))


while True:
    search_term = input("\nWhat term are you looking for? ")

    if search_term.lower() == "exit":
        print("Goodbye! 🌷")
        break

    if search_term.lower() == "add":
        add_term()
        continue

    if search_term.lower() == "list":
        print("Listing all terms in the glossary:")

        for term in glossary:
            display_term(term)

        continue

    genre = input("What genre? (leave blank for all): ")
    match_count = 0

    for term in glossary:
        if (normalize_english(search_term) in normalize_english(term["English"])
                or normalize_turkish(search_term) in normalize_turkish(term["Turkish"])):

            if genre == "" or genre.lower() == term["Genre"].lower():
                display_term(term)
                match_count += 1

    


    if match_count == 0:
        similar_terms = find_similar_terms(search_term, glossary, genre)

        if similar_terms:
            print("No exact matches. Did you mean:")

            for term, score in similar_terms:
                print(f"Similarity: {score:.0%}")
                display_term(term)

        else:
            print("No matching terms found.")

    else:
        print("Matches found:", match_count)
