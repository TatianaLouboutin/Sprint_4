import pytest

from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2


    def test_add_new_book_add_the_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_add_book_with_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_set_book_genre_add_two_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Ужасы')
        assert list(collector.books_genre.values()) == ['Фантастика', 'Ужасы']

    def test_set_book_genre_no_genre_dont_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Боевик')
        assert list(collector.books_genre.values()) == ['Фантастика', '']


    def test_get_book_genre_correct_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Боевик')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Horror night')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Ужасы')
        collector.set_book_genre('Horror night', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если ваш кот хочет вас убить', 'Horror night']

    def test_get_books_for_children_horror_is_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Ужасы')
        assert not collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    lst_books = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', 'Великий Гэтсби']
    @pytest.mark.parametrize('name', lst_books)
    def test_add_book_in_favorites_three_books(self, name):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Великий Гэтсби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Великий Гэтсби')
        assert name in collector.favorites

    def test_delete_book_from_favorites_one_book_is_not_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Великий Гэтсби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Великий Гэтсби')
        collector.delete_book_from_favorites('Великий Гэтсби')
        assert not 'Великий Гэтсби' in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Великий Гэтсби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Великий Гэтсби')
        collector.delete_book_from_favorites('Великий Гэтсби')
        assert collector.favorites == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']
