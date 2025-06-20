# Описание задачи

В аптечной сети представлено множество товаров, но не все из них вносят одинаковый вклад: некоторые товары могут занимать значительную долю в запасах, но иметь низкую оборачиваемость, другие же зависят от сезона и т.д.
Поэтому необходимо контролировать запасы и обновлять ассортимент.

## Что было сделано

Мной было предложено провести ABC-анализ:
1. Собраны данные о покупках, доходах и прибыли.
2. Проведён расчёт каждого товара по ключевым метрикам.
3. Составлены бизнес-выводы на основе анализа для оптимизации ассортимента и управления запасами.

В репозиторий я включил:
- [Исходных данныe](https://github.com/EvgenyGladyshev/ABC/blob/master/data.xlsx) (`excel` файл нужно скачать)
- [Код для проведения ABC-анализа с помощью Pandas](https://github.com/EvgenyGladyshev/ABC/blob/master/abc_analysis.py)
- [График распределения по группам](https://github.com/EvgenyGladyshev/ABC/blob/master/treemap.png)
- [Бизнес-выводы и рекомендации](https://github.com/EvgenyGladyshev/ABC/blob/master/insights.md)

# Запуск скрипта

```sh
# Создаем виртуальное окружение
python -m venv abc_analysis

# Активируем виртуальное окружение
./abc_analysis/scripts/activate # source abc_analysis/bin/activate для Linux

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем скрипт
python abc_analysis.py
```