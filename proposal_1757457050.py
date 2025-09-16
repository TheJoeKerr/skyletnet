import json

def get_welsh_genealogy_data():
    with open('welsh_genealogy.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    print(get_welsh_genealogy_data())