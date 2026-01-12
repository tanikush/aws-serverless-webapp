import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactFormData')

def lambda_handler(event, context):
    """
    AWS Lambda function to handle contact form submissions.
    
    Args:
        event: API Gateway event containing form data
        context: Lambda context object
        
    Returns:
        Response object with status code and body
    """
    try:
        # Parse request body
        body = json.loads(event['body'])
        
        # Create item for DynamoDB
        item = {
            'id': str(uuid.uuid4()),
            'name': body['name'],
            'email': body['email'],
            'message': body['message'],
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Store in DynamoDB
        table.put_item(Item=item)
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Data saved successfully',
                'id': item['id']
            })
        }
        
    except Exception as e:
        # Return error response
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Error',
                'error': str(e)
            })
        }
