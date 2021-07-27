import time
import logging

def run(settings, out_queue, data, final_out_queue):
    logging.info('Starting periodic publisher thread...')
    while True:
        # Lock settings and get the settings
        with settings.lock:
            periodic_publish = settings.configuration['config']['periodic_publish']
            kafka_producer_topic = settings.configuration['config']['kafka_producer_topic']
            publish_interval = settings.configuration['config']['publish_interval']

        # If periodic publish is enabled, publish on kafka
        if periodic_publish:
            msg = out_queue.get()

            msg = {'topic': kafka_producer_topic, 'data': msg}
            final_out_queue.put(msg)

            time.sleep(publish_interval)
