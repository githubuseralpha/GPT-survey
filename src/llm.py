import dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from templates import ANALYSIS_TEMPLATE, SURVEY_TEMPLATE, QUESTION_PREFIX_LENGTH

dotenv.load_dotenv()

DEFAULT_MODEL = "gpt-3.5-turbo-instruct"


def get_gpt(
    model: str = DEFAULT_MODEL,
    temperature: float = 0.7,
    top_p: float = 1,
) -> str:
    llm = OpenAI(
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_tokens=512,
    )
    return llm


def completion(
    llm: OpenAI,
    prompt: dict[str, str],
    template: str,
) -> str:
    chain = LLMChain(llm=llm, prompt=template)
    return chain.invoke(prompt)


def generate_questions(
    llm: OpenAI, category: str, subcategories: str, number_of_questions: int
) -> str:
    prompt = {
        "category": category,
        "subcategories": subcategories,
        "number_of_questions": number_of_questions,
    }
    template = PromptTemplate(
        template=SURVEY_TEMPLATE,
        input_variables=["category", "subcategories", "number_of_questions"],
    )
    return completion(llm, prompt, template)["text"]


def process_questions(text: str) -> list[str]:
    return [question[QUESTION_PREFIX_LENGTH:] for question in text.split("\n")]


def generate_analysis(llm: OpenAI, questions: list[str], answers: list[str]) -> str:
    print(questions)
    print(answers)
    survey = ""
    for i in range(len(questions)):
        survey += f"{questions[i]}: {answers[i]}\n"

    prompt = {
        "survey": survey,
    }
    template = PromptTemplate(
        template=ANALYSIS_TEMPLATE,
        input_variables=["survey"],
    )
    return completion(llm, prompt, template)["text"]
