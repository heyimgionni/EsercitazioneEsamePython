'''

3)
Leggere da un file di testo (nella forma 
nome1
nome2
nome3
)
e indicare quale nome è il più lungo e da quanti caratteri è formato

'''

list_names = open("nomi.txt").read().splitlines()
def find_longest_name(list_name):
    longest_name = ""
    for name in list_name:
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name

longest_name = find_longest_name(list_names)
longest_name_lenght = len(longest_name)
print(f"The longest name is {longest_name} and the lenght is {longest_name_lenght}")