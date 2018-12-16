class OS:
    name = "Android"
    year = 2012
    multitasking = True
class Samsung :
    website = "www.samsung.com"
    Manufacture_country = "South Korea"

#class inheritance with parent class Samsung
class TV(Samsung):
    def __init_(self):
        print ("This is a product is made in %s. You can go to the website for more details %s" % (self.Manufacture_country, self.website))

#multiple inheritance with parent class OS and Samsung 
class S9(OS, Samsung):
    def __init__(self):
        if self.multitasking is True:
            print ("THis is a multitasking system. Visit {} for more details".format(self.website))
            print ("Name :" , self.name)
S9_1 = S9()
STV1 = TV()
