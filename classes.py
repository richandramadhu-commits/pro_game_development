#classes are templates/blueprint/recipe
class B72():
    books="book"
    pencils="pencil"
    rulers="ruler"
    erasers="eraser"
    #constructor is called when the object is created
    def __init__(self):
        print("hi")
    def change_details(self):
        self.pencils=input("how many pencils are sharpened? ")
        self.rulers=input("how long is longest ruler? ")
    def show_details(self):
        print(self.books)
        print(self.erasers)
        print(self.pencils)
        print(self.rulers)
#object
anything=B72()
object=B72()
anything.change_details()
anything.show_details()
object.show_details()