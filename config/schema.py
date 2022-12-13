import strawberry
import typing


@strawberry.type
class Movie:
    pk: int
    title: str
    year: int
    rating: int


movies_db: typing.List[Movie] = [
    Movie(pk=1, title="god father1", year=1990, rating=5),
    Movie(pk=2, title="god father2", year=1991, rating=3),
    Movie(pk=3, title="god father3", year=1992, rating=2),
]


@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        return "pong"

    @strawberry.field
    def movies(self) -> typing.List[Movie]:
        return movies_db

    @strawberry.field
    def movie(self, movie_pk: int) -> Movie:
        return movies_db[movie_pk - 1]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_movie(self, title: str, year: int, rating: int) -> Movie:
        movie = Movie(pk=len(movies_db) + 1, title=title, year=year, rating=rating)
        movies_db.append(movie)
        return movie


schema = strawberry.Schema(query=Query, mutation=Mutation)
