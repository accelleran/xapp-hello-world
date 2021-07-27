configuration = {
    "metadata": {
        "name": "xApp Name",
        "configName": "",
        "namespace": "default"
    },
    "description": "xApp Description...",
    "last_modified": "06/07/2020 23:32:00",
    'config': {
        'REDIS_URL': '',
        'REDIS_PORT': 0,
        'LOG_LEVEL': 20,  # CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10, NOTSET=0
        'KAFKA_URL': '10.20.20.20',
        'KAFKA_PORT': '31090',
        'API_GATEWAY_URL': '',
        'API_GATEWAY_PORT': '',
        'DRAX_COMMAND_TOPIC': 'Topic_OPENRAN_COMMANDS.OranController',
        'NATS_URL': 'nats://10.20.20.20:31000',
        'kafka_producer_topic': 'test_xapp_topic',
        'KAFKA_LISTEN_TOPICS': 'test2, Topic_State',
        'periodic_publish': True,
        'publish_interval': 1  # in seconds
    },
    "jsonSchemaOptions": {},
    "uiSchemaOptions": {}
}
