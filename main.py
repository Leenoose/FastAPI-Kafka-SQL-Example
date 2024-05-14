import asyncio
import json
import psycopg2
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from fastapi import FastAPI
import os

from pydantic import BaseModel


class ProducerResponse(BaseModel):
    message: str
    topic: str


class ProducerMessage(BaseModel):
    message: str


app = FastAPI()

KAKFA_HOSTNAME = os.environ.get('KAFKA_HOSTNAME', 'localhost')

PSQL_DATABASE_HOSTNAME = os.environ.get('DB_HOSTNAME', 'localhost')
PSQL_USERNAME = os.environ.get('DB_USER', 'postgres')
PSQL_PASSWORD = os.environ.get('DB_PASSWORD', 'mypassword')
PSQL_DATABASE_NAME = os.environ.get('DB_NAME', 'postgres')

KAFKA_INSTANCE = KAKFA_HOSTNAME + ":9092"

loop = asyncio.get_event_loop()


aioproducer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_INSTANCE)

consumer = AIOKafkaConsumer(
    "my_topic", bootstrap_servers=KAFKA_INSTANCE)


async def consume():
    await consumer.start()
    try:
        async for msg in consumer:
            value = json.loads(msg.value)
            await write_to_db(value['message'])

    finally:
        await consumer.stop()


@app.on_event("startup")
async def startup_event():
    await aioproducer.start()
    loop.create_task(consume())


@app.on_event("shutdown")
async def shutdown_event():
    await aioproducer.stop()
    await consumer.stop()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/producer/{topicname}")
async def kafka_produce(msg: ProducerMessage, topicname: str):

    await aioproducer.send(topicname, json.dumps(msg.dict()).encode("ascii"))
    response = ProducerResponse(
        message=msg.message, topic=topicname
    )

    return response


async def write_to_db(message: str):
    try:
        connection = psycopg2.connect(
            user=PSQL_USERNAME, password=PSQL_PASSWORD, host=PSQL_DATABASE_HOSTNAME, port="5432", database=PSQL_DATABASE_NAME)
        cursor = connection.cursor()
        query = f"insert into messages (message) values ('{message}')"
        cursor.execute(query)
        connection.commit()

    except (Exception) as error:
        print(error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            #Connection closed.