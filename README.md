# Implementando un sistema de reseñas de películas con Python y Programación Orientada a Objetos
En este proyecto, nos pondremos como meta desarrollar una plataforma similar a [IMDB](https://www.imdb.com/) o [Letterboxd]
(https://letterboxd.com/) completamente en Python. La mayor simplificación consiste en que nuestro programa manejará la creación de usuarios
(en plataformas reales varios usuarios se registran y generan tráfico / interacciones).

La funcionalidad principal de nuestra plataforma debe ser registrar y administrar las reseñas de usuarios sobre películas de nuestro 
catálogo.

## Requerimientos técnicos
La plataforma, que llamaremos **KinoReviews**, será una aplicación por línea de comandos que deberá contar con la siguiente funcionalidad:
- Creación de usuarios: Tendremos una clase `UsersDb` la cual nos permitirá crear usuarios `User`, a partir de un correo electrónico. 
Debe implementar los métodos `add_user(email: str)` y `get_user(user_id: int)`.

- Catálogo de Películas: La clase `MovieCatalog` contendrá un listado de películas variadas. La clase `Movie` debe tener ciertos atributos como 
el nombre, descripción breve, año de estreno, director, géneros.
Debe implementar los métodos `add_movie()` y `get_movie(movie_id: int)`:

Sobre las reseñas: Se sugiere crear una Clase `KinoReviewsManager` que permita:
- Los usuarios pueden dejar una sola reseña sobre una película. La clase `Review` debería contener un identificador, el usuario 
(la forma más fácil sería asignar un id a cada usuario), la película (de la misma manera, un identificador por película), calificación en estrellas (del 1 al 5) y 
texto de la reseña (opcional, puede no darse). Estas reseñas pueden ser editadas o eliminadas.
ejemplo: `kinoReviewsManager.add_review(user: User, movie: Movie, rating: int, review_text: str = None)`

- Cada usuario tiene los atributos: `num_reviews_given` y `average_rating_given` los cuales van modificándose a medida que siguen haciendo reseñas.

- Cada película tiene los atributos: `num_reviews` y `average_rating` que se irá modificando de la misma forma a medida que reciben reseñas.

- `KinoReviewsManager` podrá tambien mostrar una lista de las películas con mejores puntajes, así como la mayor cantidad de reseñas.
ejemplo: `kinoReviewsManager.show_top_rated_movies()`, `kinoReviewsManager.show_most_reviewed_movies()`

- Finalmente, `kinoReviewsManager` tendrá la opción de exportar los datos a un archivo CSV, con el siguiente formato:
`user_id,movie_id,rating,review`

## Consideraciones de diseño

1. Responsabilidad de las clases. Cada clase debe tener una funcionalidad clara y definida. Antes de escribir el código, 
elabora un diagrama que te permita describir claramente las relaciones entre las clases, sus atributos y métodos.

2. Construcción de objetos. Piensa qué datos son necesarios para construir los objetos de una clase, y además, quién sería el 
responsable de construirlos (el usuario mediante el programa, la clase `MovieCatalog`, la clase `KinoReviewsManager`, etc.)

3. Manejo de errores. Piensa qué partes del programa pueden generar errores (por ejemplo, tratar de crear un review dos veces, 
dar un rating fuera del rango 1-5). Con `try` y `except` puedes manejar estos errores de manera adecuada.

## Sugerencias / Ayuda
Preguntar a Sergio en el canal de WhatsApp.
- Puedes usar cualquier versión de Python. Te recomiendo una versión superior a 3.8, y utilizar un entorno virtual para el proyecto (
recomendable `venv` o `uv`
  )
- El proyecto debe ser avanzado en este repositorio. Solo necesitamos saber lo básico de GitHub, usa VsCode o Pycharm para 
poder subir tus cambios más fácilmente.