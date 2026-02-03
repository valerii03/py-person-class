from typing import List, Dict, Optional


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        Person.people[name] = self


def create_person_list(people_dicts: List[Dict]) -> List[Person]:
    person_list = [
        Person(p["name"], p["age"])
        for p in people_dicts
    ]

    for p_dict in people_dicts:
        person = Person.people[p_dict["name"]]

        if p_dict.get("wife"):
            person.wife = Person.people[p_dict["wife"]]

        if p_dict.get("husband"):
            person.husband = Person.people[p_dict["husband"]]

    return person_list
