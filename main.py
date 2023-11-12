# Função para gerar a chave a partir da palavra-chave e do texto original
def gerar_chave(texto, palavra_chave):
  palavra_chave = list(palavra_chave)
  if len(texto) == len(palavra_chave):
    return(palavra_chave)
  else:
    for i in range(len(texto) - len(palavra_chave)):
      palavra_chave.append(palavra_chave[i % len(palavra_chave)])
  return("".join(palavra_chave))

# Função para criptografar o texto usando a chave
def criptografar(texto, chave):
  texto_cifrado = []
  for i in range(len(texto)):
    letra = texto[i]
    k = ord(chave[i]) - ord('A')
    texto_cifrado.append(chr((ord(letra) - ord('A') + k) % 26 + ord('A')))
  return("".join(texto_cifrado))

# Pedir ao usuário que digite o texto original
texto = input("Digite o texto original: ")

# Gerar a chave usando a palavra-chave TESSOFTHEDURBERVILLES
palavra_chave = input("Digite a palavra chave: ")
chave = gerar_chave(texto, palavra_chave)

# Criptografar o texto usando a chave
texto_cifrado = criptografar(texto, chave)

# Salvar o texto cifrado em um arquivo chamado vigenere.cipher
with open("vigenere.cipher", "w") as arquivo:
  arquivo.write(texto_cifrado)

# Imprimir o texto original e o texto cifrado
print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
