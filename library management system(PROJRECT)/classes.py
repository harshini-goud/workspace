class Book:
    def __init__(self,isbn,title,author,genre,copies,book_type):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.genre=genre
        self.copies=copies
        self.available_copies=copies
        self.book_type=book_type
        self.waitlist=[]

class LibraryBranch:
    def __init__(self,branch_id,location,operating_hours):
        self.branch_id=branch_id
        self.location=location
        self.operating_hours=operating_hours

class Member:        
    def __init__(self,member_id,name,contact,membership_type):
        self.member_id=member_id
        self.name=name
        self.contact=contact
        self.membership_type=membership_type
        self.books_issued=3
        self.overdue=0
        self.fine=0
        self.total_books_borrowed=47
        self.avg_reading_time=8.5
        self.reading_challenges={"50 Books challenge 2025":47}
        self.reading_history=(
            ["mystery"]*16+
            ["Science Fiction"]*13+
            ["Biography"]*10
        )
        




    
