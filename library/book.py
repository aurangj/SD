import datetime
# create three dictionary data structures to store the details of the book
# by author, category and name which returns a list of book objects
# this dictionary will act as in memory db for now
book_author = {}
book_category = {}
book_title = {}

class Book:
    def __init__(self,id=None,title=None,author=None,category=None,pub_date=None,rackid=None):
        self.bookid= id
        self.title = title
        self.author = author
        self.category = category
        self.pub_date = pub_date
        self.rackid = rackid
        self.isavailable = True
        self.issueDate = None
        self.returnDate = None #
    def update_book_rack_id(self):
         pass
    def update_author(self):
         pass
    def update_title(self):
         pass
    def issuebook(self):
        if self.isavailable:
            self.isavailable = False
            self.issueDate = datetime.datetime.now()
            self.returnDate = self.issueDate + 5


class SearchBooks:

     def __init__(self):
         self.book_list = []

     def search_by_book_title(self,title :str):
        book_list = []
        for key, values in book_title.items():

            if title in key:
                book_list.append(Book(values[0],values[1],values[2],values[3],values[4]))

                return book_list


     def search_by_book_category(self, category : str):
        # same as above
        pass


     def search_by_book_author(self, author : str):
        #same as abaove
        pass











