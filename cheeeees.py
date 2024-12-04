class CHESS:
    def __init__(self):
        n=0
        self.a=[]
        while n!=8:
            self.a.append([])
            if n<3:
                for i in range(0,8):
                    if (n+i)%2==0 :
                        self.a[n].append(2)
                    else:
                        self.a[n].append(0) 
            elif n<5:
                for i in range(0, 8):
                    self.a[n].append(0)
            else:
                for i in range(0,8):
                    if (n+i)%2==0 :
                        self.a[n].append(1)
                    else:
                        self.a[n].append(0)  
            n = n + 1
        self.right=1
    def doska(self):
        for i in self.a:
            print(i)
    def proverka(self):
        k=int(input("Введите координату x "))
        j=int(input("Введите координату y "))
        if self.a[k-1][j-1]==1 or self.a[k-1][j-1]==2:
            return print("Клетка занята")
        else:
            return print("Клетка свободна")
    def add(self):
        k=int(input("Введите координату x "))
        j=int(input("Введите координату y "))
        while  self.a[k-1][j-1]==1:
            print("Введите новые переменные")
            k=int(input("Введите координату x "))
            j=int(input("Введите кооримнату y "))
        self.a[k-1][j-1]=1
        print("Клетка добавлена")
    def removed(self):
        k=int(input("Введите координату x "))
        j=int(input("Введите координату y "))
        while  self.a[k-1][j-1]==0:
            print("Введите новые переменные")
            k=int(input("Введите координату x "))
            j=int(input("Введите кооримнату y "))
        self.a[k-1][j-1]=0
        print("Клетка убрана")

