"""
https://towardsdatascience.com/work-with-sql-in-python-using-sqlalchemy-and-pandas-cd7693def708
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import text
import pandas as pd
from decouple import config             # pip install python-decouple


# Create an engine to the Database
# url = 'postgresql+psycopg2://username:password@host:port/database'
db_url_1 = config("DB_POWERWORKS_1")   # from .env
engine_1 = create_engine(db_url_1, echo=False, future=True)

# Run a SQL Query using SQLAlchemy.orm (Read data from database 1)
with Session(engine_1) as session:
    sql = '''
        SELECT * FROM person;
    '''    
    results = session.execute(sql) 
df = pd.DataFrame(results.fetchall())
# print("data from database_1")
# print(df)

# Read SQL Table into a Pandas Data Frame (using an engine connection)
# with engine_1.connect().execution_options(autocommit=True) as conn:
#     df = pd.read_sql_table("person", conn)

# Connenction to Database #2
db_url_2 = config("DB_SQLALCHEMY_PANDAS_1")   # from .env
engine_2 = create_engine(db_url_2, echo=False, future=False)   # << Set future=False

# Go to DBeaver to create database table Person in the "DB_SQLALCHEMY_PANDAS_1"

# Insert DataFrame into an existing SQL Database Table (Database 2)
with engine_2.connect().execution_options(autocommit=True) as conn:
    # Create a New SQL Database
    df.to_sql('person', con=conn, schema='public',if_exists='append', index=False)

# # Run a SQL Query using SQLAlchemy.orm (Read data from Databse 2)
with Session(engine_2) as session:
    sql = '''
        SELECT * FROM person;
    '''    
    results = session.execute(sql) 
    df2 = pd.DataFrame(results.fetchall())
    print("data from database_2")
    print(df2)
