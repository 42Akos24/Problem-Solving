class BookRent:

    def __init__(self, member, book, rent_start_date, rent_end_date='2025-06-01'):
        self.member = member
        self.book = book
        self.rent_start_date = rent_start_date
        self.rent_end_date = rent_end_date
