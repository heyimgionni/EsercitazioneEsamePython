'''
2)
visualizzare tutte le versioni di una stringa assegnata come parametro e
 ottenuta come rotazione dei caratteri della stringa stessa.
Produrre un file di log dei risultati ottenuti

# come funziona --> rotazioni 

abc è la string 
prima rotazione --> bca
seconda rotazione --> cba

'''

def rotate_string(s):
    list_rotation = [] # we create an empty list
    for i in range(len(s)): # for len of the string
        list_rotation.append(s[i:] + s[:i]) # we append the first char to last position
    with open('rotation.txt' , 'w') as f: # we open a file ( if doesn't exist it will create the file on the root) and open in write mode 
        for line in list_rotation: 
            f.write(line)
            f.write('\n')
    return list_rotation

print(rotate_string('ciao'))