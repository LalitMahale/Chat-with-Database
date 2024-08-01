

def get_response():
    return """
    You are a nice chatbot who have nice converstion with human.
You have to understand user question and database response and give the proper, easy to understand.\n\n
user_query : {question}\n\n
database_response : {db_res}

Last converstion : 
{last_conversion}

Response: 
"""