from src.hh_api import HHApi
from src.json_saver import JSONSaver
from src.utils import top_vacancies, print_vacancies


def user_interface():
    """Функция взаимодействия с пользователем"""

    print("Программа запущена\n")

    json_saver = JSONSaver()

    while True:
        new_search_input = input("Очистить данные предыдущего поиска или "
                               "добавить новый поисковый "
              "запрос к старому? (О)чистить (по-умолчанию) / (Д)обавить. \n")
        if new_search_input.lower() == "о" or new_search_input.lower() == "":
            json_saver.delete_vacancies()
            print("Данные предыдущего поиска очищены\n")
            break
        elif new_search_input.lower() == "д":
            print(f"Данные из поискового запроса будут добавлены к старому\n")
            break
        else:
            print("Введите \"О\" или \"Д\"")

    key_word = input("Введите поисковый запрос для запроса вакансий из hh.ru:\n")


    hh = HHApi()
    vacancies = hh.get_vacancies(key_word)


    json_saver.write_vacancies(vacancies)

    vacs = json_saver.read_vacancies()

    while True:
        user_want_top = input("Хотите ли Вы получить только топ вакансий по "
                            "зарплате? ("
                          "Да/Нет)\n")
        if user_want_top.lower() == "да":
            user_want_top_yes = True
            break
        elif user_want_top.lower() == "нет":
            user_want_top_yes = False
            print(f"Будут отображены все вакансии с ключевым словом \"{key_word}\"\n")
            break
        else:
            print("Введите \"Да\" или \"Нет\"")

    n_top = "все"

    while True:
        if user_want_top_yes:
            n_top = input("Сколько первых вакансий отобразить? ("
                          "по-умолчанию 5)\n")
            if not n_top.isdigit() and n_top != "":
                print("Возможен ввод только чисел")
            else:
                break
        else:
            break

    if n_top == "все":
        print_vacancies(vacs)
    elif n_top == "":
        vacs = top_vacancies(vacs)
        print_vacancies(vacs)
    else:
        vacs = top_vacancies(vacs, int(n_top))
        print_vacancies(vacs)



if __name__ == "__main__":
    user_interface()