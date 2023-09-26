### boto3 send.py ( Lambda to Firehose )
```python
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
```
## Parquet Conversion
### send record
```json
{"datetime": "2023-09-23 10:35:39.103628"}
```
### python Field
```
        json_data = {
                    "datetime": [payload1['datetime']]
                }
```

### example
```json
{"msg": "hello", "age": "19"}
```

### python Field
```
        json_data = {
                    "msg": [payload1['msg']],
                    "age": [payload1['age']]
                }
```