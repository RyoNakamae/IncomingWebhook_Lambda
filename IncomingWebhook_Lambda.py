# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Lambda用
# ---------------------------------------------------------------------------


import json

def lambda_handler(event, context):
    # 引数：eventの内容を表示
    print("Received event: " + json.dumps(event))
    # rawQueryString
    rawQueryString = event['rawQueryString']
    if(len(rawQueryString) != 0):
        queryStringParameters = event['queryStringParameters']
        print(queryStringParameters)

    # body
    body = event.get('body')
    if(not body is None):
        json_body = json.dumps(body)
        print(json_body)

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': json.dumps('Hello from Lambda!')
    }