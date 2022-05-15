"""
https://towardsdatascience.com/work-with-sql-in-python-using-sqlalchemy-and-pandas-cd7693def708
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import text
import pandas as pd
from decouple import config             # pip install python-decouple


db_url_2 = config("DB_SQLALCHEMY_PANDAS_1")   # from .env

# Have to set Future to False, otherwise it will throw an error
# engine_2 = create_engine(db_url_2, echo=False, future=True)
engine_2 = create_engine(db_url_2, echo=False, future=False)

df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})

# Insert DataFrame into an existing SQL Database Table (Database 2)
# with engine_2.connect() as conn:
#     #reate a New SQL Database
#     print(df)
#     df.to_sql('Users', con=conn)

print(df['name'])