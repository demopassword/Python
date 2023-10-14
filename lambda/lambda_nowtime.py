import base64
import json
from datetime import datetime
import time

print('Loading function')


def lambda_handler(event, context):
    output = []

    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data']).decode('utf-8')
        payload1 = json.loads(payload)
        now_time = datetime.now()
        date_string  = str(now_time)
        date_object = datetime.strptime(date_string,'%Y-%m-%d %H:%M:%S.%f')
        timestamp = time.mktime(date_object.timetuple())
        
        
        payload1["now_time"] = str(timestamp)
        
        
        payload = json.dumps(payload1)

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload.encode('utf-8')).decode('utf-8')
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
