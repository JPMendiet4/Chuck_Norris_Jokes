# Chuck Norris Jokes API

This application is an API that connects to the Chuck Norris API to fetch random jokes and allow users to save their favorite jokes to a database. It also features a custom authentication system using JWT tokens.

## Features

- Fetches a random joke from the Chuck Norris API.
- Allows users to save jokes as favorites.
- Includes a custom authentication system using JWT tokens.

## Requirements

To run this application, you will need:

- Python 3.x
- A virtual environment
- Dependencies listed in the requirements.txt file

## Installation

1. Clone this repository.
2. Create a virtual environment: `python -m venv env`.
3. Activate the virtual environment: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows).
4. Install the dependencies: `pip install -r requirements.txt`.
5. Run the migrations: `python manage.py migrate`.
6. Start the server: `python manage.py runserver`.

## Configuration

This application uses a SQLite database. To change the database configuration, update the `settings.py` file.

## Usage

1. Start the server: `python manage.py runserver`.
2. Log in using the following credentials:
   - Username: `admin`.
   - Password: `123456`.
3. To fetch a random joke, make a GET request to `/api/jokes/random`.
4. To save a joke as a favorite, make a POST request to `/api/jokes/favorites` with the following data:
   - `joke_id`: The ID of the joke you want to save.
5. To fetch all favorite jokes, make a GET request to `/api/jokes/favorites`.

## Contributing

If you would like to contribute to this application, follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes and commit them (`git commit -am "Added a new feature"`).
4. Push your changes (`git push origin feature/my-feature`).
5. Open a pull request.

## License

This application is distributed under the MIT license.

## Contact

If you have any questions or issues with this application, feel free to contact us by email at `support@example.com`.
