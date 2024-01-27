import dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from templates import survey_template, QUESTION_PREFIX_LENGTH

dotenv.load_dotenv()
DEFAULT_MODEL = "gpt-3.5-turbo-instruct"


def get_gpt(
    model: str = DEFAULT_MODEL,
    temperature: float = 0.6,
    top_p: float = 0.9,
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
        template=survey_template,
        input_variables=["category", "subcategories", "number_of_questions"],
    )
    return completion(llm, prompt, template)


def process_questions(answer: str) -> list[str]:
    return [question[QUESTION_PREFIX_LENGTH:] for question in answer["text"].split("\n")]


if __name__ == "__main__":
    llm = get_gpt()
    answer = generate_questions(llm, "food", "restaurants, cooking", 3)
    print(process_questions(answer))
