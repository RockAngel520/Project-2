import pytest

from src.vacancy import Vacancy


@pytest.fixture
def first_vacancy():
    return Vacancy(
        name="Web-программист",
        link="www.hh.ru/123",
        description="программирует",
        salary={"from": 100000, "to": 100000, "currency": "RUR", "gross": True},
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        name="Секретарь",
        link="www.hh.ru/321",
        description="печатает",
        salary={"from": None, "to": 50000, "currency": "RUR", "gross": True},
    )


@pytest.fixture
def vacancy_without_salary():
    return Vacancy(name="Секретарь", link="www.hh.ru/321", description="печатает", salary=None)


@pytest.fixture
def temp_json_file(tmp_path):
    temp_file = tmp_path / "test_vacancies.json"
    temp_file.write_text("[]", encoding="utf-8")
    return str(temp_file)


@pytest.fixture
def test_vacancies():
    return [
        {
            "name": "Web-программист",
            "alternate_url": "www.hh.ru/123",
            "salary": {"from": 100000, "to": 100000},
            "snippet": {"requirement": "программирует"},
        },
        {
            "name": "Секретарь",
            "alternate_url": "www.hh.ru/321",
            "salary": {"from": 30000, "to": 50000},
            "snippet": {"requirement": "печатает"},
        },
    ]
