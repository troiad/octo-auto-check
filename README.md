# octo-auto-check

Что нужно для работы:
1. Python 3.9+
2. PyCharm - для нормального запуска, отладки, и правки кода

Пошаговый алгоритм (делается только 1 раз, не пугайтесь):
1. Устанавливаем Python 3.9+ с официального сайта
2. Устанавливаем PyCharm
3. Скачиваем и распаковываем архив с octo-auto-check в папку PycharmProjects
4. Должен получится примерно такой путь: /Users/mac/PycharmProjects/octo-auto-check/
5. Создаем внутри папки /octo-auto-check/ новую папку с названием 1
6. Вбиваем в гугл "chromedriver chrome version 96", скачиваем chromedriver, и загружаем его в папку 1
7. Открываем проект в PyCharm
8. Импортируем все библиотеки, которые указаны вверху main.py.
В PyCharm-е для этого достаточно навести мышкой на подчеркнутое красным название библиотеки, и нажать Импорт
6. Дополнительно устанавливаем "webdriver-manager" через Pycharm -> Настройки -> Python Interpreter -> жмем на плюсик -> вставляем название пакета webdriver-manager
7. Создаем папку "~auto", внутри главной директории /Users/mac/
8. Возращаемся в проект, и вставляем API ключ от вашего Octo Browser в поле  <API_TOKEN>
9. Запускаем Octo Browser
10. Вносим изменения в названия аккаунтов которые вы хотите пропустить через скрипт. Например, добавляете к названию приставку #check
11. Можно запускать программу
12. Вы увидите надпись "Введите ключевое слово для аккаунтов: " - вбиваем наше ключевое слово #check
13. PROFIT!

FAQ:
1. Какие аккаунты будет запускать программа?
- Мы подаем запрос на АПИ такого вида: "найди мне все айди профайлов, у которых в названии присутствует "{ваше_ключевое_слово}". Получаем список айди, и программа по очереди начинает запускать их и выполнять скрипт.
2. Что делать если выбивает ошибку "debug_info"?
- Закрываем/открываем Окто, и пробуем снова :) Скорее всего залагала синхронизация профиля, и окто не дает вам запустить профайл.
3. Что делать с ошибкой HTTPConnect....?
- Попробуйте изменить в коде программы номер порта. Я использую 58888, вам возможно нужен 58878 порт.
4. Что делать если не получается загрузить фото? Скрипт прыгает не в ту папку
- Т.к загрузка фото происходит через передачу нажатий клавиш клавиатуры во время открытия окна проводника - возможны нюансы. Вам нужно поменять количество keyboard.press / realease функций в коде.
 Открываете браузерный профайл, жмете загрузить фото на любом сайте (например imgur), и считаете сколько раз вам нужно сделать нажатий стрелочек вправо-влево-вверх-вниз, чтобы попасть в нужную директорию. Посчитали, записали, поменяли код - и запускаете программу.
Надеюсь в скором времени прикручу загрузку фото по post/get запросам, и эта проблема уйдет.
5. Программа не ворует аккаунты/токены/логины_пароли?
- Все прозрачно. Перед вами открытый код, и можете сами посмотреть что никаких запросов на сторонние ресурсы не подается. Программа использует официальные библиотеки, запускается у вас на локальной машине.
6. Можно ли подправить программу под свои нужды/цели? Или поправить твои костыли?
- Конечно можно, это же opensource. Буду рад если вы сможете использовать этот скрипт как скелет для своих задач.
 Если вы можете поправить мои костыли, чтобы программа работала лучше/сильнее/быстрее буду вам только признателен, и жду в личке :)
