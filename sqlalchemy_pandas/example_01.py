"""
https://towardsdatascience.com/work-with-sql-in-python-using-sqlalchemy-and-pandas-cd7693def708
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, aliased
import pandas as pd
from decouple import config             # pip install python-decouple


# Create Connection to the Database
# url = 'postgresql+psycopg2://username:password@host:port/database'
db_url = config("DB_POWERWORKS_1")   # from .env
engine = create_engine(db_url, echo=False, future=True)

# Run a SQL Query using SQLAlchemy.orm
with Session(engine) as session:
    sql = '''
        SELECT * FROM person;
    '''    
    results = session.execute(sql) 
    df = pd.DataFrame(results.fetchall())
    print(df)

# Read SQL Table into a Pandas Data Frame (using an engine connection)
# conn = engine.connect()
# df2 = pd.read_sql_table("person", conn)
# print(df2)
# conn.close()

# Insert DataFrame into an Existing SQL Database


#