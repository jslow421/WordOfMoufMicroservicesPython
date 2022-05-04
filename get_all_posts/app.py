from __future__ import print_function
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Posts')

    item = table.get_item(Key={
        'PostId': 'b967aa67-4842-48b8-a0f0-ea3fdecae6cb'
    })

    print(item)
    return item
