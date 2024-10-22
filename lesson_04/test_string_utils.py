# pylint: disable=missing-function-docstring

import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("input_string, exected_output", [
    ("skynet", "Skynet"),
    ("privet", "Privet"),
    ("523", "523"),

    ('', ""),
    (' ', " "),
    ("978test", "978test"),
])
def test_capitilize(input_string, exected_output):
    assert utils.capitilize(input_string) == exected_output


def test_trim():
    assert utils.trim(" skynet") == "skynet"
    assert utils.trim(" privet") == "privet"
    assert utils.trim(" Pro ") == "Pro "

    assert utils.trim("") == ""


@pytest.mark.parametrize('string, delimeter, result', [
   ("диван,стул,ложка", ",", ["диван", "стул", "ложка"]),
   ("1,2,3", ",", ["1", "2", "3"]),
   ("*;$;%;&", ";", ["*", "$", "%", "&"]),
   ("", None, []),
   ("1,2,3", None, ["1", "2", "3"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("диван", "д", True),
    ("кровать", "в", True),
    ("земля", "я", True),
    ("лада-калина", "-", True),
    ("145", "5", True),
    ("Skypro", "t", False),
    ("зима", "Д", False),
    ("бабочка", "@", False),
    ("", "  ", False),
    ("96587", "o", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Skypro", "k", "Sypro"),
    ("Ника", "и", "Нка"),
    ("917", "1", "97"),
    ("Лада-Калина", "-", "ЛадаКалина"),

    ("", "", ""),
    ("", "с", ""),
    ("мойка", "", "мойка"),
    ("грач", " ", "грач"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("гриб", "г", True),
    ("", "", True),
    ("Дельфин", "Д", True),
    ("Error",  "E", True),
    ("Пирог-картошка", "П", True),
    ("236", "2", True),

    ("Мороз", "м", False),
    ("Лошадь", "л", False),
    ("", "№", False),
    ("телевизор", "г", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Клава", "а", True),
    ("КАРТА", "А", True),
    ("", "", True),
    ("мешок.", ".", True),
    ("789", "9", True),

    ("речка", "к", False),
    ("", "*", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ("", True),
    (' ', True),
    ("  ", True),

    ("сторка не пустая", False),
    ("титаник ", False),
    ("5487", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, joiner, result', [
    (["M", "B", "R"], ",", "M,B,R"),
    ([5, 2, 4], ":", "5:2:4"),
    (["Летчик", "Истребитель"], "-", "Летчик-Истребитель"),
    (["Зима", "Лето"], "_", "Зима_Лето"),
    (["Саша", "Таня"], " ", "Саша Таня"),

    ([], None, ""),
    ([], ",", ""),
    ([], "  ", ""),
    ([], "мышь", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
