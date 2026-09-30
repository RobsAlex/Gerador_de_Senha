import random
import string
print("---- GERADOR DE SENHAS ----")
caracteres = string.ascii_letters + string.digits + string.punctuation
tamanho = int(input("Digite a quantidade de caracteres da senha:"))
senha = "".join(random.choice(caracteres) for _ in range(tamanho))
print(f"\nsua senha gerada foi: {senha}")