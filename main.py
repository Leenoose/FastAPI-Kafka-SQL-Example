import asyncio
import json

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from fastapi import FastAPI

import psycopg2
from psycopg2 import Error

from pydantic import BaseModel, StrictStr


class ProducerResponse(BaseModel):
    name: StrictStr
    topic: StrictStr


class ProducerMessage(BaseModel):
    message: StrictStr


app = FastAPI()

KAFKA_INSTANCE = "localhost:9092"


loop = asyncio.get_event_loop()


aioproducer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_INSTANCE)

consumer = AIOKafkaConsumer(
    "quickstart-events", bootstrap_servers=KAFKA_INSTANCE, loop=loop)


async def consume():
    await consumer.start()
    # Write message to database.
    queries = []
    try:
        async for msg in consumer:
            response = json.loads(msg.value.decode('utf-8'))
            print(
                "consumed: ",
                response['message']
            )
            query = f"insert into messages (message) values ('{response['message']}')"
            queries.append(query)

    finally:
        await consumer.stop()
        try:
            connection = psycopg2.connect(
                user="postgres", password="mypassword", host="localhost", port="5432", database="postgresql")
            cursor = connection.cursor()

            for query in queries:
                cursor.execute(query)
                connection.commit()

        except (Exception, Error) as error:
            print(error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                # Connection closed.


# cannot access local variable 'connection' where it is not associated with a value.
# Look into trying to run database connection and command while running an async function to wait for message.

    # try:
    #     async for msg in consumer:
    #         response = json.loads(msg.value.decode('utf-8'))
    #         query = f"insert into messages (message) values ('{response['message']}')"
    #         print("consumed: ", response['message'])

    #     connection = psycopg2.connect(
    #         user="postgres", password="mypassword", host="localhost", port="5432", database="postgresql")
    #     cursor = connection.cursor()
    #     cursor.execute(query)
    #     connection.commit()

    # except (Exception, Error) as error:
    #     print(error)
    # finally:
    #     if (connection):
    #         cursor.close()
    #         connection.close()
    #         # Connection closed.
    #         await consumer.stop()


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
        name=msg.message, topic=topicname
    )

    return response
