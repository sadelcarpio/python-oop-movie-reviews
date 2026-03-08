from movies import MovieCatalog
from users import UsersDb


class KinoReviewsManager:
    def __init__(self, movies_catalog: MovieCatalog, users_db: UsersDb):
        pass

    def add_review(self, movie_id: str, user_id: str, review_text: str):
        pass

    def show_top_rated_movies(self):
        pass

    def show_most_reviewed_movies(self):
        pass

    def export_reviews_to_csv(self, filename: str):
        pass
