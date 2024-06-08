def es_palindromo(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]
