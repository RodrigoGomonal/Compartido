rut = 0
rutrev = 0
num = 2
suma = 0
total = 0
totalsum = 0

while True:
  rut = input('Ingrese rut sin DV ').strip()
  if rut.isnumeric() == True:
    if len(rut) == 8:
      rutrev = rut[::-1]
      for i in range(len(rutrev)): #reverse()
        if num == 8:
          num = 2
        suma = int(rutrev[i]) * num
        totalsum+= suma
        print(rutrev[i],num, suma, totalsum)
        num+= 1
      totalrut = totalsum
      totalsum = totalsum/11
      total = int(totalsum) * 11
      print(total)
      total = totalrut - total
      total = 11 - total
      if total == 11:
        total = 0
      elif total == 10:
        total = str(total)
        total = 'K'
      print(rut,'-',total)
      break
    else: print('Error, largo debe ser 8')
  else: print('Error, ingrese numeros')