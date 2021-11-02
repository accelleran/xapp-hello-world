import logging
import threading
import requests
import action_taker
import time


def send_handover_command(settings, handover_list):
    action_taker.trigger_handover(settings, handover_list)


def send_subband_masking_command(settings, sub_band_masking_list):
    action_taker.trigger_sub_band_selection(settings, sub_band_masking_list)


# def publish_on_kafka(out_queue, data):
#     '''
#      topic: Kafka topic where to publish the data
#      data: Data to send on the Kafka databus. This should be JSON
#     '''
#     out_queue.put(
#         {
#             'topic': topic,
#             'data': data
#         }
#     )

def create_api_url(settings, endpoint):
    with settings.lock:
        drax_ric_api_gateway_url = settings.configuration['config']['API_GATEWAY_URL']
        drax_ric_api_gateway_port = settings.configuration['config']['API_GATEWAY_PORT']

    api_url = 'http://{drax_ric_api_gateway_url}:{drax_ric_api_gateway_port}/api{endpoint}'.format(
        drax_ric_api_gateway_url=drax_ric_api_gateway_url,
        drax_ric_api_gateway_port=drax_ric_api_gateway_port,
        endpoint=endpoint
    )

    return api_url


def run(settings, in_queue, out_queue, data_store):

    # Loop
    while True:
        data = in_queue.get()

        ### YOUR CODE HERE


        ### Following is a list of examples, uncomment to test them out

        # ### Example 1: Just logging all the messages received from the dRAX Databus
        # logging.info("Received message from dRAX RIC Databus!")
        logging.info("dRAX RIC Databus message: {data}".format(data=data))

        # ### Example 2: Parsing and combining data
        # if 'type' in data:
        #     if data['type'] == 'THROUGHPUT_REPORT':
        #         data_store.setdefault(data['throughputReport']['ueRicId'], {})
        #         data_store[data['throughputReport']['ueRicId']]['dlThr'] = data['throughputReport']['dlThroughput']
        #         data_store[data['throughputReport']['ueRicId']]['ulThr'] = data['throughputReport']['ulThroughput']
        #         data_store['type'] = 'MY_TEST_TYPE'
        #     elif data['type'] == 'BLER_REPORT':
        #         data_store.setdefault(data['blerReport']['ueRicId'], {})
        #         data_store[data['blerReport']['ueRicId']]['dlBler'] = data['blerReport']['dlBler']
        #         data_store[data['blerReport']['ueRicId']]['ulBler'] = data['blerReport']['ulBler']
        #         data_store['type'] = 'MY_TEST_TYPE'
        # logging.info(data_store)


        # ### Example 3: Publishing data on the dRAX Databus
        # out_queue.put(data_store)
        # if 'type' in data:
        #     if data['type'] == 'MY_TEST_TYPE':
        #         logging.info("dRAX Databus message: {data}".format(data=data))


        ### Example 4: Send handover command
        # handover_list = [
        #     {'ueIdx': 'ueDraxId_to_handover_1', 'targetCell': 'Bt1Cell', 'sourceCell': 'Bt2Cell'},
        #     {'ueIdx': 'ueDraxId_to_handover_2', 'targetCell': 'Bt2Cell', 'sourceCell': 'Bt1Cell'}
        # ]
        # send_handover_command(settings, handover_list)


        # ### Example 5: Send subband masking command
        # sub_band_masking_list = [
        #     {'cell': 'Cell_1', 'num_of_bands': '13', 'mask': [True, True, True, True, True, True, True, True, True, True, True, True, True]},
        #     {'cell': 'Cell_2', 'num_of_bands': '9', 'mask': [True, True, True, True, True, True, True, True, True]}
        # ]
        # send_subband_masking_command(settings, sub_band_masking_list)


        # ### Example 6: How to get the configuration of a cell
        # endpoint = '/cellconfiguration/summary/Warehouse'
        # api_response = requests.get(
        #     create_api_url(settings, endpoint)
        #     )
        # # logging.info(endpoint)
        # if api_response.status_code == 200:
        #     try:
        #         logging.info(api_response.json())
        #     except:
        #         logging.warning('Failed to load JSON, showing raw content of API response:')
        #         logging.info(api_response.text)
        # else:
        #     logging.error("Failed to reach the API Gateway!")

        # ### Example 7: How to use the dRAX RIC API Gateway to get the netconf server ports
        # endpoint = '/xappconfiguration/discover/services/netconf'
        # api_response = requests.get(create_api_url(settings, endpoint))
        #
        # if api_response.status_code == 200:
        #     try:
        #         logging.info(api_response.json())
        #     except:
        #         logging.info('Failed to load JSON, showing raw content of API response:')
        #         logging.info(api_response.text)


        # ### Example 8: Get the ports where the netconf servers of cells are exposed
        # endpoint = '/xappconfiguration/discover/services/netconf'
        # api_response = requests.get(create_api_url(settings, endpoint))
        #
        # for cell, cell_info in api_response.json().items():
        #     for port in cell_info['spec']['ports']:
        #         if port['name'] == 'netconf-port':
        #             logging.info('Cell [{cell}] has NETCONF exposed on port [{port}]'.format(
        #                 cell=cell,
        #                 port=port['node_port']
        #                 )
        #             )

        # ### Example 9: How to send a Netconf RPC to the cells using the API Gateway (toggle Admin State)
        # lock_admin_state_rpc = """
        # <edit-config>
        #   <target>
        #     <running/>
        #   </target>
        #   <default-operation>none</default-operation>
        #   <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        #     <enb xmlns="http://accelleran.com/ns/yang/accelleran-enb" xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        #       <cu-cell-list>
        #         <cell>
        #           <local-cell-id>5632</local-cell-id>
        #           <oam-state-management xc:operation="replace">
        #             <admin-state>locked</admin-state>
        #           </oam-state-management>
        #         </cell>
        #       </cu-cell-list>
        #     </enb>
        #   </config>
        # </edit-config>
        # """
        # cell_instance_id = "Cell1"
        # endpoint = "/cellconfiguration/netconfrpc/{}".format(cell_instance_id)
        # headers = {'Content-Type': 'application/xml'}
        # api_response = requests.put(create_api_url(settings, endpoint), data = lock_admin_state_rpc, headers = headers)
        # if api_response.status_code == 200:
        #     try:
        #         logging.info(api_response.json())
        #     except:
        #         logging.info('Failed to send Netconf RPC:')
        #         logging.info(api_response.text)
        # else:
        #     logging.info("Received status code {} with reason {}".format(api_response.status_code, api_response.reason))


        # ### Example 10: How to send a Netconf RPC to the cells using the API Gateway (change cell PCI and reboot)
        # target_pci = 10
        # cell_id = 256
        # set_pci_rpc = """<edit-config>
        #     <target>
        #         <running/>
        #     </target>
        #     <default-operation>none</default-operation>
        #     <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        #         <enb xmlns="http://accelleran.com/ns/yang/accelleran-enb" xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        #         <cu-cell-list>
        #             <cell>
        #             <local-cell-id>{cell_id}</local-cell-id>
        #             <phy xc:operation="replace">
        #                 <physical-cell-id>{pci}</physical-cell-id>
        #             </phy>
        #             </cell>
        #         </cu-cell-list>
        #         </enb>
        #     </config>
        #     </edit-config>""".format(cell_id=cell_id, pci=target_pci)
        # reboot_rpc = """<reboot xmlns="http://accelleran.com/ns/yang/accelleran-custom-rpcs"/>"""
        # cell_instance_id = "Warehouse"
        # endpoint = "/cellconfiguration/netconfrpc/{}".format(cell_instance_id)
        # headers = {'Content-Type': 'text/xml'}
        # response = requests.put(create_api_url(settings, endpoint), data = set_pci_rpc, headers = headers)
        # if "ok" in response.text:
        #     reboot_response = requests.put(create_api_url(settings, endpoint), data = reboot_rpc, headers = headers)
        #     if not "ok" in reboot_response.text:
        #         logging.error("Could not reboot cell {}".format(cell_instance_id))
        #     else:
        #         logging.info("PCI set for cell {}. Rebooting.".format(cell_instance_id))
        # else:
        #     logging.error("Could not set pci for cell {}".format(cell_instance_id))


        # ### Example 11: How to send a Netconf RPC to the cells using the Netconf Client (get cell configuration)
        # from netconf_client.connect import connect_ssh
        # from netconf_client.ncclient import Manager
        # netconf_server_host = "10.55.1.2"   # can be discovered using the Service Monitor service (IP of the Netconf server Kubernetes Service)
        # netconf_server_port = 31380         # can be discovered using the Service Monitor service (port of the Netconf server Kubernetes Service)
        #
        # with connect_ssh(host=netconf_server_host,
        #          port=netconf_server_port,
        #          username='xapp',
        #          password='xapp') as session:
        #     mgr = Manager(session, timeout=1000)
        #     logging.info("Complete cell configuration:")
        #     logging.info(mgr.get().data_xml)


