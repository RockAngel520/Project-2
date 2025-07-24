import json

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def test_write_vacancies(temp_json_file, test_vacancies):

    saver = JSONSaver(temp_json_file)
    saver.write_vacancies(test_vacancies)

    with open(temp_json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Web-программист"
    assert data[1]["name"] == "Секретарь"


def test_read_vacancies(temp_json_file, test_vacancies):

    saver = JSONSaver(temp_json_file)
    saver.write_vacancies(test_vacancies)

    vacancies = saver.read_vacancies()

    assert len(vacancies) == 2
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].name == "Web-программист"
    assert vacancies[1].name == "Секретарь"


def test_delete_vacancies(temp_json_file, test_vacancies):

    saver = JSONSaver(temp_json_file)
    saver.write_vacancies(test_vacancies)
    saver.delete_vacancies()

    with open(temp_json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 0
