# Design a system for a library that manages different types of items available for borrowing. 
# Each item in the library has some common attributes, such as a title, a creator (like an author or director), a publication year, and a unique identifier. 
# All items should also have a way to display their details.

# Within the library, there are different types of items (e.g., books and DVDs), each with its own unique characteristics. 
# Some might have information about the number of pages, while others could include details like duration or content rating. 
# These specific characteristics should be added while still maintaining the shared structure that all library items have in common.

# In addition to storing and displaying information, the system should allow users to borrow and return items. 
# Once borrowed, an item should be marked as unavailable, and when returned, it should become available again.

class LibraryItem:

    def __init__(self, title, creator, publication_year, unique_id):
        self.__title = title
        self.__creator = creator
        self.__publication_year = publication_year
        self.__unique_id = unique_id
        self.__available = True

    @property
    def title(self):
        return self.__title

    @property
    def creator(self):
        return self.__creator
    
    @property
    def publication_year(self):
        return self.__publication_year
    
    @property
    def unique_id(self):
        return self.__unique_id
    
    @property
    def available(self):
        return self.__available

    def borrow(self):
        if not self.__available:
            raise Exception("Item is not available")
        else:
            self.__available = False

    def return_item(self):
        self.__available = True

    def __str__(self):
        return f"{self.__title} by {self.__creator} ({self.__publication_year})"
    
    def __eq__(self, other):
        return other is not None and \
            isinstance(other, LibraryItem) and \
            self.__unique_id == other.__unique_id
    
class Book(LibraryItem):

    def __init__(self, title, creator, publication_year, unique_id, num_pages):
        super().__init__(title, creator, publication_year, unique_id)
        self.__num_pages = num_pages

    @property
    def num_pages(self):
        return self.__num_pages

    def __str__(self):
        return f"[BOOK] {super().__str__()} - {self.__num_pages} pages - Avaialble: {self.available}"
    

class DVD(LibraryItem):

    def __init__(self, title, creator, publication_year, unique_id, duration):
        super().__init__(title, creator, publication_year, unique_id)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        return f"[DVD] {super().__str__()} - {self.__duration} minutes - Avaialble: {self.available}"
    
class Library:

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def __check_id(self, unique_id):
        for item in self.__items:
            if item.unique_id == unique_id:
                return True
        return False
    
    def __get_item(self, unique_id):
        for item in self.__items:
            if item.unique_id == unique_id:
                return item

    def borrow_item(self, item_id):
        if not self.__check_id(item_id):
            raise Exception("Item not found")
        self.__get_item(item_id).borrow()

    def return_item(self, item_id):
        if not self.__check_id(item_id):
            raise Exception("Item not found")
        self.__get_item(item_id).return_item()

    def __str__(self):
        return "\n".join([str(item) for item in self.__items])

if __name__ == '__main__':
    library = Library()
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937, 1, 310)
    book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 2, 223)
    dvd1 = DVD("Inception", "Christopher Nolan", 2010, 3, 148)
    dvd2 = DVD("The Dark Knight", "Christopher Nolan", 2008, 4, 152)

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(dvd1)
    library.add_item(dvd2)

    print(library)

    print("\n----------------------------------------------------")

    library.borrow_item(1)
    print(library)
    print("\n----------------------------------------------------")

    library.borrow_item(3)
    print(library)
    print("\n----------------------------------------------------")

    library.return_item(1)
    print(library)
    print("\n----------------------------------------------------")

    library.return_item(3)
    print(library)
    print("\n----------------------------------------------------")
    
    try:
        library.borrow_item(5)
    except Exception as e:
        print(e)
        print("\n----------------------------------------------------")
        
    try:
        library.return_item(5)
    except Exception as e:
        print(e)
        print("\n----------------------------------------------------")
        
    library.borrow_item(1)
    try:
        library.borrow_item(1)
    except Exception as e:
        print(e)
        print("\n----------------------------------------------------")