class rabotnik:
    def __init__(self, i, k):
        self.num = i
        self.kilom = k
    def tar(self, t):
        self.taksi = tak[t]
        
class taksi:
    def __init__(self, num, t):
        self.num=num
        self.tarif = t
n=int(input("Введите количество сотрудников от 1 до 1000: \n"))
rab=[]
tak = []
sum = 0
l=0
k=0
b=100000
i=0
c=1
for j in range(n):
    kil = int(input(f"Введите расстояние в километрах для {j+1} работника: "))
    rab.append(rabotnik((j+1), kil))
for j in range(n):
    tar= int(input(f"Введите тариф для {j+1} такси за километр: "))
    tak.append(taksi((j+1), tar))
list.sort(rab, key=lambda rabotnik: rabotnik.kilom)
list.sort(tak, reverse = True, key=lambda taksi: taksi.tarif)
for j in rab:
    j.tar(l)
    l=l+1
for j in range(n):
    sum = sum + (rab[j-1].kilom * tak[j-1].tarif)
list.sort(rab, key=lambda rabotnik: rabotnik.num)
for j in rab:
    print (j.num, "работник отправится на такси №", j.taksi.num)
print ("Общая сумма составляет:", sum)
try:
    a = sum
except ValueError:
    a = sum
ed1 = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
ed2 = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
ch = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
dec = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
sotn = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
tys = ["тысяча", "тысячи", "тысяч"]
rub = ["рубль", "рубля", "рублей"]

a1 = a // 100000
a2 = (a // 10000) % 10
a3 = (a // 1000) % 10
a4 = (a // 100) % 10
a5 = (a // 10) % 10
a6 = a % 10

chislo = ""
if a1 != 0:
    i1 = a1 - 1
    chislo += sotn[i1] + " "

if a2 == 1 and a3 == 0:
    chislo += dec[0] + " "

if a2 != 1:
    if a2 != 0:
        i2 = a2 - 1
        chislo += dec[i2] + " "

if a3 != 0:
    if a2 == 1:
        i3 = a3 - 1
        chislo += ch[i3] + " " + tys[2] + " "
    else:
        i3 = a3 - 1
        chislo += ed2[i3] + " "
        if a3 == 1:
            chislo += tys[0] + " "
        elif 1 < a3 < 5:
            chislo += tys[1] + " "
        else:
            chislo += tys[2] + " "

if (a3 == 0) and (a2 or a1 != 0):
    chislo += tys[2] + " "

if a4 != 0:
    i4 = a4 - 1
    chislo += sotn[i4] + " "

if a5 == 1 and a6 == 0:
    chislo += dec[0] + " "

if a5 != 1:
    if a5 != 0:
        i5 = a5 - 1
        chislo += dec[i5] + " "

if a6 != 0:
    if a5 == 1:
        i6 = a6 - 1
        chislo += ch[i6] + " " + rub[2]
    else:
        i6 = a6 - 1
        chislo += ed1[i6] + " "
        if a6 == 1:
            chislo += rub[0] + " "
        elif 1 < a6 < 5:
            chislo += rub[1] + " "
        else:
            chislo += rub[2] + " "
if (a6 == 0) and (a5 or a4 or a3 or a2 or a1 !=0):
    chislo += rub[2]
chislo = chislo.capitalize()
print(chislo)
