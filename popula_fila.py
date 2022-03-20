import json
import boto3
from botocore.credentials import BaseAssumeRoleCredentialFetcher
QUEUE_DEST = 'bundle-router-queue'
sqs_client = boto3.resource('sqs', region_name='us-west-2')
queue_dest = sqs_client.get_queue_by_name(QueueName=QUEUE_DEST)
for i in range(0, 1000):
    message = dict()
    data = dict()
    message["userId"] = "5521967813698"
    message["offer"] = "DISCOVERY3"
    message["serviceId"] = 2184
    message["bundleId"] = "e9a3dbc4-07a4-4ac6-b799-0257e1015665"
    message["planType"] = "POS"
    message["type"] = "BUNDLE"
    message["suspend"] = False
    message["externalTransactionId"] = "d9d732b4-8252-44cc-br97-b15d26f36234"
    message["eventName"] = "INSERT"
    message["transactionId"] = None
    message["enrollable"] = None
    message["integrationTarget"] = "PROVIDER"
    message["relationshipId"] = "e9a3dbc4-07a4-4ac6-b799-0257e1015665"
    message["eventOrigin"] = "SPS"
    message["createDate"] = "2021-11-09T20:38:34.842556"
    message["updateDate"] = "2021-11-09T20:38:34.8426782"
    message["tags"] = {"externalOffer":"GLOBOPLAY_BAS_BDL_M", "portability": False}
    queue_dest.send_message(MessageBody=json.dumps(message))














