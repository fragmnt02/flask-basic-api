import json

file_directory = 'db.json'
json_data = open(file_directory).read()

data = json.loads(json_data)


class Person:
    def __init__(self, id):
        self.id = id
        self.name = data[self.id]['name']
        self.age = data[self.id]['age']
        self.company = data[self.id]['company']

    def get_name(self):
        return self.name

    def get_age(self):
        return str(self.age)

    def get_company(self):
        return str(self.company)


if __name__ == '__main__':
    pass
