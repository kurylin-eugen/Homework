print('Введите ваш вес')
Weight =int(input())
print('Введите ваш рост')
Heihgt =int(input())
BMI= Weight / ((Heihgt/100)**2)
print('Ваш индекс массы тела' , BMI )
I = round(BMI)
L, R = 20, 50
print(str(L) + '='*(I-L-1) + '|' + '='*(R-I-1) + str(R))
