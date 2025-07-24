class Vacancy:
    """Класс для работы с вакансиями"""


    __slots__ = ("name", "link", "desc", "salary_from", "salary_to",
                 "salary_middle") # определяем какие атрибуты должны быть
    # в экземпляре класса


    def __init__(self, name, link, description, salary):
        """Метод для инициализации экземпляра класса Vacancy"""

        self.name = name
        self.link = link
        self.desc = description
        self.__validate(salary)


    def __validate(self, salary):
        """Метод приведения зарплаты к единому формату (валидации) и
        нахождение средней ЗП"""
        if salary:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
            if self.salary_to == 0 or self.salary_from == 0:
                self.salary_middle = (self.salary_from + self.salary_to)
            else:
                self.salary_middle = (self.salary_from + self.salary_to) / 2
        else:
            self.salary_middle = 0


    def __lt__(self, other):
        """Магический метод сравнения зарплат - меньше (<)"""

        return self.salary_middle < other.salary_middle


    def __str__(self):
        """Магический метод отображения информации о вакансии"""

        return f"Вакансия: {self.name}. Ссылка: {self.link}. Зарплата: {
        self.salary_middle}. Описание: {self.desc}."
