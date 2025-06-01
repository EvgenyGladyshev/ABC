import numpy as np
import pandas as pd

# Считываем excel файл с данными 
df = pd.read_excel('data.xlsx', sheet_name='data')
# Форматируем числа float формата
pd.set_option('display.float_format', '{:.2f}'.format)

# Группируем по количеству, закупочной и розничной цене
df = df.groupby('dr_ndrugs')[['dr_kol', 'dr_czak', 'dr_croz']].agg('sum').reset_index()# Переводим в группы каждую метрику:
# По правилу Парето - группа "А" от 0 до 80%, "В" от 80 до 95% и "С" больше 95%

# Сначала посчитаем прибыль

# Прибыль = розничная цена * количество покупок / сумма (розничная цена * количество покупок)
df['revenue'] = df['dr_croz']*df['dr_kol']/sum(df['dr_croz']*df['dr_kol'])

# Отсортировали в порядке убывания, чтобы посчитать нарастающий итог
df = df.sort_values('revenue', ascending=False)
df['cumsum_revenue'] = df['revenue'].cumsum()

# Отнесли каждый товар в свою группу
df['abc_revenue'] = np.where(df['cumsum_revenue']<=0.8,'A',np.where(df['cumsum_revenue']<=0.95,'B','C'))

# Посчитаем количество проданных товаров

# Количество проданных товаров - количество проданного товара на общее количество проданных товаров
df['amount'] = df['dr_kol']/sum(df['dr_kol'])

# Отсортировали в порядке убывания, чтобы посчитать нарастающий итог
df = df.sort_values('amount', ascending=False)
df['cumsum_amount'] = df['amount'].cumsum()

# Отнесли каждый товар в свою группу
df['abc_amount'] = np.where(df['cumsum_amount']<=0.8,'A',np.where(df['cumsum_amount']<=0.95,'B','C'))

# Считаем маржинальность (в процентах)

# Сначала посчитаем выручку с каждого товара
# Вычитаем из розничной цены закупочную цену и делим на розничную цену
df['profit'] = (df['dr_croz'] - df['dr_czak'])/df['dr_croz']

# Маржинальность - выручка с одного товара на общую выручку
df['margin'] = df['profit']/sum(df['profit'])

# Отсортировали в порядке убывания, чтобы посчитать нарастающий итог
df = df.sort_values('margin', ascending=False)
df['cumsum_margin'] = df['margin'].cumsum()

# Отнесли каждый товар в свою группу
df['abc_margin'] = np.where(df['cumsum_margin']<=0.8,'A',np.where(df['cumsum_margin']<=0.95,'B','C'))

# Объединяем группы по трем метрикам
df['abc'] = df['abc_revenue'] + df['abc_amount'] + df['abc_margin']

# Сортируем по группам
df = df.sort_values('abc')

# Оставляем только нужные столбцы
df = df[['dr_ndrugs', 'dr_kol', 'dr_czak', 'dr_croz', 'abc_revenue', 'abc_amount', 'abc_margin', 'abc']]

print(df)