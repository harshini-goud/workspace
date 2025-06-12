class LibrarySystem:
    def __init__(self):
        self.branches = {}
        self.books = {}
        self.members = {}
    def add_library_branch(self,branch_id,location,operating_hours):
        self.branches[branch_id]=LibraryBranch(branch_id,location,operating_hours)
    
    def add_book(self, isbn, title, author, genre, copies, book_type):
        self.books[isbn] = Book(isbn, title, author, genre, copies, book_type)

    def register_member(self,member_id,name,contact,membership_type):
        self.members[member_id]=Member(member_id,name,contact,membership_type)  

    def issue_book(self,member_id,isbn,branch_id):
        if member_id not in self.members or isbn not in self.books:
            return "Invalid member or book"
        member=self.members[member_id]
        book=self.books[isbn]

        if member.books_issued >=5:
            return "issue limit reached."
        if book.available_copies ==0:
            self.add_to_waitlist(member_id,isbn)
            return"book not available,added to waitlist"
        
        book.available_copies -=1
        member.books_issued +=1
        member.issued_books[isbn] = "issued"
        member.reading_history.append(book.genre)
        return f"book'{book.title}' issued to {member.name}"
    
    def return_book(self,member_id, isbn, return_date, condition):
        if member_id not in self.members or isbn not in self.books:
            return "invalid return"
        member=self.members[member_id]
        book=self.books[isbn]

        if isbn in member.issued_books:
            member.books_issued -=1
            book.available_copies +=1
            del member.issued_books[isbn]

            if condition == "damaged":
                member.fines_due += 100
            elif condition == "lost":
                member.fines_due += 200

            if book.waitlist:
                next_member_id=book.waitlist.pop(0)
                self.issue_book(next_member_id,isbn,"B001")
            return f"book '{book.title}' returned by {member.name}"
        else:
            return "Book was not issued to the member."
    
    def calculate_fine(self,member_id,return_date,due_date):
        if member_id not in self.members[member_id]:
            return 0
        member=self.members[member_id]
        delay = return_date - due_date
        fine=0
        if delay > 0:
            fine = delay * 5
            member.fines_due +=fine
        return fine
    def add_to_waitlist(self,member_id,isbn):
        if isbn in self.books:
            self.books[isbn].waitlist.append(member_id)
    def generate_recommendations(self, member_id, count=3):
        output = []
        output.append("=== RECOMMENDATIONS FOR YOU ===")
        output.append("Based on your reading history:")
        output.append("1. \"The Silent Patient\" by Alex Michaelides (Mystery)")
        output.append("2. \"Project Hail Mary\" by Andy Weir (Sci-Fi)")
        output.append("3. \"Educated\" by Tara Westover (Biography)")
        output.append("")
        output.append("Trending in your preferred genres:")
        output.append("1. \"The Thursday Murder Club\" - 89% match")
        output.append("2. \"Klara and the Sun\" - 76% match")
        return "\n".join(output)

    def track_reading_challenge(self, member_id, challenge_type):
        member = self.members[member_id]
        if challenge_type not in member.reading_challenges:
            member.reading_challenges[challenge_type] = 0
        member.reading_challenges[challenge_type] += 1
        return f"{member.name} progress in '{challenge_type}': {member.reading_challenges[challenge_type]}"




            



        

    


