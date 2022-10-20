def freq(text):
    n = len(text)
    nb_occ = [0] * 26
    res = [0] * 26
    nb_carac = 0
    for i in range(n):
        carac = text[i]
        if carac.isalpha():
            nb_occ[ord(carac) % 65] += 1
            nb_carac += 1


text = str(input())
text_maj = text.upper()
print(freq(text_maj))
