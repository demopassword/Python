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
        date_string  = str(payload1['time'])
        date_object = datetime.strptime(date_string,'%d/%b/%Y:%H:%M:%S %z')
        timestamp = time.mktime(date_object.timetuple())
        
        # lambda now time
        now_time = datetime.now()

        day  = payload1["time"].split("/")[0]
        month  = payload1["time"].split("/")[1]
        year  = payload1["time"].split("/")[2].split(":")[0]
        hour  = payload1["time"].split("/")[2].split(":")[1]
        minute  = payload1["time"].split("/")[2].split(":")[2]
        second  = payload1["time"].split("/")[2].split(":")[3].split()[0]
        
        payload1["time"] =  timestamp
        payload1["now_time"] = str(now_time)
        
        partition_keys  = {
            "day":    day,
            "month":   month,
            "year":    year,
            "hour":    hour,
            "minute":   minute,
            "second":  second
        }
        
        payload = json.dumps(payload1)

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload.encode('utf-8')).decode('utf-8'),
            'metadata': { 'partitionKeys': partition_keys }
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
