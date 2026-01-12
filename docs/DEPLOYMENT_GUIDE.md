# Deployment Guide

## Step-by-Step Deployment Instructions

---

## Prerequisites

- AWS Account (Free Tier)
- AWS CLI installed and configured
- Git installed
- Basic knowledge of AWS services

---

## Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/aws-serverless-webapp.git
cd aws-serverless-webapp
```

---

## Step 2: Create S3 Bucket

### Using AWS Console:

1. Go to S3 service
2. Click "Create bucket"
3. Bucket name: `serverless-webapp-yourname` (must be unique)
4. Region: `us-east-1`
5. Uncheck "Block all public access"
6. Click "Create bucket"

### Enable Static Website Hosting:

1. Open your bucket
2. Go to "Properties" tab
3. Scroll to "Static website hosting"
4. Click "Edit" → Enable
5. Index document: `index.html`
6. Save changes

### Add Bucket Policy:

1. Go to "Permissions" tab
2. Click "Bucket Policy" → Edit
3. Paste this policy (replace bucket name):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::serverless-webapp-yourname/*"
    }
  ]
}
```

### Upload Files:

1. Go to "Objects" tab
2. Click "Upload"
3. Upload files from `frontend/` folder
4. Click "Upload"

---

## Step 3: Create DynamoDB Table

### Using AWS Console:

1. Go to DynamoDB service
2. Click "Create table"
3. Table name: `ContactFormData`
4. Partition key: `id` (String)
5. Table settings: Default settings
6. Click "Create table"

---

## Step 4: Create Lambda Function

### Using AWS Console:

1. Go to Lambda service
2. Click "Create function"
3. Function name: `ContactFormHandler`
4. Runtime: Python 3.12
5. Click "Create function"

### Add Code:

1. Copy code from `lambda/lambda_function.py`
2. Paste in Lambda code editor
3. Click "Deploy"

### Add DynamoDB Permission:

1. Go to "Configuration" → "Permissions"
2. Click on the role name
3. Click "Add permissions" → "Attach policies"
4. Search: `AmazonDynamoDBFullAccess`
5. Select and attach

---

## Step 5: Create API Gateway

### Using AWS Console:

1. Go to API Gateway service
2. Click "Create API"
3. Choose "REST API" → Build
4. API name: `ContactFormAPI`
5. Endpoint type: Regional
6. Click "Create API"

### Create Resource:

1. Click "Actions" → "Create Resource"
2. Resource name: `contact`
3. Enable CORS: ✓
4. Click "Create Resource"

### Create POST Method:

1. Select `/contact` resource
2. Click "Actions" → "Create Method" → POST
3. Integration type: Lambda Function
4. Lambda Proxy integration: ✓
5. Lambda Function: `ContactFormHandler`
6. Click "Save" → OK

### Enable CORS:

1. Select `/contact` resource
2. Click "Actions" → "Enable CORS"
3. Click "Enable CORS and replace existing CORS headers"
4. Confirm

### Deploy API:

1. Click "Actions" → "Deploy API"
2. Deployment stage: [New Stage]
3. Stage name: `prod`
4. Click "Deploy"

### Get API URL:

1. Go to "Stages" → "prod" → "POST" → "/contact"
2. Copy the "Invoke URL"

---

## Step 6: Update Frontend

1. Open `frontend/script.js`
2. Replace `YOUR_API_URL` with your actual API Gateway URL
3. Save the file
4. Re-upload `script.js` to S3 bucket

---

## Step 7: Test Application

1. Get S3 website URL from bucket properties
2. Open URL in browser
3. Fill the contact form
4. Submit
5. Check DynamoDB for data

---

## Step 8: Monitor with CloudWatch

1. Go to CloudWatch service
2. Click "Logs" → "Log groups"
3. Open `/aws/lambda/ContactFormHandler`
4. View execution logs

---

## Cleanup (To Avoid Charges)

### Delete in this order:

1. **API Gateway:** Delete `ContactFormAPI`
2. **Lambda:** Delete `ContactFormHandler` function
3. **DynamoDB:** Delete `ContactFormData` table
4. **S3:** Empty bucket → Delete bucket
5. **CloudWatch:** Delete log groups (optional)
6. **IAM:** Delete Lambda execution role (optional)

---

## Troubleshooting

### Issue: CORS Error
**Solution:** Enable CORS in API Gateway and redeploy

### Issue: 403 Forbidden on S3
**Solution:** Check bucket policy and public access settings

### Issue: Lambda timeout
**Solution:** Increase timeout in Lambda configuration

### Issue: DynamoDB access denied
**Solution:** Check IAM role has DynamoDB permissions

---

## Cost Estimation

All services used are within AWS Free Tier:
- S3: 5 GB storage (using ~1 MB)
- Lambda: 1M requests/month (using ~100)
- API Gateway: 1M requests/month (using ~100)
- DynamoDB: 25 GB storage (using ~10 KB)

**Estimated Cost: $0.00/month**

---

**Deployment Complete! 🎉**
