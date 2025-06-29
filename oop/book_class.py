class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def __del__(self):
        print(f"Deleting {self.__title}")

    def __str__(self):
        return (f"{self.__title} by {self.__author}, published " +
                f"in {self.__year}")

    def __repr__(self):
         return (f"Book('{self.__title}', '{self.__author}', '{self.__year}')")
