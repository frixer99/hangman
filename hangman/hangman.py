import random

def decode_word(guess_letter, secret_word, code_word):
    index = 0
    code_list = list(code_word)
    for letter in secret_word:
        if guess_letter == letter:
            code_list[index] = guess_letter
        index += 1
    new_code_word = "".join(code_list)
    return new_code_word

def codf_word(word):
    count = 0
    new_word = ""
    for letter in word:
        if letter == word[0]:
            new_word = word.replace(letter,"*")
            count += 1
        else:
            new_word = new_word.replace(letter,"*")
            count += 1
    return new_word


word_list = [
"cadeira", "mesa", "lapis", "caneta", "computador",
"livro", "caderno", "calculadora", "rato", "telefone",
"mochila", "borracha", "monitor", "teclado", "folha",
"tesoura", "capa", "agrafador", "cola"
]
secret_word = random.choice(word_list)
print(secret_word)
code_word = codf_word(secret_word)

print("Este e um jogo da forca. As palavras estao em portugues, \
todas minusculas e sem acentos. Boa sorte!")
print("A palavra secreta é: " + code_word)
guess_letter = input("Letra: ")
guess_word = code_word
bad_tries = 0

while guess_word != secret_word and bad_tries < 7:
    if len(guess_letter) == 1:
        if guess_letter in secret_word: #se a palavra tiver a letra
            guess_word = decode_word(guess_letter, secret_word, guess_word)
            if guess_word == secret_word:
                print("Parabens! Acertaste na palavra!")
            else:
                print("Muito bem! A palavra secreta e: " + guess_word)
                guess_letter = input("Letra: ") 
            
        else: #se a palavra nao tiver a Letra
            bad_tries += 1
            if bad_tries == 7:
                print("Perdeste o jogo. A palavra era " + secret_word)
            else:
                print("Nao ha essa letra na palavra. Tenta outra vez.") 
                guess_letter = input("Letra: ")
    else:
        guess_letter = input("Introduz apenas uma letra: ")
