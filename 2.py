
edades = [10,15,50,30,40,50,22,33,44,66]
mayores_de_60 =[]
de_cero_20 = []
de_20_30 = []
de_30_40 = []
de_40_60 = []
for i in edades:
    if i > 60:
        mayores_de_60.append(i)
    elif i > 40:
        de_40_60.append(i)
    elif i > 30:
        de_30_40.append(i)
    elif i > 20:
        de_20_30.append(i)
    else:
        de_cero_20.append(i)

print(f"Mayores de 60: {mayores_de_60},De 40 a 60: {de_40_60},"
      f"De 30 a 40: {de_30_40},De 20 a 30: {de_20_30},"
      f"De cero a 20: {de_cero_20}")