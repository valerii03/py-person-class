class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts):
    person_list = []

    for person_data in people_dicts:
        person_list.append(Person(person_data["name"], person_data["age"]))

    for person_data in people_dicts:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]

    return person_list
