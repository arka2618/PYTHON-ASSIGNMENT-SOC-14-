class Library:
    def __init__(self, title, writer):
        self.title = title
        self.author = writer
        self.available = True
    def checkout(self):
        if self.available == False:
            print(f"{self.title} book has been checked out")
        else:
            print(f"Sorry, {self.title} book is not available")
    def returned(self):
        if self.available == True:
            print(f"{self.title} book has been returned")
        else:
            print(f"{self.title} book is not returned")
    def show_details(self):
        status = "Available" if self.available else "Checked Out"
        print(f"Title: {self.title}\nAuthor: {self.author}\nStatus: {status}")
b1 = Library("The Blue Umbrella", "Ruskin Bond")
b2 = Library("A House for Mr Biswas", "V. S. Naipaul")
b1.show_details()
b1.checkout()
b2.returned()
b2.show_details()
