import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


db_connection = mysql.connector.connect(
    host=os.environ.get('HOST'),
    port=3306,
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASS'),
    autocommit=True,
    collation='utf8mb3_general_ci'
)

