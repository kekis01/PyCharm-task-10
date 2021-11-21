# PyCharm-task-10

## Профилизатор

Результат профилировщика filter.py:

![Профилизатор filter](https://github.com/kekis01/PyCharm-task-10/blob/main/prof_img/prof_filter.png)

Результат профилировщика old_filter.py:

![Профилизатор old_filter](https://github.com/kekis01/PyCharm-task-10/blob/main/prof_img/prof_old_filter.png)

Можно заметить, что новый файл с отредактированным кодом 
быстрее, чем старый. Даже с учетом ввода данных, новый код работает быстрее,
так как в нем не происходит переполнение, выделены методы и использована
библиотека numpy.

Результат профилировщика file_with_filename.py:

![Профилизатор file_with_filename](https://github.com/kekis01/PyCharm-task-10/blob/main/prof_img/prof_filter_with_filename.png)

Время заметно сократилось. Из полученных данных можно сделать вывод, 
что большая часть времени затрачивается на ввод данных. Без ввода
он работает в разы быстрее обычного.

## Изображения

До:

![img](https://github.com/kekis01/PyCharm-task-10/blob/main/img2.jpg)

После filter.py:

![filter_img](https://github.com/kekis01/PyCharm-task-10/blob/main/res_filter.jpg)

После old_filter.py:

![old_filter_img](https://github.com/kekis01/PyCharm-task-10/blob/main/res.jpg)

После filter_with_filename.py:

![filter_with_filename_img](https://github.com/kekis01/PyCharm-task-10/blob/main/res_filename.jpg)

## Тесты

Для второго модуля не смог сделать тест, так как метод не возвращает
никакой элемент. Тесты для первого метода работают корректно.

![doc_test](https://github.com/kekis01/PyCharm-task-10/blob/main/doc_img/doc_tests.png)

![error](https://github.com/kekis01/PyCharm-task-10/blob/main/doc_img/test_error.png)

## Отладчик

Значения переменных из дебагера:

![Debugger](https://github.com/kekis01/PyCharm-task-10/blob/main/debugger.png)

