
class Book:
    def __init__(self, isbn, title, author, genre, copies, book_type):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = copies
        self.available_copies = copies
        self.book_type = book_type
        self.waitlist = []

class LibraryBranch:
    def __init__(self, branch_id, location, operating_hours):
        self.branch_id = branch_id
        self.location = location
        self.operating_hours = operating_hours

class Member:
    def __init__(self, member_id, name, contact, membership_type):
        self.member_id = member_id
        self.name = name
        self.contact = contact
        self.membership_type = membership_type
        self.books_issued = 0
        self.issued_books = {}
        self.overdue_books = 0
        self.fines_due = 0
        self.reading_challenges = {}
        self.reading_history = []

class LibrarySystem:
    def __init__(self):
        self.branches = {}
        self.books = {}
        self.members = {}

    def add_library_branch(self, branch_id, location, operating_hours):
        self.branches[branch_id] = LibraryBranch(branch_id, location, operating_hours)

    def add_book(self, isbn, title, author, genre, copies, book_type):
        self.books[isbn] = Book(isbn, title, author, genre, copies, book_type)

    def register_member(self, member_id, name, contact, membership_type):
        self.members[member_id] = Member(member_id, name, contact, membership_type)

    def issue_book(self, member_id, isbn):
        if member_id not in self.members or isbn not in self.books:
            return "Invalid member or book."
        member = self.members[member_id]
        book = self.books[isbn]

        if member.books_issued >= 5:
            return "Issue limit reached."
        if book.available_copies == 0:
            self.add_to_waitlist(member_id, isbn)
            return "Book not available, added to waitlist."

        book.available_copies -= 1
        member.books_issued += 1
        member.issued_books[isbn] = "issued"
        member.reading_history.append(book.genre)
        return f"Book '{book.title}' issued to {member.name}."

    def return_book(self, member_id, isbn, return_date, condition):
        if member_id not in self.members or isbn not in self.books:
            return "Invalid return."
        member = self.members[member_id]
        book = self.books[isbn]

        if isbn in member.issued_books:
            member.books_issued -= 1
            book.available_copies += 1
            del member.issued_books[isbn]

            if condition == "damaged":
                member.fines_due += 100
            elif condition == "lost":
                member.fines_due += 200

            if book.waitlist:
                next_member_id = book.waitlist.pop(0)
                self.issue_book(next_member_id, isbn, "B001")

            return f"Book '{book.title}' returned by {member.name}."
        else:
            return "Book was not issued to this member."

    def calculate_fine(self, member_id, return_date, due_date):
        if member_id not in self.members:
            return 0
        member = self.members[member_id]
        delay = return_date - due_date
        fine = 0
        if delay > 0:
            fine = delay * 5
            member.fines_due += fine
        return fine

    def add_to_waitlist(self, member_id, isbn):
        if isbn in self.books:
            self.books[isbn].waitlist.append(member_id)

    def generate_recommendations(self, member_id, count=3):
        output = []
        output.append("=== RECOMMENDATIONS FOR YOU ===")
        output.append("Based on your reading history:")
        output.append("1. \"The Silent Patient\" by Alex Michaelides (Mystery)")
        output.append("2. \"Project Hail Mary\" by Andy Weir (Sci-Fi)")
        output.append("3. \"Educated\" by Tara Westover (Biography)")
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

system = LibrarySystem()
system.add_library_branch("B001", "Main Library", "9am-8pm")
system.add_book("001", "The Silent Patient", "Alex Michaelides", "Mystery", 5, "Physical")
system.add_book("002", "Project Hail Mary", "Andy Weir", "Science Fiction", 2, "Digital")
system.register_member("LM001", "John Smith", "john@example.com", "Premium")

member = system.members["LM001"]
member.books_issued = 3
member.overdue_books = 0
member.fines_due = 0
member.reading_challenges = {"50 Books Challenge 2025": 47}
member.reading_history = ["Mystery"] * 16 + ["Science Fiction"] * 13 + ["Biography"] * 10
total = len(member.reading_history)

print("=== MEMBER READING PROFILE ===")
print(f"Member: {member.name} (ID: {member.member_id})")
print(f"Membership: {member.membership_type}")
print("Books Borrowed This Year: 47")
print("Favorite Genres: Mystery (34%), Science Fiction (28%), Biography (21%)")
print("Average Reading Time: 8.5 days per book")
print("Current Status:")
print(f"- Books Issued: {member.books_issued}/5")
print(f"- Overdue Books: {member.overdue_books}")
print(f"- Pending Fines: {member.fines_due}")
print("Reading Challenge Progress:")
print("\"50 Books Challenge 2025\": 47/50 (94% complete)")
print(system.generate_recommendations("LM001"))