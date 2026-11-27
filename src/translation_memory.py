import csv


def load_translation_memory():
    with open(
        "data/translation_memory.csv",
        "r",
        encoding="utf-8"
    ) as file:

        translation_memory = list(csv.DictReader(file))

    return translation_memory
def get_approved_translations(translation_memory):
    approved_translations = []

    for entry in translation_memory:
        if entry["Status"].strip().lower() == "approved":
            approved_translations.append(entry)

    return approved_translations

def search_translation(search_text, translation_memory):
    if search_text.strip() == "":
        return []
    
    results = []

    for entry in translation_memory:
        if search_text.lower() in entry["English"].lower():
            if entry["Status"].strip().lower() == "approved":
                results.append(entry)

    return results
if __name__ == "__main__":
    memory = load_translation_memory()

    search_text = input("Enter an English sentence or word: ")

    results = search_translation(search_text, memory)

    for entry in results:
        print(entry["English"], "->", entry["Turkish"])
