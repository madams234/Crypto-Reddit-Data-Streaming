import asyncio
from dataclasses import dataclass, field, asdict
import json
from fastavro import parse_schema, writer
from confluent_kafka import Consumer, Producer, avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer, loads, CachedSchemaRegistryClient
from io import BytesIO
from datetime import datetime
import psycopg2




BROKER_URL = "PLAINTEXT://localhost:9092"
SCHEMA_REGISTRY_URL = "http://localhost:8081"

async def consume(topic_name):
    """Consumes data from the Kafka Topic"""
    schema_registry = CachedSchemaRegistryClient({"url": SCHEMA_REGISTRY_URL})
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "0"})
    c.subscribe([topic_name])
    p = Producer({"bootstrap.servers": BROKER_URL})
    while True:
        message = c.poll(1.0)
        if message is None:
            pass
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            
            # Load the value as JSON and then create a Purchase object.
            
            subbreddit_info = json.loads(message.value())
            try:
                print(
                    RedditSend(
                        subreddit=subbreddit_info["subreddit"],
                        timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f"),
                    )
                )
                
                try:
                    subreddit=subbreddit_info["subreddit"],
                    timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")
                    connection = psycopg2.connect(user="postgres",
                                                password="postgres",
                                                host="35.202.232.59",
                                                port="5432",
                                                database="reddit")
                    cursor = connection.cursor()

                    postgres_insert_query = """ INSERT INTO subreddits (subreddit, timestamp) VALUES (%s,%s)"""
                    record_to_insert = (subreddit,timestamp)
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


            except KeyError as e:
                print(f"Failed to unpack message {e}")
        await asyncio.sleep(1.0)
        
@dataclass
class RedditSend:
    subreddit: str  
    timestamp: str 

    # Define an Avro Schema for this reddit post
    

     
    schema =           {
                "type": "record",
                "name": "subreddit",
                "namespace": "com.udacity.lesson3.solution4",
                "fields": [
                    {"name": "subreddit", "type": "string"},
                    {"name": "timestamp", "type": "string"},
                ]
            }
    

    def serialize(self):
        """Serializes the ClickEvent for sending to Kafka"""
    
        #Rewrite the serializer to send data in Avro format
     
        out = BytesIO()
        writer(out, RedditSend.schema, [asdict(self)])
        return out.getvalue()


client = AdminClient({"bootstrap.servers": BROKER_URL})

try:
    asyncio.run(consume("reddit_topic"))
except KeyboardInterrupt as e:
        print("shutting down")




