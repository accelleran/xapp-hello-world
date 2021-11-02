import logging
import oranCommand_pb2
from pynats import NATSClient


def create_handover_command_message(ueIdx, targetCell, sourceCell):
    peer_msg = oranCommand_pb2.OpenRAN_commandMessage()
    peer_msg.messageType = 1
    peer_msg.originator = 'HandoverManager'

    handover = oranCommand_pb2.OpenRan_UeHandoverCommand()
    handover.ueRicId = ueIdx
    handover.targetCell = targetCell
    handover.sourceCell = sourceCell

    peer_msg.handover.CopyFrom(handover)

    return peer_msg


def create_subband_masking_command_message(cell, num_bands, masking):
    peer_msg = oranCommand_pb2.OpenRAN_commandMessage()
    peer_msg.messageType = 6
    peer_msg.originator = 'SubbandMaskingController'

    subband_masking = oranCommand_pb2.OpenRAN_SubBandMaskrequest()
    subband_masking.cell = cell
    subband_masking.numBands = int(num_bands)

    subband_masking.mask.extend(masking)

    peer_msg.subBandMaskrequest.CopyFrom(subband_masking)

    return peer_msg


def nats_publish(nats_url, msg, topic):
    msg_to_send = msg.SerializeToString()
    with NATSClient(nats_url) as client:
        client.publish(topic, payload=msg_to_send)


def trigger_handover(settings, handover_list):
    logging.info("Triggering the handovers...")

    # Trigger all handover
    for item in handover_list:
        # Create the peer_msg containing the handover request
        peer_msg = create_handover_command_message(item['ueIdx'], item['targetCell'], item['sourceCell'])

        # Read settings
        with settings.lock:
            nats_url = settings.configuration['config']['NATS_URL']
            drax_cmd_topic = settings.configuration['config']['DRAX_COMMAND_TOPIC']

        # Send the message to NATS
        nats_publish(nats_url, peer_msg, drax_cmd_topic)

        logging.info("Sent handover command to move UE [{ue_id}] from [{serving_cell}] to [{target_cell}]".format(
            ue_id=item['ueIdx'],
            serving_cell=item['sourceCell'],
            target_cell=item['targetCell']
        ))


def trigger_sub_band_selection(settings, sub_band_masking_list):
    logging.info("Triggering the sub-band masking...")

    # Trigger all sub-band masking commands
    for item in sub_band_masking_list:
        # Create the peer_msg containing the handover request
        peer_msg = create_subband_masking_command_message(item['cell'], item['num_of_bands'], item['mask'])

        # Read settings
        with settings.lock:
            nats_url = settings.configuration['config']['NATS_URL']
            drax_cmd_topic = settings.configuration['config']['DRAX_COMMAND_TOPIC']

        # Send the message to NATS
        nats_publish(nats_url, peer_msg, drax_cmd_topic)

        logging.info("Subband masking applied for cell [{cell}]: {mask}".format(
            cell=item['cell'],
            mask=item['mask']
        ))

