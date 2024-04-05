<script>
document.addEventListener('DOMContentLoaded', function() {
    var base_url = '<input_your_server_base_url_here>'; // Base URL defined here

    document.getElementById('sign-up-button').addEventListener('click', function(e) {
        e.preventDefault(); // Prevent the default form submission

        var errorContainer = document.getElementById('sign-up-error-container');
        var errorText = document.getElementById('sign-up-error-text');
        errorContainer.style.display = 'none'; // Unhide the error container
        errorText.textContent = ''; // Change the text

        // Collect email and password from the form
        var first_name = document.getElementById('sign-up-first-name').value;
        var last_name = document.getElementById('sign-up-last-name').value;
        var date_of_birth = document.getElementById('sign-up-dob').value;
        var height = document.getElementById('sign-up-height').value;
        var weight = document.getElementById('sign-up-weight').value;
        var gender = document.getElementById('sign-up-gender').value;
        var email = document.getElementById('sign-up-email').value;
        var password = document.getElementById('sign-up-password').value;

        // Prepare the API request
        var data = {
            first_name: first_name, 
            last_name: last_name, 
            date_of_birth: date_of_birth,
            height_cm: height,
            weight_kg: weight,
            gender: gender,
            email: email,
            password: password
        };

        fetch(base_url + '/api/users/register', { // Use base_url variable
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'true',
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (response.status === 201) {
                // Registration successful, redirect to the dashboard
                window.location.href = '/log-in'; // Replace with your actual dashboard page URL
            } else if (response.status === 409) {
                // User already exists, show error message
                var errorContainer = document.getElementById('sign-up-error-container');
                var errorText = document.getElementById('sign-up-error-text');
                errorContainer.style.display = 'flex'; // Unhide the error container
                errorText.textContent = 'Email already exists.'; // Change the text
            } else if (response.status === 400) {
                // Validation Error
                var errorContainer = document.getElementById('sign-up-error-container');
                var errorText = document.getElementById('sign-up-error-text');
                errorContainer.style.display = 'flex'; // Unhide the error container
                errorText.textContent = 'Invalid data provided to create account.'; // Change the text
            } else if (response.status === 500) {
                // Validation Error
                var errorContainer = document.getElementById('sign-up-error-container');
                var errorText = document.getElementById('sign-up-error-text');
                errorContainer.style.display = 'flex'; // Unhide the error container
                errorText.textContent = 'Internal Server Error, please contact support.'; // Change the text
            } else {
                // Handle other errors or invalid registration attempts
                alert('Registration failed. Please try again.');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
</script>