
import unittest
import sys
import os

# Make the src folder accessible
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from glossary_search import validate_glossary


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


if __name__ == "__main__":
    unittest.main()
