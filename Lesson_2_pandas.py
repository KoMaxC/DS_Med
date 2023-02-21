import numpy as np
import pandas as pd

# создаем DataFrame с указанными данными
authors_data = {"author_id": [1, 2, 3],
                "author_name": ['Тургенев', 'Чехов', 'Островский']}
authors = pd.DataFrame(authors_data)
print("Датафрейм authors")
print(authors)

books_data = {"author_id": [1, 1, 1, 2, 2, 3, 3],
              "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой',
                             'Гроза', 'Таланты и поклонники'],
              "price": [1200, 2300, 900, 1000, 789, 2340, 1376]}
book = pd.DataFrame(books_data)
print("Датафрейм book")
print(book)

# объединяем фреймы по столбцу author_id
authors_price = pd.DataFrame.merge(authors, book, on="author_id")
print("Датафрейм authors_price")
print(authors_price)

# находим топ 5 книг
top_5 = pd.DataFrame(authors_price.nlargest(5, "price"))
print("Датафрейм топ 5 книг по цене")
print(top_5)

# создаем параметр для группировки
parameters = {'price': ['max', 'min', 'mean']}

# создаем датафрейм с требуемыми столбцами и данными
author_stats = authors_price.groupby(['author_name']).agg(parameters).round(2).rename(columns={"min": "min_price",
                                                                                               "max": "max_price",
                                                                                               "mean": "mean_price"})
author_stats.columns = author_stats.columns.droplevel(0)
print("Датафрейм autors_stats")
print(author_stats)
# author_stats.to_csv('file.csv')


# добавим столбец cover в датафрейм authors_price
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']

print('Датафрейм authors_price')
print(authors_price)

# формируем pivot_table с индексом author_name и колонками cover
book_info = pd.pivot_table(authors_price, index=['author_name'], columns=['cover'], values=['price'],
                           aggfunc=[np.sum], fill_value=0)
print("pivot table")
print(book_info)

# сохраняем в формате pickle
book_info.to_pickle("book_info.pkl")

# создадим новый датафрейм и загрузим в него полученный файл
new_book_info = pd.read_pickle("book_info.pkl")

# выведем на экран полученный датафрейм
print("датафрейм из файла")
print(new_book_info)

