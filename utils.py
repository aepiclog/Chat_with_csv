from langchain_openai import ChatOpenAI, OpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

llm_chat = ChatOpenAI(temperature=0.1, model_name='gpt-3.5-turbo')


def initialize_dataset(file_path):
    df = pd.read_csv(file_path)
    return (df)


def generate_summary_prompt(df):
    speech = ""
    for col_name in list(df.columns):
        speech += col_name + "\n" + str(df[col_name].describe()) + "\n\n\n"
    return [speech, str(df.head())]


def get_response(speech):
    chat_messages = [
        SystemMessage(
            content='You are an expert assistant with expertize in Data Analysis'),
        HumanMessage(
            content=f'Please provide a breif summary of the following Dataset in 150-200 Words:\n {speech[0]} \n And The Dataset Looks like This {speech[1]}')
    ]
    return llm_chat(chat_messages)


def get_desc(file_path):
    df = initialize_dataset(file_path)
    temp = df.apply(pd.to_numeric, errors='coerce')
    temp = temp.dropna(axis=1)

    return temp.describe().iloc[:3]


def init_conversation(file_path):
    agent = create_csv_agent(
        llm_chat,
        file_path,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

    return agent


def get_answer(query, agent):
    answer = agent.run(query)
    return (answer)


def get_summary(file_path):
    df = initialize_dataset(file_path)
    speech = generate_summary_prompt(df)

    summary = get_response(speech)

    return (summary.content)
