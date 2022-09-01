# Lista de tuplas
vendas_produtos = [
    ('iphone', 558147, 951642),
    ('galaxy', 712350, 244295),
    ('ipad', 573823, 26964),
    ('tv', 405252, 787604),
    ('máquina de café', 718654, 867660),
    ('kindle', 531580, 78830),
    ('geladeira', 973139, 710331),
    ('adega', 892292, 646016),
    ('notebook dell', 422760, 694913),
    ('notebook hp', 154753, 539704),
    ('notebook asus', 887061, 324831),
    ('microsoft surface', 438508, 667179),
    ('webcam', 237467, 295633),
    ('caixa de som', 489705, 725316),
    ('microfone', 328311, 644622),
    ('câmera canon', 591120, 994303)
]

# Cabeçalho do relatório
print("-" * 85)
print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(
    "PRODUTO", "VENDAS 2019", "VENDAS 2020", "CRESCIMENTO"))
print("-" * 85)

for produto, vendas2019, vendas2020 in vendas_produtos:
    # Cálculo do crescimento percentual
    crescimento = (vendas2020 / vendas2019) - 1

    if vendas2020 > vendas2019:
        crescimento = "{:.2%} 🔼".format(crescimento)
    else:
        crescimento = "{:.2%} 🔽".format(crescimento)

    # Formatação dos valores
    vendas2019 = "R${:_.2f}".format(
        vendas2019).replace(",", ".").replace("_", ".")
    vendas2020 = "R${:_.2f}".format(
        vendas2020).replace(",", ".").replace("_", ".")

    # Exibição do resultado
    print("|{:<20}|{:^20}|{:^20}|{:^20}|".format(
        produto, vendas2019, vendas2020, crescimento))

# Rodapé do relatório
print("-" * 85)
