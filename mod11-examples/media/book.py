from publication import Publication


class Book(Publication):
    def __init__(self, name, page_count):
        self.page_count = page_count
        super().__init__(name)
        self.editorname = "Rosa Liksom"

    def print_info(self):
        super().print_info()
        print(f"Olen {self.page_count}-sivuinen kirja, kirjailija: {self.editorname} ")