def count_letter_a(s):
    count = s.lower().count("a")
    if count > 0:
        return f"A letra 'a' (maiúscula ou minúscula) ocorre {count} vezes na string."
    else:
        return "A letra 'a' (maiúscula ou minúscula) não foi encontrada na string."


input_string = input("Informe uma string para verificar a existência da letra 'a': ")
result = count_letter_a(input_string)
print(result)
