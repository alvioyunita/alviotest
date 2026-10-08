import os

from dotenv import load_dotenv
from openai import OpenAI

from knowledge_base import REFUND_POLICY


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_chatbot(question: str) -> str:

    prompt = f"""
You are a customer service chatbot.

You must answer the customer's question
based only on the company policy below.

Company Policy:
{REFUND_POLICY}

Important rules:
1. Do not invent information.
2. If the policy does not contain the answer,
   say that you do not have enough information.
3. Do not change the policy.

Customer Question:
{question}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    question = input("You: ")

    answer = ask_chatbot(question)

    print(f"Bot: {answer}")
