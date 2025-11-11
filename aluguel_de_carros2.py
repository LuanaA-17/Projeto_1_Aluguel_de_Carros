carro =input("qual o modelo do carro: ")
dias =float(input("quantos dias o carro foi alugado: "))
km =float(input("quantos km voce rodou: "))

if carro == 'gol':
    diaria = 80

elif carro == "fusca":
    diaria = 50

elif carro == "voyage":
    diaria = 78

elif carro == "dodge ram":
    diaria = 90

else:
    diaria=60

total_dias =dias*diaria
total_km =km*0.15
valor_total =total_dias+total_km
print(f"voce andou {km} por {dias} então o preço a pagar é {valor_total}: ")

