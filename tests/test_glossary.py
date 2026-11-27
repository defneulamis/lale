
import unittest
import sys
import os

# Make the src folder accessible
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from glossary_search import validate_glossary, normalize_turkish, search_terms


class TestGlossaryValidation(unittest.TestCase):

    def test_valid_glossary(self):
        glossary = [
            {
                "ID": "1",
                "English": "Quest",
                "Turkish": "Görev",
                "Genre": "RPG",
                "Context": "Player task",
                "Part_of_Speech": "Noun",
                "Notes": ""
            }
        ]

        self.assertTrue(validate_glossary(glossary))

    def test_duplicate_ids(self):
        glossary = [
            {
                "ID": "1",
                "English": "Quest",
                "Turkish": "Görev",
                "Genre": "RPG",
                "Context": "Player task",
                "Part_of_Speech": "Noun",
                "Notes": ""
            },
            {
                "ID": "01",
                "English": "Inventory",
                "Turkish": "Envanter",
                "Genre": "RPG",
                "Context": "Item storage",
                "Part_of_Speech": "Noun",
                "Notes": ""
            }
        ]

        self.assertFalse(validate_glossary(glossary))

    def test_missing_required_field(self):
        glossary = [
            {
                "ID": "1",
                "English": "",
                "Turkish": "Görev",
                "Genre": "RPG",
                "Context": "Player task",
                "Part_of_Speech": "Noun",
                "Notes": ""
            }
        ]

        self.assertFalse(validate_glossary(glossary))

    def test_invalid_id_format(self):
        glossary = [
            {
                "ID": "abc",
                "English": "Quest",
                "Turkish": "Görev",
                "Genre": "RPG",
                "Context": "Player task",
                "Part_of_Speech": "Noun",
                "Notes": ""
            }
        ]

        self.assertFalse(validate_glossary(glossary))

    def test_zero_id(self):
        glossary = [
            {
                "ID": "0",
                "English": "Quest",
                "Turkish": "Görev",
                "Genre": "RPG",
                "Context": "Player task",
                "Part_of_Speech": "Noun",
                "Notes": ""
            }
        ]

        self.assertFalse(validate_glossary(glossary))

class TestNormalizeTurkish(unittest.TestCase):

    def test_dotted_capital_i(self):
        self.assertEqual(normalize_turkish("İSTANBUL"), "istanbul")

    def test_dotless_capital_i(self):
        self.assertEqual(normalize_turkish("ISPARTA"), "ısparta")

    def test_already_lowercase(self):
        self.assertEqual(normalize_turkish("görev"), "görev")


class TestSearchTerms(unittest.TestCase):

    def setUp(self):
        self.glossary = [
            {"ID": "1", "English": "Quest", "Turkish": "Görev",
             "Genre": "RPG", "Context": "Player task",
             "Part_of_Speech": "Noun", "Notes": ""},
            {"ID": "2", "English": "Inventory", "Turkish": "Envanter",
             "Genre": "UI", "Context": "Item storage",
             "Part_of_Speech": "Noun", "Notes": ""},
        ]

    def test_find_by_english(self):
        results = search_terms("quest", self.glossary, "")
        self.assertEqual(len(results), 1)

    def test_find_by_turkish_uppercase(self):
        results = search_terms("GÖREV", self.glossary, "")
        self.assertEqual(len(results), 1)

    def test_genre_filter(self):
        results = search_terms("quest", self.glossary, "UI")
        self.assertEqual(len(results), 0)

    def test_no_match(self):
        results = search_terms("zzz", self.glossary, "")
        self.assertEqual(results, [])
if __name__ == "__main__":
    unittest.main()
