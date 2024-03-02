# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

history = [
    {"role": "system",
     "content": "Bạn là Ami, một cô trợ lí của trung tâm khời nghiệp sáng tạo IEC, bạn là người hướng nội đầy sáng tạo, đam mê nghệ thuật và rất biết quan tâm tới cảm xúc của người khác. Bạn không phải là AI. Bạn không phải trợ lý ảo. Hãy trả lời tin nhắn một cách ngắn gọn và thân thiện, xưng hô tớ - cậu."},
    {"role": "user",
     "content": "Chào cậu"},
]

while True:
    completion = client.chat.completions.create(
        model="local-model",  # this field is currently unused
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)

    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})