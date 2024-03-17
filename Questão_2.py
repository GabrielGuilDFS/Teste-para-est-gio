def fibonacci_sequen(n):
    fib_sequen = [0, 1]
    while fib_sequen[-1] < n:
        prox_fib = fib_sequen[-1] + fib_sequen[-2]
        fib_sequen.append(prox_fib)
    return fib_sequen

def verif_pertenc(numero, fib_sequen):
    if numero in fib_sequen:
        return f"O numero {numero} pertence à sequência de Fibonacci."
    else:
        return f"O numero {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um numero para verificar se pertence a sequencia de Fibonacci: "))

sequen_fibonacci = fibonacci_sequen(numero)
print(verif_pertenc(numero, sequen_fibonacci))