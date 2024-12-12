class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
p1=Book("Python","Joy","42")
print(p1.title)
print(p1.author)
print(p1.pages)



# question5 (ii)
class EBook:
    def __init__(self, title,author,pages,format):
        self.title = title
        self.author = author  
        self.pages = pages
        self.format = format
    def new_class(self):
            print(self.title)
            print(self.author)
            print(self.pages)
            print(self.format)
p1 =EBook("python","Joy","42","New edition")
p1.new_class()


 # question5
 # iii
def book():
     title = "python"
     author ="Joy"
     while title=="python" and author=="Joy":
          values =["title","author"]
          return values
     
#question5
#iv)
# A class is an attribute with many properties that stores key objects.
# An object is an oriented object programming  attribute which inherits the properties of a class.