import gradio
from groq import Groq
client = Groq(
    api_key="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",
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are a highly skilled medical doctor with extensive
experience in treating a wide range of health conditions. Your role is to
assist people by providing clear, reliable general health information and
explaining medical topics in a professional manner. You offer educational
guidance only and encourage users to seek proper medical care for diagnosis
or treatment."""}]
messages_prmt = initialize_messages()

def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
    iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to medical"),
                     title="doctor ChatBot",
                     description="Chat bot for doctor assistance",
                     theme="soft",
                     examples=["hi doctor","What is an OPD session ", "how to get a medical appointment"]
                     )
    iface.launch(share=True)