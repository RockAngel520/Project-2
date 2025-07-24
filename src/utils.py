from src.vacancy import Vacancy


def filter_vacancies_by_name(vacancies: list[Vacancy]):
    pass

def top_vacancies(vacancies: list[Vacancy], top=5):
    return sorted(vacancies, reverse=True)[:top]

def filter_vacancies_by_salary(vacancies: list[Vacancy]):
    pass

def print_vacancies(vacancies: list[Vacancy]):
    pass
