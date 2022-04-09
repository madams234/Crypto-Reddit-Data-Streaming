import yliveticker
import psycopg2


# this function is called on each ticker update
def on_new_msg(ws, msg):
    info = msg
    ticker = info['id']
    timestamp = info['timestamp']
    price = info['price']
    changepercent = info['changePercent']
    print(ticker)
    print(timestamp)
    print(price)
    print(changepercent)
    try:
                    connection = psycopg2.connect(user="postgres",
                                                password="postgres",
                                                host="35.202.232.59",
                                                port="5432",
                                                database="reddit")
                    cursor = connection.cursor()

                    postgres_insert_query = """ INSERT INTO crypto (ticker, timestamp, price, changepercent) VALUES (%s,%s,%s,%s)"""
                    record_to_insert = (ticker,timestamp,price,changepercent)
                    cursor.execute(postgres_insert_query, record_to_insert)

                    connection.commit()
                    count = cursor.rowcount
                    print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
                print("Failed to insert record into mobile table", error)

    finally:
                # closing database connection.
                if connection:
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

yliveticker.YLiveTicker(on_ticker=on_new_msg, ticker_names=[
    "BTC-USD","ETH-USD","ADA-USD","SOL-USD","XRP-USD","DOGE-USD","USDT","USD","BUSD","USD"])



