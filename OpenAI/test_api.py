import openai

client = openai.OpenAI(api_key="*******")

response = client.completions.create(
    model="gpt-3.5-turbo",
    prompt="Chi ha creato il linguaggio Python?",
    temperature=0.7,
    max_tokens=100,
)

print(response["choices"][0]["text"]) #primo risultato del dizionario
