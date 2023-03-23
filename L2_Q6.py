import random
quantidade = list(random.sample(range(1, 101), 20))
price = list(random.sample(range(1, 101), 20))
faturamento = []
for q, p in zip(quantidade, price):
    faturamento.append(q*p)
faturamento_total = sum(faturamento)
media = faturamento_total / len(faturamento)
faturamento_abaixo_media = []
for i in faturamento:
    if i < media:
        faturamento_abaixo_media.append(i)
print(f'O faturamento é : {faturamento}.\nO faturamento total dos produtos é {faturamento_total}.\nA média de faturamento é {media}.\nE o número de faturamentos abaixo da média é {len(faturamento_abaixo_media)}.')