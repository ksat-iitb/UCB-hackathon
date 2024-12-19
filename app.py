from source.embedding.gemini import GeminiEmbedding
from source.inference.gemini import ChatGemini
from source.agent.web import WebSearchAgent
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv('GOOGLE_API_KEY')
llm=ChatGemini(model='gemini-1.5-flash',api_key=api_key,temperature=0)
embedding=GeminiEmbedding(model='text-embedding-004',api_key=api_key)

agent=WebSearchAgent(llm=llm,embedding=embedding,browser='edge',verbose=True,strategy='combined',headless=False,incognito=True,screenshot=False)
user_query=input('Enter your query: ')
agent_response=agent.invoke(user_query)
print(agent_response)