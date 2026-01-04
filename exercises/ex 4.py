class book:
    def __init__(self,title,auther,price):
        self.title = title
        self.auther = auther
        self.price = float(price)
    def display_detail(self):
        print(f"title{self.title}")
        print(f"auther{self.auther}")
        print(f"price{self.price:.2f}")

    def aply_discount(self,percent):
      self.price *= (1-float(percent)/100)

ketab1= book("harry potter" , "j.k.rowling", 45000)
ketab2= book( "game of thrones" , "george raymond martin", 100000)

print("ghabl")
ketab2.display_detail()

ketab2.aply_discount(40)

print("first")
ketab1.display_detail()
print("two")
ketab2.display_detail()