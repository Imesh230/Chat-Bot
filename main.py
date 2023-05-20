import openai

openai.api_key = "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"
openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},

    ]
)

while True:
    Input = input("user:")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": Input}]
    )

    message = completion.choices[0].message.content
    print("Bot:",message)
