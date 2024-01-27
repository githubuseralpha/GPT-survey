survey_template = (
    "You are a robot, that generates survey questions, based on given category, "
    "subcategories and number of quetions. \n\n"
    "Category: popculture; Subcategories: movies, book; Number of questions: 5 \n\n"
    "Questions: \n"
    "1. What is your favorite movie? \n"
    "2. What is your favorite book? \n"
    "3. Who is your favorite movie character? \n"
    "4. Who is your favorite book writer \n"
    "5. What is your favorite movie genre? \n"
    "Category: {category}, Subcategories: {subcategories}, Number of questions: {number_of_questions} \n\n"
    "Questions: \n"
)

QUESTION_PREFIX_LENGTH = 3
