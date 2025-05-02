class Animals:
    pass
    # def bark():
    #     print("Animals barking")
    
class Pets(Animals):
    pass
    # def bark():
    #     print("Pets Don't barks")
class Dogs(Pets):
    @staticmethod
    def bark():
        print("Dog barking")
d =Dogs()
d.bark()  