from src.hh_api import HHApi
from src.json_saver import JSONSaver
from src.utils import top_vacancies


hh = HHApi()
vacancies = hh.get_vacancies("python")
json_saver = JSONSaver()
json_saver.write_vacancies(vacancies)


vacs = json_saver.read_vacancies()

vacs = top_vacancies(vacs)

for vac in vacs:
    print(vac)


# def user_interface():
#     print("Меню")
#     print("1: Вывод топа вакансий")
#     print("2: Вывод вакансий по городу")
#     print("3: Вывод вакансий по диапазону зарплат")
#     print("3: Вывод вакансий, в которых есть какое-то ключевое слово")
