import base64
import json

print('Loading function')


def lambda_handler(event, context):
    output = []

    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data']).decode('utf-8')
        payload1 = json.loads(payload)
        day  = payload1["time"].split("/")[0]
        month  = payload1["time"].split("/")[1]
        year  = payload1["time"].split("/")[2].split(":")[0]
        hour  = payload1["time"].split("/")[2].split(":")[1]
        minute  = payload1["time"].split("/")[2].split(":")[2]
        second  = payload1["time"].split("/")[2].split(":")[3].split()[0]
        
        partition_keys  = {
            "day":    day,
            "month":   month,
            "year":    year,
            "hour":    hour,
            "minute":   minute,
            "second":  second
        }

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload.encode('utf-8')).decode('utf-8'),
            'metadata': { 'partitionKeys': partition_keys }
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
