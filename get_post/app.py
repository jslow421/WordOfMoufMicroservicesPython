from __future__ import print_function

# import json

import boto3


def lambda_handler(event, context):
    table = boto3.resource('dynamodb').Table('Posts')

    requested_id = event['id']

    post = table.get_item(Key={
        'PostId': requested_id
    })

    # found_post = json.loads(post)

    return post
