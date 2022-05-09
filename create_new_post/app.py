import uuid
from datetime import datetime, timezone

import boto3


def lambda_handler(event, context):
    table = boto3.resource('dynamodb').Table('Posts')

    post = table.put_item(
        Item={
            'PostId': str(uuid.uuid4()),
            'AuthorName': event['postAuthor'],
            'CreatedDate': str(datetime.now(timezone.utc)),
            'PostHtml': event['postText'],
            'UpdatedDate': str(datetime.now(timezone.utc))
        }
    )

    return {
        'statuscode': 200,
        'body': post
    }
