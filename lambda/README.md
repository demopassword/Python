event json
```json
{
  "invocationId": "invocationIdExample",
  "deliveryStreamArn": "arn:aws:kinesis:EXAMPLE",
  "region": "us-east-1",
  "records": [
    {
      "recordId": "49546986683135544286507457936321625675700192471156785154",
      "approximateArrivalTimestamp": 1495072949453,
      "data": "eyJ0aW1lc3RhbXAiOiIyMDIzLTEwLTA1IDA3OjI4OjQzIiwicmVtb3RlX2FkZHIiOiIxMjcuMC4wLjEiLCJtZXRob2QiOiJHRVQiLCJwYXRoIjoiL3YxL2NvbG9yL21lbG9uIiwicHJvdG9jb2wiOiJIVFRQLzEuMSIsInN0YXR1c19jb2RlIjoiMjAwIn0="
    }
  ]
}
```

firehose_partitioning.py response
```
Test Event Name
my_event

Response
{
  "records": [
    {
      "recordId": "49546986683135544286507457936321625675700192471156785154",
      "result": "Ok",
      "data": "eyJ0aW1lc3RhbXAiOiAxNjk2NDkwOTIzLjAsICJyZW1vdGVfYWRkciI6ICIxMjcuMC4wLjEiLCAibWV0aG9kIjogIkdFVCIsICJwYXRoIjogIi92MS9jb2xvci9tZWxvbiIsICJwcm90b2NvbCI6ICJIVFRQLzEuMSIsICJzdGF0dXNfY29kZSI6ICIyMDAifQ==",
      "metadata": {
        "partitionKeys": {
          "year": "2023",
          "month": "10",
          "date": "05",
          "hour": "07",
          "minute": "28"
        }
      }
    }
  ]
}

Function Logs
START RequestId: bea69d02-828a-4c7c-8b57-ad784a2eb373 Version: $LATEST
49546986683135544286507457936321625675700192471156785154
Successfully processed 1 records.
END RequestId: bea69d02-828a-4c7c-8b57-ad784a2eb373
REPORT RequestId: bea69d02-828a-4c7c-8b57-ad784a2eb373	Duration: 2.37 ms	Billed Duration: 3 ms	Memory Size: 128 MB	Max Memory Used: 37 MB

Request ID
bea69d02-828a-4c7c-8b57-ad784a2eb373
```
