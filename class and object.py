#EXAMPLE PROGRAM FOR CLASS AND OBJECT
class libary:
    def __init__(self):#__init__ is contructor 
        print("Program for class and object creation")
     
    def books(name,author,year_establish):
        print("name of the book:",name)
        print("author of the book :",author)
        print("year of the establish :",year_establish)
l=libary #l is the object to call the class libary
l.books("kambaramayanam","kambar",1990)

