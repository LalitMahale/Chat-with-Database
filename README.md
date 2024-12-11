---
title: Chat With Database
emoji: 😻
colorFrom: red
colorTo: purple
sdk: streamlit
sdk_version: 1.41.0
app_file: app.py
pinned: false
license: mit
---

# 🚀 Chat with Database 🚀

## Overview
"Chat with Database" is an innovative tool that bridges the gap between natural language and SQL. It allows users to query databases simply by typing in everyday language, with the system translating it into SQL queries and displaying the results. This project empowers non-technical users to access and manipulate data with ease, making data insights accessible to everyone.

## Features
- **Natural Language Querying**: Users can type queries in plain language, and the tool translates them into SQL commands.
- **Intent Understanding**: The system interprets the user’s intent, converting it into the right SQL syntax.
- **Data Retrieval & Display**: Retrieves data from the database and presents it in an easy-to-read format.
- **User-Friendly**: Makes database interaction accessible to users with minimal technical skills.

## Why This Matters
"Chat with Database" saves time and unlocks new insights by making data retrieval as simple as sending a text. No SQL knowledge is needed, making it ideal for analysts, business users, and teams seeking data-driven decisions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/chat-with-database.git
   ```
2. Navigate into the project directory:
   ```bash
   cd chat-with-database
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Database Credentials and API Key**:
   - Open `config.py`.
   - Add your **database credentials** and **Gemini API key** in the format below:

   ```python
   # config.py
   db_configuration = {
       "USER": "your_database_user",
       "PASSWORD": "your_database_password",
       "PORT": "your_database_port",
       "DB": "your_database_name",
       "HOST": "your_database_host"
   }

   API_KEY = "your_gemini_api_key"
   ```


## Usage
1. Start the application:
   ```bash
   streamlit run app.py
   ```
2. Type in your data queries in natural language, and the system will automatically generate and execute SQL queries, returning results in a user-friendly format.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

👉 **Check it out on GitHub:** [Chat with Database]([https://github.com/LalitMahale/Chat-with-Database])

