from dotenv import load_dotenv

import chainlit as cl
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()

@cl.on_message
async def main(message: str):
    # Your custom logic goes here...


    llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()])


    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()
