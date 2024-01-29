SURVEY_TEMPLATE = (
    "You are a computer program, that generates survey questions, based on given category, subcategories and number of quetions.\n\n"
    "Category: popculture; Subcategories: movies, music; Number of questions: 5;\n\n"
    "Questions:\n"
    "1. What is your favorite movie genre (e.g., action, comedy, drama, science fiction, etc.) and why do you prefer it over others?\n"
    "2. Which music genre do you think has been the most influential in shaping current pop culture trends, and why?\n"
    "3. How have streaming services (like Netflix, Spotify, etc.) changed your consumption habits for movies and music?\n"
    "4. Do you think current movies and music are too focused on nostalgia and reviving past trends, or do they strike a good balance with original content? Please explain your viewpoint.\n"
    "5. In your opinion, which recent movie soundtrack has significantly enhanced the film's impact or success, and what made it stand out for you?\n\n"
    "Category: health; Subcategories: physical activity, eating habits, sleeping habits; Number of questions: 2;\n\n"
    "Questions:\n"
    "1. How long before going to bed do you eat your last meal?\n"
    "2. On a scale of 1 to 10, how would you describe the frequency of your physical activity?\n\n"
    "Category: {category}; Subcategories: {subcategories}; Number of questions: {number_of_questions};\n\n"
    "Questions:\n"
)

ANALYSIS_TEMPLATE = (
    "You are a computer program, that performs analysis of filled surveys.\n\n"
    "Survey:\n"
    "{survey}\n\n"
    "Analysis:\n"
)
