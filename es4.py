'''
Calcolare i divisori di un numero assegnato
'''

def calc_divider(n):
    list_divider = [divide for divide in range(1,n+1) if n % divide == 0 ]
    return list_divider

print(calc_divider(36))