#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4

list=[1,6,9,3,6]
ChekIndex=1
Sum=0
for i in list:
    if ChekIndex%2!=0:
        print(i,end=',')
        Sum+=i
    ChekIndex+=1
print(f'\n{Sum}\n')


#*********************************************8
#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
list = [1,2,3,10,3,3,1]
def ProductionIndex(list):
    index=0
    index2=1
    while index<len(list)/2:
        print(list[index]*list[-index2],end=',')
        index2+=1
        index+=1
ProductionIndex(list)
print()

#******************************************************************************

#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19



list=[1.2,3.5,6.3,8.9]
def FractionsNumber(list):
    for i in range(len(list)):
        list[i]-=int(list[i])
    print(list)
FractionsNumber(list)
result = round(max(list)-min(list),2)
print(result)

#или
sort=sorted(list)
print(sort)
print(round(list[-1]-list[0],2))
print()
#*******************************************************8
#Написать программу преобразования десятичного числа в двоичное

Number=int(input('введите число\t'))
NewNumber = ''
while Number>0:
    NewNumber=str(Number%2)+NewNumber
    Number//=2
print(f'{NewNumber}\n==================') 

# Написать программу преобразования двоичного числа в десятичное.
Number2 = int (str(NewNumber))
print (NewNumber)
degree=0
result=0
while Number2>0:
    result+=(Number2%10)*(2**degree)
    Number2//=10
    degree+=1
print(result)
print()
#***********************************************************************
#3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
fibonachi1 = 0
fibonachi2 = 1
result=0
number = int(input('введите число\t'))
i = 0
while i < number :
    fibonachisum = fibonachi1 + fibonachi2
    fibonachi1 = fibonachi2
    fibonachi2 = fibonachisum
    i += 1
    if fibonachi2%2==0:
        result+=fibonachi2
print(result)
   


