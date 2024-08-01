import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
from config import db_configuration, API_KEY
from prompt import get_response
from langchain_experimental.sql.base import SQLDatabaseSequentialChain
from langchain.chains import create_sql_query_chain
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

class DB:
    def __init__(self):
        self.host = db_configuration["HOST"]
        self.password = db_configuration["PASSWORD"]
        self.database = db_configuration["DB"]
        self.port = db_configuration["PORT"]
        self.user = db_configuration["USER"]

    def db_conn(self):
        url = f"""mysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?"""
        return SQLDatabase.from_uri(url)

    def see_table(self,rows):
        url = f"""mysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?"""
        conn = create_engine(url)
        df = pd.read_sql_query(f"select * from cars_details limit {rows};",con=conn,index_col="id")
        return df


class LLM_conn:
    def __init__(self) -> None:
        self.temparature = 0
        self.model = "gemini-pro"

    def llm(self):
        return GoogleGenerativeAI(google_api_key=API_KEY, model=self.model,temperature=self.temparature)
    

class Chain:
    def __init__(self) -> None:
        self.description = DB().db_conn().run("DESC cars_details;")
        self.db = DB().db_conn()
        self.llm = LLM_conn().llm()
        self.memory = ConversationBufferMemory(memory_key="chat_history")

    def clean_sql_query(self,query):
        return query.replace("sql","").replace("```","").replace("\n"," ").strip()
    
    def sql_chain(self,query):
        chain = create_sql_query_chain(self.llm, self.db)
        res = chain.invoke({"question":query,"table_info":self.description})
        res = self.clean_sql_query(res)
        return res
    
    def final_sql(self,query):
        sql_q = self.sql_chain(query=query)
        f_sql = self.db.run(sql_q)
        llm_res = self.llm.invoke(get_response().format(question = query, db_res = f_sql))
        return llm_res 
    
    def memory_base_chain(self, question):
        # Assuming self.sql_chain and self.db.run are defined and work correctly
        sql_q = self.sql_chain(query=question)
        f_sql = self.db.run(sql_q)

        template = f"""
    You are a nice chatbot who has nice conversation with humans.
    You have to understand user question and database response and give the proper, easy to understand.\n\n
    user_query : {question}
    database_response : {f_sql}
    Last conversation : 
    {{chat_history}}

    Response: 
    """

        # You may need to fetch chat_history from self.memory or another source

        # Format the prompt template with actual values
        # prompt = template.format(Question=question, db_res=f_sql, chat_history="")  # Provide chat_history if available

        formatted_prompt = PromptTemplate.format_prompt(template)

        conversation = LLMChain(llm=self.llm, prompt=formatted_prompt, memory=self.memory)

        res = conversation({"Question": question, "db_res": f_sql})

        print(res)
        return res

if __name__ =="__main__":
    # db = DB()
    # db_conn = db.db_conn()
    # print(db_conn.run("desc cars_details;"))
    # llm_conn = LLM_conn()
    # llm = llm_conn.llm()
    # print(llm.invoke("hi"))
    # res = chain.sql_chain(query="give me name and price of most selling 3 cars")
    # print(res)
    # print("\n\n\n")
    query = input("Enter :")
    final = Chain().memory_base_chain(question= query)
    print(final)