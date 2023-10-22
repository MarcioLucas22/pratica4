import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    
    
def avgAgeCountry(data):
    age_sum_by_country = {}
    count_by_country = {}

    for record in data:
        if 'age' in record and 'country' in record:
            age = record['age']
            country = record['country']

            if age is not None:
                age_sum_by_country[country] = age_sum_by_country.get(country, 0) + age
                count_by_country[country] = count_by_country.get(country, 0) + 1

    avg_age_by_country = {}
    for country in age_sum_by_country:
        avg_age_by_country[country] = age_sum_by_country[country] / count_by_country[country]

    return avg_age_by_country