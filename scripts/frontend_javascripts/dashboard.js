<script>
document.addEventListener('DOMContentLoaded', function() {
    var base_url = ''; // Your base URL
    var token = localStorage.getItem('user_token'); // Retrieve the JWT token from localStorage

    if (!token) {
        console.error('No token found. Redirecting to login.');
        window.location.href = '/login'; // Redirect to login if token is not available
        return;
    }

    fetch(base_url + '/user/user-details', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'ngrok-skip-browser-warning': 'true',
            'Authorization': 'Bearer ' + token, // Pass the token for authentication
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok. Status: ' + response.status);
        }
        return response.json(); // Parse JSON only if response is ok
    })
    .then(data => {
        var userDetails = data.data.user_details;
        var welcomeText = 'Welcome, ' + userDetails.first_name + ' ' + userDetails.last_name;
        document.getElementById('dashboard-welcome-header').innerText = welcomeText;
        
    })
    .catch(error => {
        console.error('Error occurred:', error);
        console.log('Error name:', error.name);
        console.log('Error message:', error.message);
        console.log('Error stack:', error.stack);
        alert('Failed to load user details. Redirecting to login.');
        window.location.href = '/log-in'; // Redirect to login on error
    });    
});

</script>
