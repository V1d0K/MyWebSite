import streamlit as st
import pandas as pd
import numpy as np
import psycopg2

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(st.secrets["db_connection_str"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from game_sales;")
select = run_query("SELECT year, COUNT(game) from game_sales group by year;")

# Print results.
dataframe =pd.DataFrame(rows)
df2 = pd.DataFrame(select)
st.write(dataframe)
st.write(df2)
fig=df2.hist('juegos')
st.pyplot(fig)

# game_df.apply(lambda x: x.sort_values(by = '4', ascending=False)).head(10)