from src.utils import print_vacancies, top_vacancies


def test_top_vacancies(first_vacancy, second_vacancy):
    assert top_vacancies([second_vacancy, first_vacancy]) == [first_vacancy, second_vacancy]


def test_print_vacancies(capsys, first_vacancy, second_vacancy):
    print_vacancies([first_vacancy, second_vacancy])
    captured = capsys.readouterr()
    assert captured.out == (
        "Вакансия: Web-программист. Ссылка: "
        "www.hh.ru/123. Зарплата: 100000.0. Описание: программирует.\n"
        "Вакансия: Секретарь. Ссылка: www.hh.ru/321. "
        "Зарплата: 50000. Описание: печатает.\n"
    )
