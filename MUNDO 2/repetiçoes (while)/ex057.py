sexo = str(input('qual seu sexo?:')).upper()[0].strip()
while sexo not in "MmFf":
    sexo = str(input('qual seu sexo?: ')).strip().upper()[0]
print('fim')