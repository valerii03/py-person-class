class Person:
    # Класовий словник для зберігання всіх людей за іменем
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Додаємо цей екземпляр у словник people
        Person.people[name] = self


def create_person_list(people_dicts):
    # Перший прохід: створюємо всі екземпляри Person
    person_list = []
    for p in people_dicts:
        person_list.append(Person(p["name"], p["age"]))

    # Другий прохід: привязуємо атрибути wife/husband
    for p_dict in people_dicts:
        person = Person.people[p_dict["name"]]
        # Привязуємо дружину, якщо є
        if "wife" in p_dict and p_dict["wife"]:
            person.wife = Person.people[p_dict["wife"]]
        # Привязуємо чоловіка, якщо є
        if "husband" in p_dict and p_dict["husband"]:
            person.husband = Person.people[p_dict["husband"]]

    return person_list
