# gold-pricing
Trabalho da disciplina de Econometria que visa precificar o ouro, utilizando regressão linear múltipla, levando em conta as variáveis NYSE Index e IPC dos EUA.


# Anotações

- R² = 67%, nível de correlação entre IPC e Indice NYSE = 90%. Durbin-Watson = 1.131
- Teste VIF apresentou alta multicolinearidade entre as variáveis explicativas (5,79 em ambas).
- Remoção do Índice NYSE e substituindo por VIX (CBOE Volatility Index).
- Dados de produção, aumentar a quantidade de observações dos dados (recomendado diários)
- Corrigindo banco de dados para dados mensais.

