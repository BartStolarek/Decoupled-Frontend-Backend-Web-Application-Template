from flask import Flask, request, make_response

def handle_preflight(app: Flask):
    @app.before_request
    def preflight_handler():
        # Only run this if it's an OPTIONS request (preflight request)
        if request.method == "OPTIONS":
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,ngrok-skip-browser-warning")
            response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            response.headers.add("Access-Control-Max-Age", "3600")  # Adjust max age as needed
            return response
