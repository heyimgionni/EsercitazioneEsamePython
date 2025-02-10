'''

3)
realizzare encoder e decoder di stringhe in cui l'econding avviene sostituendo
 a un carattere il carattere ASCII corrispondente+1

'''

# chr --> restituisce il carattere associato al codice ascii invece 
# ord converte il carattere in un integer

def encoder(s):
    result = ""
    for c in s: 
        result+= chr(ord(c) + 1) 
    return result
def decoder(s):
    result = ""
    for c in s: 
        result+= chr(ord(c) - 1)
    return result


encode_s = encoder("ciao")
decode_s = decoder(encode_s)
print(encode_s)
print(decode_s)