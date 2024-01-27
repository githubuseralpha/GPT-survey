import dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

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
    prompt: str,
    template: str,
) -> str:
    chain = LLMChain(llm=llm, prompt=template)
    return chain.invoke(prompt)

if __name__ == "__main__":
    prompt = "Why do you like The Matrix?"
    template = """
    Human: What's your favorite movie?
    AI: I like The Matrix.
    Human: {question}
    AI: 
    """
    template = PromptTemplate(template=template, input_variables=["question"])
    llm = get_gpt()
    print(completion(llm, prompt, template))
