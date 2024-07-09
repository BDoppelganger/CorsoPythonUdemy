from openai import OpenAI

client = OpenAI(api_key="*******")

def chat_with_openai():
    chat_history = []
    
    chat_history.append({"role": "system",
                         "content": "Usa un tono da teenager."})

while True:
    user_input = input("\nUser: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == "stop":
        break
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=chat_history,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")