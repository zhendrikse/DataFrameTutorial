import pandas as pd

data = {'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}

purchases = pd.DataFrame(data)
print(purchases)

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)
purchases.loc['June']

purchases.to_csv('my_test_data.csv')
purchases.to_json('my_test_data.json')
# purchases.to_sql('my_test_data.sql')

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
print(movies_df.head())
print(movies_df.tail(2))
print(movies_df.info())
print(movies_df.shape)
