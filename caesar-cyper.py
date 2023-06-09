import fasttext
model = fasttext.load_model('../lid.176.bin')

# Uses the FastText "lid.176" language identification model to detect the language of a given text.
def detectarIdioma(texto): 
    previsao = model.predict(texto)  # Prediction of the language
    idioma, probabilidade = previsao  # The prediction returns both the language and a probability
    idioma = (''.join(idioma)).replace('__label__','')  # The language comes with the prefix "__label__", this line removes it
    if(probabilidade > 0.85):  # If the probability of the language is more than 85%, the function returns the detected language
        return idioma
    else:
        return 0
    
# Shifts a given letter by a certain amount, according to the Caesar cipher rule.
def somar_letras(letra, deslocamento):
    valor_letra = ord(letra.lower())  # Get the numeric ASCII value of the lowercase letter
    novo_valor = (valor_letra - ord('a') + deslocamento) % 26  # Calculate the new ASCII value by shifting it and using modulo 26 to handle overflow (wrap around Z back to A)
    nova_letra = chr(novo_valor + ord('a'))  # Convert the numeric value back to a letter
    return nova_letra

# Decodes a given Caesar cipher-encoded text by brute force.
def cifraDecoder(texto_codificado):
    decode = ''  
    codificado = list(texto_codificado)  # Transform the input text into a list, allowing the program to operate with each character individually
    for cont in range (0, 26):  # Try all 26 possible shifts (one for each letter of the alphabet)
        for letras in codificado: 
            if(letras == ' '):  # If the character is a space, it won't be shifted
                decode = (decode + ' ')
            else:
                decode = (decode + somar_letras(letras, cont))  # If it's a letter, it gets shifted
        else:
            if detectarIdioma(decode) != 0:  # If the function doesn't return 0, it will keep trying to decode
                idioma = detectarIdioma(decode)
                print('\nResultado Encontrado!\n')
                print('cifra de ordem: {}\nresultado: {}\nidioma: {}\n'.format(cont,decode,idioma)) # Returns the order of the cipher, the result and the recognized language
                break
            else: print('cifra de ordem: {}, resultado: {}, idioma: N/A'.format(cont,decode))  # If the decoded text is not recognized as a valid language, it will print "Não identificado" for the language.
            decode = ''  # If the decoded text is not recognized as a valid language, the decode variable is reset, and the loop continues with the next shift

texto_codificado = input("insira o texto a ser decodificado: ")  # User input for the encoded text
cifraDecoder(texto_codificado)  # Call the function with the user input
