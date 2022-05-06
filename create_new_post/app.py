import uuid
from datetime import datetime, timezone

import boto3


class PostModel:
    def __init__(self, post_id, author_name, created_date, post_html, updated_date):
        self.PostId = post_id
        self.AuthorName = author_name
        self.CreatedDate = created_date
        self.PostHtml = post_html
        self.UpdatedDate = updated_date


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
