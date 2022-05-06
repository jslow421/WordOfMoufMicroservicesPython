import boto3


def lambda_handler(event, context):
    table = boto3.resource('dynamodb').Table('Posts')
    posts = table.scan()

    return posts
