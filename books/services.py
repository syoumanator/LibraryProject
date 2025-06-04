from datetime import date
from rest_framework.exceptions import ValidationError


def take_book(book):
    """Выдача книги"""
    if book.is_available:
        if book.in_stock_quantity >= 1:
            book.in_stock_quantity -= 1
            book.save()
        else:
            book.is_available = False
            book.save()
        return book
    else:
        raise ValidationError(f"Книга {book.title} отсутствует")


def return_book(take_book, book):
    """Возврат книги"""
    if not take_book.is_returned:
        take_book.is_returned = True
        take_book.return_date = date.today()
        if book.in_stock_quantity < book.quantity:
            book.in_stock_quantity += 1
            book.is_available = True
            book.save()
            take_book.save()
        else:
            raise ValidationError(f"Книга {book.title} возвращена")
    else:
        raise ValidationError(f"Книга {book.title} возвращена")
