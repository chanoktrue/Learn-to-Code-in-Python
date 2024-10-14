class Animal:    
    def __init__(self, colour, legs):
        self.colour = colour
        self.legs = legs
                
    def move(self):
        print("ขยับ...ขยับ...")
        
class Cat(Animal):    
    def __init__(self):
        super().__init__("whtie", 2)
            
    def speek(self,sound):
        print(f"ส่งเสียยดัง : {sound}") 
        
cat = Cat()
print(cat.speek("เมียว... 11"))

cat.move()
print("cat สี: " , cat.colour , "มี ขา : " , cat.legs)