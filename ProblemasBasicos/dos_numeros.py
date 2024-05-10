a = input('')
b = input('')

print(a,b, sep='+', end='=')
suma: int = int(a) + int(b)
print(suma) 

print(a,b, sep='-', end='=')
resta: int = int(a) - int(b)
print(resta)

print(a, b, sep='*',end='=')
mult: int = int(a)*int(b)
print(mult)

print(a, b, sep='/', end='=')
div: float = round(float(a) / float(b), 1)
print(div)