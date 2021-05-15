class Noon():
    

    def __init__(self,f,b,c):
        self.a = f
        self.b = b
        self.c = c
        print("This is the init-1")
    
    def dave(self):
        print(self.a, self.b,"This Test-2")

    def moon(self):
        print("This is the Moon-3",self.a, self.b, self.c)

full = Noon(23,17,"red")
full2 = Noon(12.5, 89,"green")
andy = Noon("This","Is","Hole")
frank = Noon("fish",1,2)
full.moon()
full2.moon()
andy.moon()
full.dave()
print(full.a)
print(frank.b)





