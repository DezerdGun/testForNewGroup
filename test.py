questions = [
    {
        "question": "Что делает функция `range()` в Python?",
        "options": [
            "a) Создает список чисел",
            "b) Создает генератор чисел",
            "c) Создает строку чисел",
            "d) Создает кортеж чисел"
        ],
        "answer": "b"
    },
    {
        "question": "Какой результат выполнения выражения `2 ** 3` в Python?",
        "options": [
            "a) 5",
            "b) 6",
            "c) 8",
            "d) 9"
        ],
        "answer": "c"
    },
    {
        "question": "Какое значение имеет переменная `x` после выполнения следующего кода:\n```python\nx = [1, 2, 3]\ny = x\ny.append(4)\n```",
        "options": [
            "a) [1, 2, 3]",
            "b) [1, 2, 3, 4]",
            "c) [4, 1, 2, 3]",
            "d) Ошибка выполнения"
        ],
        "answer": "b"
    },
    {
        "question": "Что вернет следующий код:\n```python\ndef func(a, b=[]):\n    b.append(a)\n    return b\n\nresult = func(1)\nresult = func(2, result)\nresult = func(3)\n```",
        "options": [
            "a) [1, 2, 3]",
            "b) [3]",
            "c) [1, 3]",
            "d) [1, 2, 3, 3]"
        ],
        "answer": "d"
    },
    {
        "question": "Что делает оператор `is` в Python?",
        "options": [
            "a) Проверяет эквивалентность объектов",
            "b) Проверяет идентичность объектов",
            "c) Проверяет тип объекта",
            "d) Проверяет значение объекта"
        ],
        "answer": "b"
    },
    {
        "question": "Что такое Django?",
        "options": [
            "a) Язык программирования",
            "b) Веб-фреймворк",
            "c) База данных",
            "d) Текстовый редактор"
        ],
        "answer": "b"
    },
    {
        "question": "Какой файл используется для настройки URL в Django?",
        "options": [
            "a) settings.py",
            "b) urls.py",
            "c) views.py",
            "d) models.py"
        ],
        "answer": "b"
    },
    {
        "question": "Как создать новую модель в Django?",
        "options": [
            "a) class NewModel(models.Class)",
            "b) class NewModel(models.Model)",
            "c) def NewModel(models.Model)",
            "d) def NewModel(models.Class)"
        ],
        "answer": "b"
    },
    {
        "question": "Какую команду нужно использовать для создания миграций в Django?",
        "options": [
            "a) python manage.py makemigrations",
            "b) python manage.py migrate",
            "c) python manage.py runserver",
            "d) python manage.py createsuperuser"
        ],
        "answer": "a"
    },
    {
        "question": "Для чего используется файл settings.py в Django?",
        "options": [
            "a) Для настройки URL",
            "b) Для настройки моделей",
            "c) Для настройки проекта",
            "d) Для настройки тестов"
        ],
        "answer": "c"
    },
    {
        "question": "Что такое SQL?",
        "options": [
            "a) Язык программирования",
            "b) Язык запросов к базам данных",
            "c) Язык разметки",
            "d) Операционная система"
        ],
        "answer": "b"
    },
    {
        "question": "Какая команда используется для выборки данных из базы данных?",
        "options": [
            "a) SELECT",
            "b) INSERT",
            "c) UPDATE",
            "d) DELETE"
        ],
        "answer": "a"
    },
    {
        "question": "Какую команду нужно использовать для добавления новой записи в таблицу?",
        "options": [
            "a) SELECT INTO",
            "b) INSERT INTO",
            "c) UPDATE INTO",
            "d) DELETE INTO"
        ],
        "answer": "b"
    },
    {
        "question": "Какую команду нужно использовать для изменения существующей записи в таблице?",
        "options": [
            "a) SELECT",
            "b) INSERT",
            "c) UPDATE",
            "d) DELETE"
        ],
        "answer": "c"
    },
    {
        "question": "Что делает команда `DELETE FROM table_name`?",
        "options": [
            "a) Удаляет таблицу",
            "b) Удаляет базу данных",
            "c) Удаляет все записи из таблицы",
            "d) Удаляет конкретные записи из таблицы"
        ],
        "answer": "c"
    },
    {
        "question": "Что такое Git?",
        "options": [
            "a) Система управления базами данных",
            "b) Система контроля версий",
            "c) Система операционных систем",
            "d) Система управления проектами"
        ],
        "answer": "b"
    },
    {
        "question": "Какую команду нужно использовать для клонирования репозитория?",
        "options": [
            "a) git clone",
            "b) git pull",
            "c) git push",
            "d) git commit"
        ],
        "answer": "a"
    },
    {
        "question": "Какая команда используется для создания новой ветки?",
        "options": [
            "a) git branch new_branch",
            "b) git checkout new_branch",
            "c) git merge new_branch",
            "d) git pull new_branch"
        ],
        "answer": "a"
    },
    {
        "question": "Какую команду нужно использовать для объединения веток?",
        "options": [
            "a) git branch",
            "b) git checkout",
            "c) git merge",
            "d) git push"
        ],
        "answer": "c"
    },
    {
        "question": "Для чего используется команда `git commit`?",
        "options": [
            "a) Для сохранения изменений в локальном репозитории",
            "b) Для отправки изменений на удаленный репозиторий",
            "c) Для создания новой ветки",
            "d) Для удаления ветки"
        ],
        "answer": "a"
    },
    {
        "question": "Какое предназначение у команды `git push`?",
        "options": [
            "a) Загрузка изменений на удаленный репозиторий",
            "b) Слияние веток",
            "c) Создание новой ветки",
            "d) Удаление ветки"
        ],
        "answer": "a"
    },
    {
        "question": "Что такое индекс в контексте Git?",
        "options": [
            "a) База данных коммитов",
            "b) Текущая рабочая директория",
            "c) Список изменений перед коммитом",
            "d) Удаленный репозиторий"
        ],
        "answer": "c"
    },
    {
        "question": "Что делает команда `git pull`?",
        "options": [
            "a) Обновляет локальный репозиторий до последних изменений из удаленного",
            "b) Отправляет изменения на удаленный репозиторий",
            "c) Создает новую ветку",
            "d) Удаляет ветку"
        ],
        "answer": "a"
    },
    {
        "question": "Какие из перечисленных языков программирования могут использоваться для написания хранимых процедур в MySQL?",
        "options": [
            "a) SQL",
            "b) Python",
            "c) Java",
            "d) PHP"
        ],
        "answer": "a"
    },
    {
        "question": "Что такое ключевое слово `WHERE` в SQL?",
        "options": [
            "a) Оператор для сортировки данных",
            "b) Оператор для фильтрации данных",
            "c) Оператор для объединения таблиц",
            "d) Оператор для удаления данных"
        ],
        "answer": "b"
    },
    {
        "question": "Какие операторы используются для проверки равенства значений в SQL?",
        "options": [
            "a) = и <>",
            "b) == и !=",
            "c) IS и IS NOT",
            "d) LIKE и NOT LIKE"
        ],
        "answer": "a"
    },
    {
        "question": "Какие типы соединений (joins) существуют в SQL?",
        "options": [
            "a) Внутреннее, левое, правое и полное",
            "b) Внешнее и внутреннее",
            "c) Левое, правое и внешнее",
            "d) Левое и правое"
        ],
        "answer": "a"
    },
    {
        "question": "Что такое первичный ключ (primary key) в SQL?",
        "options": [
            "a) Уникальный индекс для ускорения поиска",
            "b) Уникальное поле, которое идентифицирует каждую запись в таблице",
            "c) Колонка, которая ссылается на другую таблицу",
            "d) Индекс, который разрешает дубликаты значений"
        ],
        "answer": "b"
    },
    {
        "question": "Что такое внешний ключ (foreign key) в SQL?",
        "options": [
            "a) Уникальное поле, которое идентифицирует каждую запись в таблице",
            "b) Колонка, которая ссылается на другую таблицу",
            "c) Индекс для ускорения поиска",
            "d) Индекс, который разрешает дубликаты значений"
        ],
        "answer": "b"
    },
    {
        "question": "Какие операторы используются для сравнения значений в SQL?",
        "options": [
            "a) =, <, >, <=, >=, <>",
            "b) ==, <, >, <=, >=, !=",
            "c) IS, IS NOT",
            "d) LIKE, NOT LIKE"
        ],
        "answer": "a"
    },
    {
        "question": "Какой оператор используется для сортировки данных в SQL?",
        "options": [
            "a) SORT BY",
            "b) GROUP BY",
            "c) ORDER BY",
            "d) SORT"
        ],
        "answer": "c"
    },
    {
        "question": "Что делает команда `GROUP BY` в SQL?",
        "options": [
            "a) Удаляет дубликаты из результата запроса",
            "b) Сортирует данные в обратном порядке",
            "c) Группирует строки с одинаковыми значениями в указанные столбцы",
            "d) Выполняет кросс-таблицу"
        ],
        "answer": "c"
    },
    {
        "question": "Какие функции используются для агрегации данных в SQL?",
        "options": [
            "a) ADD, SUBTRACT, MULTIPLY, DIVIDE",
            "b) COUNT, SUM, AVG, MAX, MIN",
            "c) UPDATE, INSERT, DELETE",
            "d) SELECT, FROM, WHERE"
        ],
        "answer": "b"
    },
    {
        "question": "Какие операторы используются для логического соединения условий в SQL?",
        "options": [
            "a) AND, OR, NOT",
            "b) LIKE, BETWEEN, IN",
            "c) JOIN, ON, USING",
            "d) UNION, INTERSECT, EXCEPT"
        ],
        "answer": "a"
    },
    {
        "question": "Что делает команда `LIKE` в SQL?",
        "options": [
            "a) Ищет точное соответствие значений",
            "b) Ищет значения в диапазоне",
            "c) Ищет значения, подходящие по шаблону",
            "d) Ищет значения, которые не встречаются"
        ],
        "answer": "c"
    },
    {
        "question": "Какие ключевые слова используются для управления транзакциями в SQL?",
        "options": [
            "a) BEGIN, COMMIT, ROLLBACK",
            "b) START, END, CANCEL",
            "c) CREATE, ALTER, DROP",
            "d) SAVE, LOAD, UNDO"
        ],
        "answer": "a"
    },
    {
        "question": "Какие операторы используются для обновления данных в SQL?",
        "options": [
            "a) UPDATE, INSERT, DELETE",
            "b) SELECT, FROM, WHERE",
            "c) ADD, MODIFY, REMOVE",
            "d) ALTER, DROP, CREATE"
        ],
        "answer": "a"
    },
    {
        "question": "Что такое транзакция в контексте баз данных?",
        "options": [
            "a) Одновременное выполнение нескольких запросов",
            "b) Операция или набор операций, которые должны быть выполнены атомарно",
            "c) Вывод данных на экран",
            "d) Подключение к базе данных"
        ],
        "answer": "b"
    },
    {
        "question": "Какие операторы используются для удаления данных в SQL?",
        "options": [
            "a) DELETE, DROP, TRUNCATE",
            "b) SELECT, FROM, WHERE",
            "c) ADD, MODIFY, REMOVE",
            "d) UPDATE, INSERT, DELETE"
        ],
        "answer": "a"
    },
    {
        "question": "Какое предназначение у команды `TRUNCATE TABLE` в SQL?",
        "options": [
            "a) Удаляет все данные из таблицы, но оставляет структуру",
            "b) Удаляет структуру таблицы",
            "c) Удаляет только первую запись в таблице",
            "d) Обновляет все данные в таблице"
        ],
        "answer": "a"
    },
    {
        "question": "Какие операторы используются для изменения структуры таблиц в SQL?",
        "options": [
            "a) ADD, MODIFY, REMOVE",
            "b) SELECT, FROM, WHERE",
            "c) UPDATE, INSERT, DELETE",
            "d) CREATE, DROP, ALTER"
        ],
        "answer": "d"
    },
    {
        "question": "Какие типы индексов могут использоваться в MySQL?",
        "options": [
            "a) Уникальный и неуникальный",
            "b) Скалярный и векторный",
            "c) Временной и постоянный",
            "d) Первичный и внешний"
        ],
        "answer": "a"
    },
    {
        "question": "Что такое внешний ключ (foreign key) в контексте баз данных?",
        "options": [
            "a) Уникальный индекс для ускорения поиска",
            "b) Колонка, которая ссылается на другую таблицу",
            "c) Уникальное поле, которое идентифицирует каждую запись в таблице",
            "d) Индекс, который разрешает дубликаты значений"
        ],
        "answer": "b"
    },
    {
        "question": "Какие функции агрегации данных поддерживаются в MySQL?",
        "options": [
            "a) COUNT, SUM, AVG, MAX, MIN",
            "b) ADD, SUBTRACT, MULTIPLY, DIVIDE",
            "c) SELECT, FROM, WHERE",
            "d) UPDATE, INSERT, DELETE"
        ],
        "answer": "a"
    },
    {
        "question": "Что такое процедура в MySQL?",
        "options": [
            "a) Специальный вид таблицы",
            "b) Функция для агрегации данных",
            "c) Набор инструкций, выполняемых в определенном порядке",
            "d) Индекс для ускорения поиска"
        ],
        "answer": "c"
    },
    {
        "question": "Какие типы соединений поддерживаются в SQL?",
        "options": [
            "a) Внутреннее, левое, правое и полное",
            "b) Внешнее и внутреннее",
            "c) Левое, правое и внешнее",
            "d) Левое и правое"
        ],
        "answer": "a"
    },
    {
        "question": "Какие операторы используются для объединения таблиц в SQL?",
        "options": [
            "a) JOIN, ON, USING",
            "b) LIKE, BETWEEN, IN",
            "c) SELECT, FROM, WHERE",
            "d) UNION, INTERSECT, EXCEPT"
        ],
        "answer": "a"
    },
    {
        "question": "Какие операторы используются для создания и изменения данных в SQL?",
        "options": [
            "a) SELECT, FROM, WHERE",
            "b) ADD, MODIFY, REMOVE",
            "c) UPDATE, INSERT, DELETE",
            "d) CREATE, DROP, ALTER"
        ],
        "answer": "d"
    },
    {
        "question": "Что делает оператор `ALTER TABLE` в SQL?",
        "options": [
            "a) Создает новую таблицу",
            "b) Изменяет структуру существующей таблицы",
            "c) Удаляет данные из таблицы",
            "d) Объединяет таблицы"
        ],
        "answer": "b"
    },
    {
        "question": "Какие типы данных могут использоваться в MySQL?",
        "options": [
            "a) Числовые, текстовые, дата и время и другие",
            "b) Логические и целочисленные",
            "c) Одномерные и многомерные",
            "d) Скалярные и векторные"
        ],
        "answer": "a"
    },
    {
        "question": "Что такое триггер в контексте баз данных?",
        "options": [
            "a) Специальный вид запроса",
            "b) Процедура, автоматически запускаемая при определенных событиях",
            "c) Функция для агрегации данных",
            "d) Индекс для ускорения поиска"
        ],
        "answer": "b"
    },
    {
        "question": "Какие ключевые слова используются для управления доступом к данным в SQL?",
        "options": [
            "a) GRANT и REVOKE",
            "b) CREATE и DROP",
            "c) SELECT и INSERT",
            "d) BEGIN и COMMIT"
        ],
        "answer": "a"
    },
    {
        "question": "Какие операторы используются для сортировки данных в SQL?",
        "options": [
            "a) SORT BY",
            "b) GROUP BY",
            "c) ORDER BY",
            "d) SORT"
        ],
        "answer": "c"
    },
    {
        "question": "Что делает оператор `HAVING` в SQL?",
        "options": [
            "a) Определяет условие для группировки данных",
            "b) Фильтрует строки по указанному условию",
            "c) Удаляет данные из таблицы",
            "d) Объединяет таблицы"
        ],
        "answer": "a"
    },
    {
        "question": "Какие функции используются для работы с строками в SQL?",
        "options": [
            "a) LEN, LOWER, UPPER",
            "b) COUNT, SUM, AVG",
            "c) LIKE, NOT LIKE",
            "d) TRIM, CONCAT, SUBSTRING"
        ],
        "answer": "d"
    },
]

score = 0

for index, question in enumerate(questions):
    print(f"Вопрос {index + 1}: {question['question']}")
    for option in question['options']:
        print(option)
    user_answer = input("Введите ваш ответ (a, b, c или d): ").strip().lower()
    if user_answer == question['answer']:
        print("Правильно!\n")
        score += 1
    else:
        print(f"Неправильно. Правильный ответ: {question['answer']}\n")

print(f"Вы ответили правильно на {score} из {len(questions)} вопросов.")
