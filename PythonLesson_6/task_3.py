class Worker:
    def __init__(self, name, surname, position, _income={"wage": 120000, "bonus": 12000}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

a = Position("Jane","Doe", "CEO", {"wage": 220000, "bonus": 12000})
print(a.get_full_name())
print(a.get_total_income())
print(a.name)
print(a.position)

