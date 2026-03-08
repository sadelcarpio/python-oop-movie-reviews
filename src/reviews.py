from movies import MovieCatalog, Movie
from users import UsersDb, User


class Review:
    def __init__(self, movie_id: int, user_id: int, rating: int, review_text: str):
        pass


class KinoReviewsManager:
    def __init__(self, movies_catalog: MovieCatalog, users_db: UsersDb):
        pass

    def add_review(self, movie: Movie, user: User, rating: int, review_text: str):
        pass

    def show_top_rated_movies(self):
        pass

    def show_most_reviewed_movies(self):
        pass

    def export_reviews_to_csv(self, filename: str):
        pass
