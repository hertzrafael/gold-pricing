import pandas as pd

gold = pd.read_csv('files/XAU_USD.csv')
gold['Data'] = pd.to_datetime(gold['Data'], dayfirst=True)

(gold
    .assign(
        Ano=lambda x: x['Data'].dt.year,
        Mes=lambda x: x['Data'].dt.month
    )
    .astype({'Último': str})
    .query(f'Ano >= 2007 & Ano <= 2022')
    .assign(Último=lambda x: x['Último'].str.replace('.', '').str.replace(',', '.'))
    .filter(items=['Data', 'Último', 'Ano', 'Mes'])
    .astype({'Último': 'float64'})
    .groupby(['Ano', 'Mes'])
    .mean()
    .reset_index()
    .to_csv('files/gold_price_monthly.csv', index=False)
)