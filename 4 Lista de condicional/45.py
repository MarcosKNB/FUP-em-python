def funcao(texto, deslocamento):
    resultado = ''

    for char in texto:
        if char.isalpha():
            maiuscula = char.isupper()
            char = char.upper()

            novo_indice = ord(char) + deslocamento
            if novo_indice > ord('Z'):
                novo_indice -= 26

            novo_char = chr(novo_indice)
            if not maiuscula:
                novo_char = novo_char.lower()

            resultado += novo_char
        else:
            resultado += char

    return resultado