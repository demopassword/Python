import base64
import time
import json
from datetime import datetime
print('Loading function')


def lambda_handler(event, context):
    output = []

    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data']).decode('utf-8')
        payload1 = json.loads(payload)
        date_string  = str(payload1['timestamp'])
        date_object = datetime.strptime(date_string,'%Y-%m-%d %H:%M:%S')
        timestamp = time.mktime(date_object.timetuple())
        payload1["timestamp"] = timestamp
        payload = json.dumps(payload1)
        
        partition_keys = {"year": date_object.strftime('%Y'),
                            "month": date_object.strftime('%m'),
                            "date": date_object.strftime('%d'),
                            "hour": date_object.strftime('%H'),
                            "minute": date_object.strftime('%M')
                          }
        # Do custom processing on the payload here

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload.encode('utf-8')).decode('utf-8'),
            'metadata': { 'partitionKeys': partition_keys }
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
