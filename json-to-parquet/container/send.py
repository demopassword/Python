import json
import boto3
import datetime

client = boto3.client('firehose')

def lambda_handler(event, context):
    now_time = datetime.datetime.now()
    json_data = {
        "datetime": str(now_time)
    }
    jsondate_result = json.dumps(json_data)
    response = client.put_record(
        DeliveryStreamName='kinesis-firehose-stream',
        Record={
            'Data': jsondate_result
        }
    )
    print(jsondate_result)
    return response