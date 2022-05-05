from __future__ import print_function

import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Posts')
    print(event)
    print(context)
    # print(event.PostAuthor)
    requested_id = event['id']
    post = table.get_item(Key={
        'PostId': requested_id
    })

    return {
        'statuscode': 200,
        'body': post
    }
