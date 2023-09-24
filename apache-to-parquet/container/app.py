import base64
import pandas as pd
import pyarrow
import subprocess
import re

def lambda_handler(event, context):
    output = []
    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data']).decode('utf-8')
        match = re.match(r'^(.*?) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"$', payload)
        ip, timestamp, request, status, size, _, user_agent = match.groups()
        data = {
            'ip': [ip],
            'timestamp': [timestamp],
            'request': [request],
            'status': [int(status)],
            'size': [int(size)],
            'user_agent': [user_agent]
        }
        df = pd.DataFrame(data)
        df.to_parquet("/tmp/log_data.parquet")
        result = subprocess.check_output(['cat', '/tmp/log_data.parquet'])
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(result).decode('utf-8')
        }
        output.append(output_record)
        print(output)
    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
