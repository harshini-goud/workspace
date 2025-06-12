member=system.members["LM001"]
member.books_issued = 3
member.overdue_books = 0
member.fines_due = 0
member.reading_challenges = {"50 Books Challenge 2025": 47}
member.reading_history = ["Mystery"] * 16 + ["Science Fiction"] * 13 + ["Biography"] * 10
total=len(member.reading_history)