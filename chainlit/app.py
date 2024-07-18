import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
from langchain_community.llms import Ollama


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Hello there, I am Ollama. How can I help you ?").send()
    model = Ollama(model="llama3:8b", base_url="http://ollama-container:11434")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert in python code, every time you write a function you"
                "try to respect code conventions like PEP8",
            ),
            (
                "human",
                "{question}",
            ),
        ],
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
