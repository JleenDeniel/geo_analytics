<h1> Задание на построение модели машинного обучения, которая предсказывает некоторую географическую характеристику поверхности</h1>
Этапы:

1. Отбор признаков среди почти сотни с помощью feature importance

2. Отбор признаков с помощью статистики
3. Генерация новых признаков
4. Подбор оптимальных гиперпараметров для градиентого бустинга
5. Валидация 
6. Тестирование еще одного решения (ARIMA)
7. Сравнение результатов
8. Выводы
9. Итоговый расчет
10. Визуализация

Важно:
1. Не все гексагоны из таргета матчатся с "историческими" данными, я предположил что для них можно построить отдельную модель которая будет учитывать веса соседей, удаленность от центра города и тому подобное, либо же просто прогнозировать их авторегрессией, но факт отсутствия данных меня немного напряг, тем более в задании вообще сказано пресказывать тех у кого dt пустое, а таких данных в принципе нет, есть только с пропущенным pred 
2. Были найдены гексагоны с констатным таргетом, их целевое значение заполнено этой константой
3. Ход всех мыслей при решении и путь к построению модели содержится в ноутбуке по пути notebooks/experiment.ipynb
4. Ноутбуки также повторены в формате html для удобства
5. В основном задание выполнено, хочется сделать скрипты для обучения и инференса модели и прикрутить докер, но это в процессе
6. Визуализация в ноутбке не заработала, поэтому сделал ее на сайте и сохранил в notebook/visualisation/kepler.gl.html 