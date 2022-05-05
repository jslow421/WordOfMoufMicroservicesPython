from __future__ import print_function

import uuid
from datetime import datetime, timezone

import boto3

from Core.PostModel import PostModel


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Posts')
    print(event)
    post = table.put_item(
        Item=PostModel(
            uuid.uuid4(),
            event['postAuthor'],
            datetime.now(timezone.utc),
            event['postHtml'],
            datetime.now(timezone.utc)
        )
    )

    return {
        'statuscode': 200,
        'body': post
    }
