class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people):
    Person.people = {}

    result = [Person(p["name"], p["age"]) for p in people]

    for p in people:
        person = Person.people[p["name"]]

        wife = p.get("wife")
        if wife is not None:
            setattr(person, "wife", Person.people[wife])

        husband = p.get("husband")
        if husband is not None:
            setattr(person, "husband", Person.people[husband])

    return result

