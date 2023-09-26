import base64
import json

print('Loading function')


def lambda_handler(event, context):
    output = []

    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data']).decode('utf-8')
        payload1 = payload.lower()
        payload2 = json.loads(payload1)
        
        dynamodb_country = payload2['dynamodb']['newimage']['country']['s']
        dynamodb_name = payload2['dynamodb']['newimage']['name']['s']
        dynamodb_phone = payload2['dynamodb']['newimage']['phone']['s']
        
        try:
            dynamodb_from = payload2['dynamodb']['newimage']['from']['s']
            text = {
                        'country': dynamodb_country,
                        'name': dynamodb_name,
                        'phone': dynamodb_phone,
                        'from': dynamodb_from
                    }
            result_text = json.dumps(text) + "\n"
            print(result_text)
        except:
            text = {
                        'country': dynamodb_country,
                        'name': dynamodb_name,
                        'phone': dynamodb_phone,
                        'from': "ec2"
                    }
            result_text = json.dumps(text) + "\n"
            print(result_text)

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
