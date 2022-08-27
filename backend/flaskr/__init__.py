import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    cors = CORS(app, resources={r"*api/*": {"origins": "*"}})

    # TODO: Use the after_request decorator to set Access-Control-Allow

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')

        return response

    # TODO:Create an endpoint to handle GET requests for all available categories.

    @app.route('/categories', methods=['GET'])
    @cross_origin()
    def get_categories():
        categories = [category.format() for category in Category.query.all()]

        return jsonify({
            'success': True,
            'categories': categories,
            'total_categories': len(categories)
        })

    # TODO: Create an endpoint to handle GET requests for questions, including pagination (every 10 questions).
    #  This endpoint should return a list of questions,number of total questions, current category, categories.

    """
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.route('/questions', methods=['GET'])
    @cross_origin()
    def get_questions():
        selection = Question.query.order_by(Question.id).all()

        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = [question.format() for question in selection]
        current_questions = questions[start:end]

        categories = [category.format() for category in Category.query.all()]

        if len(current_questions) == 0:
            return not_found(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'categories': categories,
            'current_category': None
        })

    # TODO: Create an endpoint to DELETE question using a question ID.
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    @cross_origin()
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()
            if question is None:
                return not_found(404)

            question.delete()

            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': [question.format() for question in Question.query.all()],
                'total_questions': len(Question.query.all()),
                'categories': [category.format() for category in Category.query.all()],
                'currentCategory': None
            })

        except:
            return unprocessable(422)

    """
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    # TODO: Create an endpoint to POST a new question, which will require the question and answer text, category,
    #  and difficulty score.
    @app.route('/questions', methods=['POST'])
    @cross_origin()
    def create_question():
        body = request.get_json()
        search = body.get('searchTerm', None)

        try:
            if search:
                query = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
                questions = [question.format() for question in query]

                return jsonify({
                    'success': True,
                    'questions': questions,
                    'total_questions': len(query.all())

                })
            else:
                question = Question(
                    question=body.get('question', None),
                    answer=body.get('answer', None),
                    category=body.get('category', None),
                    difficulty=body.get('difficulty', None),
                )
                question.insert()

                return jsonify({
                    'success': True,
                    'created': question.id,
                    'questions': [question.format() for question in Question.query.all()],
                    'total_questions': len(Question.query.all())
                })
        except:
            return unprocessable(422)

    """
    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    # TODO: Create a POST endpoint to get questions based on a search term.
    #  It should return any questions for whom the search term is a substring of the question.

    """
    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    # TODO: Create a GET endpoint to get questions based on category.
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    @cross_origin()
    def question_by_category(category_id):
        category = Category.query.filter(Category.id == category_id).first()
        if category is None:
            return not_found(404)

        questions = Question.query.filter(Question.category == category_id).all()
        current_questions = [question.format() for question in questions]

        if questions is None:
            return not_found(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'category': category.format(),
            'total_questions': len(current_questions),

        })

    """
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    # TODO: Create a POST endpoint to get questions to play the quiz.
    #  This endpoint should take category and previous question parameters
    #  and return a random questions within the given category,
    #  if provided, and that is not one of the previous questions.
    def get_random_question(previous_questions, questions):
        if previous_questions:
            for previous_question in previous_questions:
                questions.remove(previous_question)
        if not questions:
            return []

        return random.choice(questions)

    @app.route('/quizzes', methods=['POST'])
    @cross_origin()
    def next_question():
        body = request.get_json()
        previous_questions = body.get('previous_questions', None)

        if type(body.get('quiz_category', None).get('type')) == str:
            questions = Question.query.all()
            all_questions = [question.format() for question in questions]

            current_question = get_random_question(previous_questions, all_questions)

        else:
            category_id = body.get('quiz_category', None).get('type').get('id')

            questions = Question.query.filter(Question.category == category_id).all()
            category_questions = [question.format() for question in questions]

            current_question = get_random_question(previous_questions, category_questions)

        return jsonify({
            'currentQuestion': current_question
        })

    """
    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    # TODO: Create error handlers for all expected errors including 404 and 422.
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.route('/categories', methods=['POST'])
    @cross_origin()
    def create_category():
        body = request.get_json()

        try:
            category = Category(
                type=body.get('type', None),
            )
            category.insert()

            return jsonify({
                'success': True,
                'created': category.id,
                'categories': [category.format() for category in Category.query.all()],
                'total_categories': len(Category.query.all())
            })
        except:
            return unprocessable(422)

    return app