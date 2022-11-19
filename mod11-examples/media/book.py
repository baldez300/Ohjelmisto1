from publication import Publication


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Olen {self.page_count}-sivuinen kirja, kirjailija: {self.author} ")