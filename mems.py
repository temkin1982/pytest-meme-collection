class MemeCollection:
    def __init__(self):
        self.memes = []

    @staticmethod
    def _validate_meme_data(title, category, likes):
        if not isinstance(title, str):
            return "title должен быть строкой"

        if not isinstance(category, str):
            return "category должен быть строкой"

        if not isinstance(likes, int):
            return "likes должен быть числом"

        if likes < 0:
            return "likes не должен быть отрицательным"

        if title.strip() == "":
            return "title не должен быть пустым"

        if category.strip() == "":
            return "category не должен быть пустым"

        return True

    def add_meme(self, title, category, likes):
        result = self._validate_meme_data(title, category, likes)

        if result is True:
            self.memes.append({"title": title, "category": category, "likes": likes})
            return "Success"
        else:
            return result

    def get_by_category(self, category):
        return [meme for meme in self.memes if meme["category"] == category]

    def get_most_popular(self):
        if not self.memes:
            return None

        likes = list(map(lambda meme: meme["likes"], self.memes))
        max_likes = max(likes)
        return [meme for meme in self.memes if meme["likes"] == max_likes]

    def clear(self):
        self.memes = []


# 1 Создать фикстуру которая будет создать и возвращать пустую коллекцию
# 2 Создать фикстуру которая будет подготавливать данные и создавать коллекцию мемов
# 3 Создать тесты:
#               1 проверить что коллекция пустая
#               2 проверить что коллекция заполнена
#               3 добавить колецию посмотреть что есть новая запись
#               4 получить самый популярный мем
#               5 очистить мемы и проверить что они пустые
#               6 получить тесты по категории get_by_category (1 - такой мем существует, 2 - такой мем НЕ существует)
#               7 получить самый популярный мем get_most_popular (0 мем, 3 мемов с разной оценкой, 3 мемов с одинаковой оценкой,)
# 4 Создать тест с параметризайией на валидацию входящий данных по title, category, likes
