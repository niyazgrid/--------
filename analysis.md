# Анализ задачи сбора данных с quotes.toscrape.com

# Что было сделано
Собраны цитаты с сайта https://quotes.toscrape.com/. Данные были сохранены в формате JSON для дальнейшего использования.

# Откуда были получены данные
Данные были получены с веб-сайта https://quotes.toscrape.com/, который предназначен для практики веб-скрейпинга.

# Как осуществлялся сбор
Сбор данных осуществлялся с использованием библиотеки Python Requests для HTTP-запросов и BeautifulSoup для разбора HTML-кода страницы. Я обошел все страницы с цитатами, извлекал текст цитаты и имя автора, после чего сохранял эту информацию в виде списка словарей.

# Почему был выбран тот или иной метод/инструмент
Выбор библиотек `Requests` и `BeautifulSoup` был обусловлен их простотой и мощностью в обработке HTML-контента. Эти библиотеки широко используются для веб-скрейпинга и хорошо документированы, что упрощает процесс разработки.
