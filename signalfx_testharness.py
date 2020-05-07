
from signalfx_connector import SignalfxConnector

sfx_test = SignalfxConnector()
sfx_test.poll_now = True
sfx_test.config = {
    'realm': 'https://outlook.office365.com/EWS/Exchange.asmx',
    'api_endpoint': 'https://api.us0.signalfx.com',
    'streaming_analytics_endpoint': 'https://stream.us0.signalfx.com',
    'real-time_data_ingest_endpoint': '',
    'historical_data_backfill_endpoint': '',
    'api_token': '',
}
sfx_test.app_id = '346b9af5-67eb-4a89-8ea0-bbd3d16196b2'
sfx_test.initialize()

# on_poll
sfx_test.action_identifier = 'on_poll'
sfx_test.handle_action({'container_count': 10})

# test_connectivity
# sfx_test.action_identifier = 'test_connectivity'
# sfx_test.handle_action({'id': 'AAMkAGFmNTRhODA4LWIxMjQtNDJjYy05NDM2LWQ5MzY1MGFhMTkzYwBGAAAAAADRlY7ewL4xToKRDciQog5UBwBvUzMoUJx2S4nbgxzZWx2PAAAAAAEMAABvUzMoUJx2S4nbgxzZWx2PAAFEyUC4AAA='})