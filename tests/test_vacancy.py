def test_vacancy(first_vacancy):
    assert first_vacancy.name == "Web-программист"
    assert first_vacancy.link == "www.hh.ru/123"
    assert first_vacancy.desc == "программирует"


def test_validation_vacation(first_vacancy):
    assert first_vacancy.salary_middle == 100000


def test_middle_salary(second_vacancy):
    assert second_vacancy.salary_middle == 50000


def test_without_salary(vacancy_without_salary):
    assert vacancy_without_salary.salary_middle == 0


def test_comparison_vacations(first_vacancy, second_vacancy):
    assert first_vacancy > second_vacancy


def test_print_vacation(first_vacancy):
    assert str(first_vacancy) == (
        "Вакансия: Web-программист. Ссылка: " "www.hh.ru/123. Зарплата: 100000.0. Описание: программирует."
    )
