import base64
import pandas as pd
import subprocess
import pyarrow
import json
def lambda_handler(event, context):
    output = []
    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data']).decode('utf-8')
        payload1 = json.loads(payload)
        json_data = {
                    "datetime": [payload1['datetime']]
                }
        df = pd.DataFrame(json_data)
        df.to_parquet("/tmp/datetime.parquet")
        result = subprocess.check_output(['cat', '/tmp/datetime.parquet'])
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(result).decode('utf-8')
        }
        output.append(output_record)
        print(output)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}