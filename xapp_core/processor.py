import logging
import threading
import action_taker


def get_cell_state_info_from_state_db():
    pass


def get_info_from_service_monitor():
    pass


def send_config_command_to_another_xapp():
    pass


def get_config_of_another_xapp():
    pass


def send_handover_command(handover_list, handover_nats_topic):

    action_taker.trigger_handover(handover_list, handover_nats_topic)


def send_subband_masking_command():
    pass


def publish_on_kafka(out_queue, topic, data):
    '''
     topic: Kafka topic where to publish the data
     data: Data to send on the Kafka databus. This should be JSON
    '''
    out_queue.put(
        {
            'topic': topic,
            'data': data
        }
    )


def run(settings, in_queue, out_queue, data_store):

    # Loop
    while True:
        data = in_queue.get()

        ### YOUR CODE HERE


        ### Following is a list of examples, uncomment to test them out

        ### Example 1: Just logging all the messages received from the dRAX Databus
        #logging.info("Received messgae from dRAX Databus!")
        logging.info("dRAX Databus message: {data}".format(data=data))


        # ### Example 2: Publishing one time or event-based data on the dRAX Databus
        # ###            We will publish on topic "my_test_topic", and just republish the "data" data
        # publish_on_kafka(out_queue, "my_test_topic", data)


        # ### Example 3: Periodic publishing of data
        # ###            We will save some data in the data_store and periodically publish that data_store
        # ###            We just save the data in the data_store, and the periodic_publisher thread is periodically publishing the data_store
        # ###            The settings of the periodic publishing is in the xapp_configuration and can be real-time configured
        # data_store = data

        # ### Example 4: Send handover command
        # handover_list = [
        #     {'ueIdx': 'ueRicId_to_handover', 'targetCell': 'Bt1Cell', 'sourceCell': 'Bt2Cell'}
        # ]
        # send_handover_command(settings, handover_list)


        ### Example 5: Send subband masking command
        # TODO

        ### Example 6: Get config of another xApp
        # TODO

        ### Example 7: Send a command to change the config of another xApp
        # TODO

        ### Example 8: Get info from the service monitor
        # TODO

        ### Example 9: Get state info from state DB
        # TODO
