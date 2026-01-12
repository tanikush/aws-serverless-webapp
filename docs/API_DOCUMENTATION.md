# API Documentation

## Contact Form API

### Base URL
```
https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod
```

---

## Endpoints

### Submit Contact Form

**Endpoint:** `/contact`  
**Method:** `POST`  
**Content-Type:** `application/json`

#### Request Body

```json
{
  "name": "string (required)",
  "email": "string (required)",
  "message": "string (required)",
  "timestamp": "string (ISO 8601 format)"
}
```

#### Example Request

```bash
curl -X POST https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello, this is a test message!",
    "timestamp": "2025-01-12T10:30:00Z"
  }'
```

#### Success Response

**Status Code:** `200 OK`

```json
{
  "message": "Data saved successfully",
  "id": "550e8400-e29b-41d4-a716-446655440000"
}
```

#### Error Response

**Status Code:** `500 Internal Server Error`

```json
{
  "message": "Error",
  "error": "Error description here"
}
```

---

## CORS Configuration

The API supports Cross-Origin Resource Sharing (CORS) with the following headers:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

---

## Rate Limits

- **Free Tier:** 1,000,000 requests per month
- **Throttling:** 10,000 requests per second (default API Gateway limit)

---

## Error Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success - Data saved successfully |
| 400 | Bad Request - Invalid input data |
| 500 | Internal Server Error - Server-side error |
| 502 | Bad Gateway - Lambda function error |
| 504 | Gateway Timeout - Request timeout |

---

## Data Storage

All form submissions are stored in DynamoDB with the following schema:

```json
{
  "id": "UUID (Primary Key)",
  "name": "string",
  "email": "string",
  "message": "string",
  "timestamp": "ISO 8601 datetime string"
}
```

---

## Security

- All API requests must use HTTPS
- CORS is configured to allow requests from any origin
- Lambda function has minimal IAM permissions (DynamoDB write only)
- No authentication required (public API)

---

## Testing

### Using cURL

```bash
curl -X POST https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod/contact \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","message":"Test message","timestamp":"2025-01-12T10:30:00Z"}'
```

### Using Postman

1. Set method to `POST`
2. Enter URL: `https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod/contact`
3. Set header: `Content-Type: application/json`
4. Add JSON body with required fields
5. Send request

---

## Monitoring

View API logs in CloudWatch:
- Log Group: `/aws/lambda/ContactFormHandler`
- Metrics: Invocations, Errors, Duration, Throttles

---

**Last Updated:** January 2025
