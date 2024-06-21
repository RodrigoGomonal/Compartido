rut = 0
multiplicador = 2
suma_multicada = 0
total = 0
totalsum = 0

while True:
  rut = input('Ingrese rut sin DV ').strip()
  if rut.isnumeric() == True:
    if len(rut) == 8: #* Verifica el largo del rut
      for i in reversed(rut): #* Invierte el rut
        if multiplicador == 8: multiplicador = 2 #* reinicia el numero con el que se multiplica
        suma_multicada = int(i) * multiplicador #* multiplica un numero del rut por un numero
        totalsum+= suma_multicada #* suma los numero del rut multiplicados
        multiplicador+= 1 #* autoincrementa el numero multiplicador
      totalrut = totalsum #* guardas la suma total multiplicada en una nueva variable
      totalsum = totalsum/11 #* divides la S.T multiplicada por 11
      total = int(totalsum) * 11 #* el resultado de lo anterior se multiplica por 11
      total = totalrut - total #* luego restas el resultado anterior por la suma total multiplicada
      total = 11 - total #* el resultado anterior se resta por 11
      if total == 11: total = 0
      elif total == 10:
        total = str(total)
        total = 'K'
      print(f'{rut}-{total}')
      break
    else: print('Error, largo debe ser 8')
  else: print('Error, ingrese numeros')
