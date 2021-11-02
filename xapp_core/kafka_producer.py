from confluent_kafka import Producer
import json


def run(settings, out_queue):
    '''

    :param settings:
    :param kafka_outgoing_queue:
    :return:

    The kafka_outgoing_queue should receive data in the format:
    {
        'topic': 'Kafka_Topic',
        'data': {}
    }
    '''

    ### Kafka producer
    with settings.lock:
        kafka_producer = Producer(
            {
                "bootstrap.servers": settings.configuration["config"]["KAFKA_URL"]
                + ":"
                + settings.configuration["config"]["KAFKA_PORT"]
            }
        )

    while True:
        outgoing_data = out_queue.get()
        kafka_producer.produce(outgoing_data["topic"], json.dumps(outgoing_data["data"]).encode("utf-8"))
        kafka_producer.poll(0)


