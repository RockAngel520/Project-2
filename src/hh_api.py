from abc import ABC, abstractmethod

import requests


class AbstractApi(ABC):
    """Абстрактный класс для работы с API-сервисами с вакансиями"""

    @abstractmethod
    def _connect(self, text):
        """Абстрактный метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, text):
        """Абстрактный метод для получения вакансий из запроса к API"""
        pass


class HHApi(AbstractApi):
    """Класс для работы с API сайта hh.ru с вакансиями"""

    def __init__(self, page=0):
        """Метод для инициализации экземпляра класса HHApi"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"page": page, "per_page": 30}

    def _connect(self, text):
        """Метод создания и отправки get запроса по API"""

        self.__params["text"] = text
        response = requests.get(self.__url, self.__params)
        if response.status_code == 200:
            return response
        else:
            print("Ошибка подключения к сервису")

    def get_vacancies(self, text):
        """Метод получения вакансий из запроса в формате JSON"""

        vacancies = self._connect(text).json()["items"]
        return vacancies
