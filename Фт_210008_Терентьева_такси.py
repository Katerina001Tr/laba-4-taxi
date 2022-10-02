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
