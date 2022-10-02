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
