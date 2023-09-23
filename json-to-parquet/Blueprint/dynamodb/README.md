References
- https://dev.classmethod.jp/articles/introduce-dynamodb-streams/

이벤트 별 스트림 레코드 정보

#### INSERT (NewImage)
```json
{
    "eventID": "9b75fc7d627937c965aa7143f7158650", 
    "eventName": "INSERT", 
    "eventVersion": "1.1", 
    "eventSource": "aws:dynamodb", 
    "awsRegion": "[region]", 
    "dynamodb": {
        "ApproximateCreationDateTime": 1628577171.0, 
        "Keys": {
            "UserId": {
                "S": "dynamo"
            }
        }, 
        "NewImage": {
            "msg": {
                "S": "Insert Item"
            }, 
            "UserId": {
                "S": "dynamo"
            }
        }, 
        "SequenceNumber": "23241900000000016191110770", 
        "SizeBytes": 38, 
        "StreamViewType": "NEW_AND_OLD_IMAGES"
    }, 
    "eventSourceARN": "arn:aws:dynamodb:[region]:[AWS Account ID]:table/dynamodb-streams-handson/stream/2021-08-06T11:11:34.568"
}
```
#### MODIFY (NewImage, OldImage)
```json
{
    "eventID": "ac3336e4ac17005525be2c754ae75a6d", 
    "eventName": "MODIFY", 
    "eventVersion": "1.1", 
    "eventSource": "aws:dynamodb", 
    "awsRegion": "[region]", 
    "dynamodb": {
        "ApproximateCreationDateTime": 1628577180.0, 
        "Keys": {
            "UserId": {
                "S": "dynamo"
            }
        }, 
        "NewImage": {
            "msg": {
                "S": "Modify Item"
            }, 
            "UserId": {
                "S": "dynamo"
            }
        }, 
        "OldImage": {
            "msg": {
                "S": "Insert Item"
            }, 
            "UserId": {
                "S": "dynamo"
            }
        }, 
        "SequenceNumber": "23242000000000016191119891", 
        "SizeBytes": 64, 
        "StreamViewType": "NEW_AND_OLD_IMAGES"
    }, 
    "eventSourceARN": "arn:aws:dynamodb:[region]:[AWS Account ID]:table/dynamodb-streams-handson/stream/2021-08-06T11:11:34.568"
}
```
#### REMOVE (Old image)
```json
{
    "eventID": "0a96116c67d0ff912e8fb15b02d20220", 
    "eventName": "REMOVE", 
    "eventVersion": "1.1", 
    "eventSource": "aws:dynamodb", 
    "awsRegion": "[region]", 
    "dynamodb": {
        "ApproximateCreationDateTime": 1628577186.0, 
        "Keys": {
            "UserId": {
                "S": "dynamo"
            }
        }, 
        "OldImage": {
            "msg": {
                "S": "Modify Item"
            }, 
            "UserId": {
                "S": "dynamo"
            }
        }, 
        "SequenceNumber": "23242100000000016191125879", 
        "SizeBytes": 38, 
        "StreamViewType": "NEW_AND_OLD_IMAGES"
    }, 
    "eventSourceARN": "arn:aws:dynamodb:[region]:[AWS Account ID]:table/dynamodb-streams-handson/stream/2021-08-06T11:11:34.568"
}
```