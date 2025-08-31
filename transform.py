import pandas as pd

gold = pd.read_csv('files/XAU_USD.csv')
gold['Data'] = pd.to_datetime(gold['Data'], dayfirst=True)

(gold
    .assign(Ano=lambda x: x['Data'].dt.year)
    .astype({'Último': str})
    .assign(Último=lambda x: x['Último'].str.replace('.', '').str.replace(',', '.'))
    .filter(items=['Data', 'Último', 'Ano'])
    .astype({'Último': 'float64'})
    .groupby('Ano')
    .mean()
    .reset_index()
    .to_csv('files/gold_price.csv')
)