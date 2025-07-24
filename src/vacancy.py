class Vacancy:
    # __slots__

    def __init__(self, name, link, salary, description):
        self.name = name
        self.link = link
        self.desc = description
        self.__validate(salary)

    def __validate(self, salary):
        if salary:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
            if self.salary_to == 0 or self.salary_from:
                self.salary_middle = (self.salary_from + self.salary_to)
            else:
                self.salary_middle = (self.salary_from + self.salary_to) / 2
        else:
            self.salary_middle = 0


    def __lt__(self, other):
        """<"""
        return self.salary_middle < other.salary_middle


    def __str__(self):
        return f"Название: {self.name}. Ссылка: {self.link}. Зарплата: {self.salary_middle}."


