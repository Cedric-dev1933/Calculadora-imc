#Calculadora IMC

# Validação peso
while True:
    try:
        peso = float(input("Digite seu peso: "))
        if peso <= 0:
            print("Por favor, digite um peso maior do que 0")
            continue
        break
    except ValueError:
        print("Valor inválido. Digite um número para o peso")

# Validação altura
while True:
    try:
        altura = float(input("Digite sua altura: "))
        altura = altura/100 # Convertendo a altura de CM para metros
        if altura <= 0:
            print("Por favor, digite uma altura maior do que 0")
            continue
        break
    except ValueError:
        print("Valor inválido. Por favor digite um número para a altura")


#Cálculo IMC        
imc = peso/altura ** 2
print(f"Seu IMC é: {imc:.1f}")

# Categoria do IMC
if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")     
elif imc < 30.0:
    print("Sobrepeso")    
else:
    print("Obesidade")  

