import json
from abc import ABC, abstractmethod

from src.config import PATH_VACATIONS_JSON
from src.vacancy import Vacancy


class AbstractJson(ABC):
    """Абстрактный класс для работы с файлами и вакансиями"""

    @abstractmethod
    def write_vacancies(self, vacancies):
        """Абстрактный метод записи вакансий в файл"""
        pass

    @abstractmethod
    def read_vacancies(self):
        """Абстрактный метод чтения вакансий из файла"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Абстрактный метод удаления всех вакансий из файла"""
        pass


class JSONSaver(AbstractJson):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, filename=PATH_VACATIONS_JSON):
        """Метод для инициализации класса JSONSaver"""
        self.__filename = filename

    def write_vacancies(self, vacancies: list[dict]):
        """Метод для добавления вакансий в JSON-файл"""

        with open(self.__filename, encoding="utf-8") as f:
            vacancies_filter = json.load(f)
        for vacancy in vacancies:
            count = 0
            for vac in range(len(vacancies_filter)):
                if vacancy["alternate_url"] == vacancies_filter[vac]["link"]:
                    count += 1
            if count == 0:
                vacancies_filter.append(
                    {
                        "name": vacancy["name"],
                        "link": vacancy["alternate_url"],
                        "salary": vacancy["salary"],
                        "description": vacancy["snippet"]["requirement"],
                    }
                )
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies_filter, f, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        """Метод чтения вакансий из JSON-файла"""

        with open(self.__filename, encoding="utf-8") as f:
            data = json.load(f)

        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies

    def delete_vacancies(self):
        """Метод удаления вакансий из JSON-файла"""

        with open(self.__filename, "w") as f:
            json.dump([], f)
