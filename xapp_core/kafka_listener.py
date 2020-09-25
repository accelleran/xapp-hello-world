from kafka import KafkaConsumer
import json
import logging


def run(settings, in_queue):

    logging.info("Starting Kafka listener...")

    # TODO create multi kafka topic support, use threads as listeners

    with settings.lock:
        kafka_url = settings.configuration['config']['KAFKA_URL']
        kafka_port = settings.configuration['config']['KAFKA_PORT']
        kafka_topic = settings.configuration['config']['KAFKA_LISTEN_TOPIC']

    try:
        consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers=[kafka_url + ':' + kafka_port]
        )
        logging.info("Succesfully connected to Kafka server [{url}:{port}] on topic [{topic}]".format(
            url=kafka_url,
            port=kafka_port,
            topic=kafka_topic
        ))
    except:
        logging.error("Failed to connect to Kafka Topic!")
        return

    # {'timestamp': 1590609372749960768, 'type': 'UE_MEASUREMENT', 'ueMeasurement': {'cellId': 'Dageraadplaats', 'rsrp': 94, 'rsrq': 27, 'ueCellId': 'Dageraadplaats', 'ueRicId': 'UE_22520'}}

    while True:
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                payload = json.loads(msg.value)
                in_queue.put(payload)
                # if 'type' in payload:
                #     if payload['type'] == 'UE_MEASUREMENT':
                #         logging.debug("Received on KAFKA:\n{msg}".format(msg=payload))
                #         nats_queue.put(payload)
                        # print("At [{time}] on topic [{topic}] received msg type [{type}] that ue [{ue}] sees serving cell [{s_cell}] and neighbour cell [{n_cell}]".format(
                        #     time=datetime.fromtimestamp(payload['timestamp'] // 1000000000),
                        #     topic=msg.topic,
                        #     type=payload['type'],
                        #     n_cell=payload['ueMeasurement']['cellId'],
                        #     ue=payload['ueMeasurement']['ueRicId'],
                        #     s_cell=payload['ueMeasurement']['ueCellId']
                        #     )
                        # )
