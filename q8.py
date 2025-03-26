palavra = input("Digite uma palavra: ")

def eh_palindromo(palavra):
    return palavra == palavra[::-1]  # Compara a palavra original com sua inversa


print(eh_palindromo(palavra))  # Saída: True


