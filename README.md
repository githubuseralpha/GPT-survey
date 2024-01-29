## Setup

Recommended Python Version: 3.10.

Libraries installation:

    python -m pip install -r requirements.txt

or

    python3 -m pip install -r requirements.txt

Depending on OS.

**You also need to provide your OpenAI API key in .env file.**

## Run

    python src/app.py

or

    python3 src/app.py

Depending on OS. By default the application will start on localhost:5000.

# Overview

Here is overview of some decisions and solutions used in this projects:
1. I am using different values of temperature and top_p for question generation and analysis. For question generation I have chosen small values for these parameters to make sure that GPT will follow the given pattern. For analysis I provided greater values to ensure creativity. Values for these parameters can be found and changed in config file.
2. The model used by default is GPT 3.5 turbo, but it can be easily changed in config file.
3. At the moment, the application offers basic survey generation functionality based on selected categories and subcategories. In a real application, however, the following would be necessary: a user system, saving the generated surveys into a database and the possibility of sharing surveys with other users.

