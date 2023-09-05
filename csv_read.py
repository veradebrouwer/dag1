print("Start met CSV uitlees applicatie")

import pandas

df = pandas.read_csv('pokemon.csv')

# print(df['Name'])

for r, rij in df.iterrows():
    # print(rij['Name'])
    print("De naam van de pokemon is " + rij['Name'])