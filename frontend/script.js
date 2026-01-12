const API_URL = 'https://c866sxm4mf.execute-api.us-east-1.amazonaws.com/prod/contact';

document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    const responseDiv = document.getElementById('response');
    
    // Show loading state
    responseDiv.className = 'response';
    responseDiv.style.display = 'block';
    responseDiv.textContent = 'Submitting...';
    
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                email: email,
                message: message,
                timestamp: new Date().toISOString()
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            responseDiv.className = 'response success';
            responseDiv.textContent = ' Message submitted successfully! Stored in DynamoDB.';
            document.getElementById('contactForm').reset();
        } else {
            throw new Error(data.message || 'Submission failed');
        }
    } catch (error) {
        responseDiv.className = 'response error';
        responseDiv.textContent = ' Error: ' + error.message;
    }
});
