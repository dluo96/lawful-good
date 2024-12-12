from openai import OpenAI

openai_api_key = ...
openai_api_base = "https://api.lambdalabs.com/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

model = "llama3.1-70b-instruct-berkeley"


if __name__ == "__main__":
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": "What is the capital of the country Georgia?"
        }],
        model=model,
    )

    print(chat_completion)
    print(client.models.list())
