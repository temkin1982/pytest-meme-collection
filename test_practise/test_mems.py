import pytest
from mems import MemeCollection
from test_data import memes, ids


# 1 Создать фикстуру которая будет создать и возвращать пустую коллекцию
@pytest.fixture
def empty_collection():
    return MemeCollection()


# 2 Создать фикстуру которая будет подготавливать данные и создавать коллекцию мемов
@pytest.fixture
def memes_collection():
    collection = MemeCollection()
    collection.add_meme("Сидим с бобром за столом", "песня", 100)
    collection.add_meme("Ты адекватная? А ниче тот факт, что…", "видео", 601)
    collection.add_meme("Лабубу", "игра", 7)
    collection.add_meme("Эффект Долиной", "ситуация", 5001)
    collection.add_meme("6-7", "ситуация", 31)
    return collection


# 3 Создать тесты:
#               1 проверить что коллекция пустая
@pytest.mark.smoke
def test_empty_collection(empty_collection):
    assert empty_collection.memes == [], "Collection is not empty"


#               2 проверить что коллекция заполнена
@pytest.mark.smoke
def test_memes_collection(memes_collection):
    assert memes_collection.memes != [], "Collection is empty"


#               3 добавить коллекцию посмотреть что есть новая запись
@pytest.mark.regression
def test_add_meme(memes_collection):
    count_before = len(memes_collection.memes)
    memes_collection.add_meme("Python", "Book", 8000)
    assert len(memes_collection.memes) == count_before + 1, "Meme was not added"


#               4 получить самый популярный мем
@pytest.mark.regression
def test_get_most_popular(memes_collection):
    result = memes_collection.get_most_popular()
    assert result[0]["title"] == "Эффект Долиной", "Wrong title"
    assert result[0]["category"] == "ситуация", "Wrong category"
    assert result[0]["likes"] == 5001, "Wrong likes"


#               5 очистить мемы и проверить что они пустые
@pytest.mark.regression
def test_clear(memes_collection):
    memes_collection.clear()
    assert memes_collection.memes == [], "Collection is not empty after clear"


#               6 получить тесты по категории get_by_category
#           (1 - такой мем существует, 2 - такой мем НЕ существует)
# Тест 1 - категория ЕСТЬ:
@pytest.mark.regression
def test_get_by_category_exists(memes_collection):
    result = memes_collection.get_by_category("ситуация")
    assert result != [], "Category not found"


# Тест 2 - категории НЕТ:
@pytest.mark.regression
def test_get_by_category_not_exists(memes_collection):
    result = memes_collection.get_by_category("музыка")
    assert result == [], "Category should not exist"


#               7 получить самый популярный мем get_most_popular
#        (0 мем, 3 мемов с разной оценкой, 3 мемов с одинаковой оценкой,)
@pytest.mark.smoke
def test_get_most_popular_empty(empty_collection):
    result = empty_collection.get_most_popular()
    assert result is None, "Should return None for empty collection"


@pytest.mark.regression
def test_get_most_popular_different(empty_collection):
    empty_collection.add_meme("Dina", "python", 80)
    empty_collection.add_meme("Marina", "python", 50)
    empty_collection.add_meme("Dima", "python", 30)
    result = empty_collection.get_most_popular()
    assert result[0]["title"] == "Dina", "Wrong title"
    assert result[0]["category"] == "python", "Wrong category"
    assert result[0]["likes"] == 80, "Wrong likes"


@pytest.mark.regression
def test_get_most_popular_equal(empty_collection):
    empty_collection.add_meme("Dina", "python", 100)
    empty_collection.add_meme("Marina", "python", 100)
    empty_collection.add_meme("Dima", "python", 100)
    result = empty_collection.get_most_popular()
    assert len(result) == 3, "Should return all 3 winners"


# 4 Создать тест с параметризацией на валидацию входящих данных по title, category, likes


@pytest.mark.param
@pytest.mark.parametrize("title, category, likes, expected_result", memes, ids=ids)
def test_validate_meme_data(title, category, likes, expected_result):
    collection = MemeCollection()
    result = collection.add_meme(title, category, likes)
    assert result == expected_result, f"Expected {expected_result} but got {result}"
