<script>
document.addEventListener('DOMContentLoaded', function() {
    var base_url = '<input_your_server_base_url_here>'; // Base URL defined here
    
    document.getElementById('login-button').addEventListener('click', function(e) {
        e.preventDefault(); // Prevent the default form submission

        // Collect email and password from the form
        var email = document.getElementById('login-email').value;
        var password = document.getElementById('login-password').value;

        // Prepare the API request
        var data = {
            email: email,
            password: password
        };

        fetch(base_url + '/user/authorize', { // Replace with your actual API endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'true',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
            // Adjusted to match the response structure provided by your server
            if (data.status === 'success' && data.data && data.data.user_token) {
                localStorage.setItem('user_token', data.data.user_token); // Store the token
                window.location.href = '/dashboard'; // Redirect
            } else {
                // Handle different errors based on the status code or error message
                // It's good practice to provide more specific feedback when possible
                alert('Login failed. Please check your credentials and try again.');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
</script>
