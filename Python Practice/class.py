class Human:
    def __init__(self, n, o):
        self.name = n
        self.occ = o

    def work (self):
        if self.occ == "tenis player" :
            print(self.name , "is a tennis player")

        elif self.occ == "dance" :
            print(self.name, "is a dancer")


    def speak (self):
        print(self.name ,'says hello world!')



alvee =Human("Alvee", "tenis player")
alvee.work()
alvee.speak()

mahia =Human("Mahia", "tenis player")
mahia.work()
mahia.speak()