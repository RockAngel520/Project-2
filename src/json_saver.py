from abc import ABC, abstractmethod

import json

from src.vacancy import Vacancy


class AbstractJson(ABC):

    @abstractmethod
    def write_vacancies(self, vacancies):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(AbstractJson):
    def __init__(self, filename="data/vacancies.json"):
        self.__filename = filename


    def write_vacancies(self, vacancies: list[dict]):
        # Чтение файла, получение вакансий - будет список из словарей,
        # пробежаться по этому списку и проверить если вакансии среди
        # полученных вакансий, если нет, то добавить и потом сделать эту же
        # запись через "w"
        #

        vacancies_filter = []
        for vacancy in vacancies:
            vacancies_filter.append({"name": vacancy["name"], "link": vacancy["alternate_url"], "salary": vacancy["salary"],
                                     "description": vacancy["snippet"]["requirement"]})
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies_filter, f, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        with open(self.__filename, encoding="utf-8") as f:
            data = json.load(f)

        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies


    def delete_vacancies(self):
        with open(self.__filename, "w") as f:
            json.dump([], f)
