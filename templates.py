QUESTION_PREFIX_LENGTH = 3

SURVEY_TEMPLATE = (
    "You are a robot, that generates survey questions, based on given category, "
    "subcategories and number of quetions. \n\n"
    "Category: popculture; Subcategories: movies, book; Number of questions: 5 \n\n"
    "Questions: \n"
    "1. What is your favorite movie? \n"
    "2. What is your favorite book? \n"
    "3. Who is your favorite movie character? \n"
    "4. Who is your favorite book writer \n"
    "5. What is your favorite movie genre? \n\n"
    "Category: {category}, Subcategories: {subcategories}, Number of questions: {number_of_questions} \n\n"
    "Questions: \n"
)

ANALYSIS_TEMPLATE = (
    "You are a robot, that performs analysis of filled surveys. \n\n"
    "survey: \n"
    "{survey} \n\n"
    "analysis: \n"
)
