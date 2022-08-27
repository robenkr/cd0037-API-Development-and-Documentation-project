# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Reference

### Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at
  the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False, 
    "error": 404,
    "message": "Not found"
}
```

The API will return two error types when requests fail:

- 404: Resource Not Found
- 422: Unprocessable

### Endpoints

#### GET /categories

- General:
  - Returns a list of category objects, success value, and total number of categories
- Sample: `curl http://127.0.0.1:5000/categories`

``` 
{
  "categories": [
    {
      "id": 7,
      "type": "Science"
    },
    {
      "id": 8,
      "type": "Art"
    },
    {
      "id": 9,
      "type": "Geography"
    },
    {
      "id": 10,
      "type": "History"
    },
    {
      "id": 11,
      "type": "Entertainment"
    },
    {
      "id": 12,
      "type": "Sports"
    },
    {
      "id": 13,
      "type": "Science-Fiction"
    }
  ],
  "success": true,
  "total_categories": 7
}
```

#### POST /categories

- General:
  - Creates a new category using the submitted type. Returns the id of the created category, success value, total
    categories, and category list.
- `curl http://127.0.0.1:5000/categories -X POST -H "Content-Type: application/json" -d '{"type":"Music"}'`

``` 
{
  "categories": [
    {
      "id": 7,
      "type": "Science"
    },
    {
      "id": 8,
      "type": "Art"
    },
    {
      "id": 9,
      "type": "Geography"
    },
    {
      "id": 10,
      "type": "History"
    },
    {
      "id": 11,
      "type": "Entertainment"
    },
    {
      "id": 12,
      "type": "Sports"
    },
    {
      "id": 13,
      "type": "Science-Fiction"
    },
    {
      "id": 14,
      "type": "Music"
    }
  ],
  "success": true,
  "created": 14,
  "total_categories": 8
}
```

#### GET /questions

- General:
  - Returns a list of question objects, list of category objects, success value, selected category, and total number of
    questions
  - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions`

```
{
  "categories": [
    {
      "id": 7,
      "type": "Science"
    },
    {
      "id": 8,
      "type": "Art"
    },
    {
      "id": 9,
      "type": "Geography"
    },
    {
      "id": 10,
      "type": "History"
    },
    {
      "id": 11,
      "type": "Entertainment"
    },
    {
      "id": 12,
      "type": "Sports"
    },
    {
      "id": 13,
      "type": "Science-Fiction"
    }
  ],
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 11,
      "difficulty": 4,
      "id": 25,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 11,
      "difficulty": 4,
      "id": 26,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 10,
      "difficulty": 2,
      "id": 27,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 11,
      "difficulty": 3,
      "id": 28,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 10,
      "difficulty": 1,
      "id": 29,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 12,
      "difficulty": 3,
      "id": 30,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 12,
      "difficulty": 4,
      "id": 31,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 10,
      "difficulty": 2,
      "id": 32,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 9,
      "difficulty": 2,
      "id": 33,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 9,
      "difficulty": 3,
      "id": 34,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 21
}
```

#### POST /questions

- General:
  - Creates a new question using the submitted question, answer, category and difficulty. Returns the id of the created
    question, success value, total questions, and question list.
- `curl http://127.0.0.1:5000/categories -X POST -H "Content-Type: application/json" -d '{"question": "Who is the savior of the world ?", "answer": "Jesus", "category": 10, "difficulty": 1 }'`

``` 
{
  "created": 72,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 11,
      "difficulty": 4,
      "id": 25,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 11,
      "difficulty": 4,
      "id": 26,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 10,
      "difficulty": 2,
      "id": 27,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 11,
      "difficulty": 3,
      "id": 28,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 10,
      "difficulty": 1,
      "id": 29,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 12,
      "difficulty": 3,
      "id": 30,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 12,
      "difficulty": 4,
      "id": 31,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 10,
      "difficulty": 2,
      "id": 32,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 9,
      "difficulty": 2,
      "id": 33,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 9,
      "difficulty": 3,
      "id": 34,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 9,
      "difficulty": 2,
      "id": 35,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 8,
      "difficulty": 1,
      "id": 36,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 8,
      "difficulty": 3,
      "id": 37,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 8,
      "difficulty": 4,
      "id": 38,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 8,
      "difficulty": 2,
      "id": 39,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 7,
      "difficulty": 4,
      "id": 40,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 7,
      "difficulty": 3,
      "id": 41,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 7,
      "difficulty": 4,
      "id": 42,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 10,
      "difficulty": 4,
      "id": 43,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Jesus",
      "category": 10,
      "difficulty": 1,
      "id": 54,
      "question": "Who is the savior of the world ?"
    },
    {
      "answer": "Former president of Zaire",
      "category": 10,
      "difficulty": 3,
      "id": 65,
      "question": "Who is Mobutu?"
    },
    {
      "answer": "Jesus",
      "category": 10,
      "difficulty": 1,
      "id": 72,
      "question": "Who is the savior of the world ?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```

#### GET /categories/category_id/questions

- General:
  - Returns a list of question objects of given category ID, the category object, success value, and total number of
    questions
- Sample: `curl http://127.0.0.1:5000/questions`

```
{
  "category": {
    "id": 12,
    "type": "Sports"
  },
  "questions": [
    {
      "answer": "Brazil",
      "category": 12,
      "difficulty": 3,
      "id": 30,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 12,
      "difficulty": 4,
      "id": 31,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```

#### DELETE /questions/{question_id}

- General:
  - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total
    questions, and question list.
- `curl -X DELETE http://127.0.0.1:5000/questions/72`

```
{
  "deleted": 72,
  "currentCategory": null,
  "categories": [
    {
      "id": 7,
      "type": "Science"
    },
    {
      "id": 8,
      "type": "Art"
    },
    {
      "id": 9,
      "type": "Geography"
    },
    {
      "id": 10,
      "type": "History"
    },
    {
      "id": 11,
      "type": "Entertainment"
    },
    {
      "id": 12,
      "type": "Sports"
    },
    {
      "id": 13,
      "type": "Science-Fiction"
    }
  ],
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 11,
      "difficulty": 4,
      "id": 25,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 11,
      "difficulty": 4,
      "id": 26,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 10,
      "difficulty": 2,
      "id": 27,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 11,
      "difficulty": 3,
      "id": 28,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 10,
      "difficulty": 1,
      "id": 29,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 12,
      "difficulty": 3,
      "id": 30,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 12,
      "difficulty": 4,
      "id": 31,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 10,
      "difficulty": 2,
      "id": 32,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 9,
      "difficulty": 2,
      "id": 33,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 9,
      "difficulty": 3,
      "id": 34,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 9,
      "difficulty": 2,
      "id": 35,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 8,
      "difficulty": 1,
      "id": 36,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 8,
      "difficulty": 3,
      "id": 37,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 8,
      "difficulty": 4,
      "id": 38,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 8,
      "difficulty": 2,
      "id": 39,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 7,
      "difficulty": 4,
      "id": 40,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 7,
      "difficulty": 3,
      "id": 41,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 7,
      "difficulty": 4,
      "id": 42,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 10,
      "difficulty": 4,
      "id": 43,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Jesus",
      "category": 10,
      "difficulty": 1,
      "id": 54,
      "question": "Who is the savior of the world ?"
    },
    {
      "answer": "Former president of Zaire",
      "category": 10,
      "difficulty": 3,
      "id": 65,
      "question": "Who is Mobutu?"
    }
  ],
  "success": true,
  "total_questions": 21
}
```

#### POST /quizzes

- General:
  - Returns a random question object using the submitted list of previous questions and category object.
- `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [{"question": "Who is the savior of the world ?", "answer": "Jesus", "category": 10, "difficulty": 1, "id": 54}], "quiz_category": { "id": 10, "type": "History" }'`

```
{
  "currentQuestion": {
    "answer": "Jackson Pollock",
    "category": 8,
    "difficulty": 2,
    "id": 39,
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
  }
}
```

## Deployment N/A

## Authors

Roland Tubongye Wabubindja.

## Acknowledgements

To our Instructor Caryn and the great team at udacity.