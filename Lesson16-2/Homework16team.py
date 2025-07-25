class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )


def test_team_lead_attributes():
    lead = TeamLead("Anna", 9000, "R&D", "Python", 5)

    assert hasattr(lead, "name"), "Атрибут 'name' відсутній"
    assert hasattr(lead, "salary"), "Атрибут 'salary' відсутній"
    assert hasattr(lead, "department"), "Атрибут 'department' відсутній"
    assert hasattr(lead, "programming_language"), "Атрибут 'programming_language' відсутній"
    assert hasattr(lead, "team_size"), "Атрибут 'team_size' відсутній"

    print("Усі атрибути є.")


# Запуск тесту
test_team_lead_attributes()
