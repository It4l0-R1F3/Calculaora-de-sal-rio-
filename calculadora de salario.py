sal_mensal = int(input("Quanto foi o seu salário deste mes?"))

gastos = int(input('gastos deste mes:'))

if gastos > sal_mensal:
    print('hoou,voce deve',sal_mensal-gastos,'RS neste mes')
 
elif gastos == sal_mensal:
    print("você não deve nada e não sobrou nada")
        
else:
    print('bom,voce economizou',sal_mensal-gastos,'RS neste mes')
