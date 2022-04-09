import plotly.express as px
import psycopg2
import pandas as pd


try:
    conn = psycopg2.connect(user="postgres",
                                                    password="postgres",
                                                    host="35.202.232.59",
                                                    port="5432",
                                                    database="reddit")

    cur = conn.cursor()
    query1 = "select * from crypto where created_at between now()-interval '1 hours' and now() and ticker = 'BTC-USD' order by created_at desc"
    query2 = "select * from subreddits where created_at between now()-interval '1 hours' and now() order by created_at desc"
    cur.execute(query1)
    cryptoDF = pd.DataFrame(cur.fetchall(),columns = ['ticker','timestamp','price','changepercent','created_at'])
    cur.execute(query2)
    subredditDF = pd.DataFrame(cur.fetchall(),columns= ['subreddit','timestamp','created_at'])

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")



fig = px.line(cryptoDF, x="created_at", y="price", title='Bitcoin Price')
fig.show()
figure = px.bar(subredditDF, x='subreddit')
figure.show()
