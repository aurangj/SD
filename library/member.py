import datetime
from SD.library.book import *
from datetime import timedelta
# create a member object and pass that to issuebook(member, book)
# ideally this will map to db table using any ORM.
# create multiple book instances.


class Member:

    def __init__(self,id,name,email):
        self.membership_id = id
        self.num_of_books = 5
        self.name = name
        self.email = email
        self.isactive = False
        self.booklist= []

    def get_num_books(self):
        return self.num_of_books

    def calculate_penalty(self):
        pass
    def is_member(self):
        return self.isactive
    def assignbook(self,book):
        self.booklist.append(book)


class libraryCard:
    library_card_id = 0

    def __init__(self,member_id=None,issueDate=None):

        self.member_id = member_id
        self.issueDate = issueDate
        self.active = False

    @classmethod
    def generate_library_card(cls,m):
        # create library card instance from member instances
        return cls(m.is_member_id,datetime.datetime.now(),'True')

    def generate_id(self):
         return libraryCard.library_card_id + 1



class library:
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.search= SearchBooks()


    def searchbook(self, criteria=None,value=None):
        if criteria == 'title':
            self.search.search_by_book_title(value)
        elif criteria == 'author':
            self.search.search_by_book_author(value)
        elif criteria == 'category':
            self.search.search_by_book_category(value)

    def issuecard(self):
        # create member class and issue library card
        m = Member()
        l = libraryCard()
        l.generate_library_card(m)

    def authentication(self,member_id):
        member = self.member.is_member(member_id)
        return member


    def issuebook(self,member,book):
        if member.is_member():
            if book.isavailable:
                book.issuebook()
                member.assignbook()

        pass
    def penalty_calulcation(self,member):
        # calculates 5 rs per day penalty
        for book in member.booklist:
            if (datetime.datetime.now() - book.returnDate) > 0:
                return 5 * datetime(datetime.datetime.now() - book.returnDate).days()

    def book_return(self,member_id,book_id):
        pass

if __name__ == '__main__':

    m1 = Member()
    m2 = Member()
    b1 = Book()
    b2 = Book()
    b3 = Book()
    l = library()
    l.authentication(m1)
    l.issuebook(m1,b1)





