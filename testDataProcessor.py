import os
import unittest
from dataProcessor import read_json_file, avgAgeCountry

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 100)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Amanda Middleton')
        self.assertEqual(data[1]['age'], 27)


    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")


    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    
    def test_avgAgeCountry_empty_json(self):
        data = []
        avg_age = avgAgeCountry(data)
        self.assertEqual(avg_age, 0)  # A média deve ser 0 para um JSON vazio.

    def test_avgAgeCountry_missing_age_values(self):
        data = [
            {'name': 'John', 'age': 30},
            {'name': 'Jane'},
            {'name': 'Bob', 'age': None}
        ]
        avg_age = avgAgeCountry(data)
        self.assertEqual(avg_age, 30)  # A média deve ser a idade de John, 30.

    def test_avgAgeCountry_missing_country(self):
        data = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30},
            {'name': 'Eve'}
        ]
        avg_age = avgAgeCountry(data)
        self.assertEqual(avg_age, 27.5)  # A média deve ser a média das idades de Alice e Bob.


if __name__ == '__main__':
    unittest.main()