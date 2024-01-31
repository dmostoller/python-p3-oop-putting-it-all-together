#!/usr/bin/env python3

class Book():
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        self._title = new_title


    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, new_page_count):
        if type(new_page_count) == int:
            self._page_count = new_page_count
        else:
            raise Exception("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

book = Book("And Then There Were None", 25)

book.turn_page()

print(book.page_count)
print(book.title)


    
        