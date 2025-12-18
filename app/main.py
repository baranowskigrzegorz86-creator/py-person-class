class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people):
    Person.people = {}

    result = []
    for p in people:
        result.append(Person(p["name"], p["age"]))

    for p in people:
        person = Person.people[p["name"]]

        if "wife" in p and p["wife"] is not None:
            setattr(person, "wife", Person.people[p["wife"]])

        if "husband" in p and p["husband"] is not None:
            setattr(person, "husband", Person.people[p["husband"]])

    return result
