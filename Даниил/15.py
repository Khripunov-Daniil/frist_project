

# avtom = ("fiat", " albea", "2012", " 1.6", "rad", "500 000")


class Car(object):
 
    def __init__(self, model, god,  ob_dvig, color):
        self.model = model
        self.god = god
   
        self.ob_dvig =ob_dvig
        self.color = color

 
    def printer(self):
        print(self.model)
        print(self.god)

        print(self.ob_dvig)
        print(self.color)

 
 
if __name__ == '__main__':
    auto = Car('придумать свойства самостоятельно')
    auto.printer()


avtom = ("fiat",  "2012", " 1.6", "rad", "500 000")