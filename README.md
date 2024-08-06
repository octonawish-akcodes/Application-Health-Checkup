# Application-Health-Checkup

**Purpose:**
This Python script is designed to monitor the uptime and health of a web application. It periodically checks the application's HTTP status code and reports whether it's 'up' (functioning correctly) or 'down' (unavailable or not responding).

**How it works:**
1. Imports necessary libraries: `requests` for making HTTP requests and `time` for introducing delays between checks.
2. Defines a function `check_application_health`:
   - Takes the application URL as input.
   - Attempts to make a GET request to the URL with a timeout.
   - Returns 'up' if the request is successful and the status code is 200.
   - Returns 'down' if the request fails or the status code is not 200.
3. Defines the `main` function:
   - Sets the application URL.
   - Continuously checks the application health using `check_application_health`.
   - Prints the status to the console.
   - Sleeps for a specified interval before the next check.

**Usage:**
1. Replace `"http://google.com"` with the actual URL of your application.
2. Adjust the `time.sleep(60)` value to change the check interval as needed.
3. Run the script `python3 app.py`.


**Example Output:**
```
Application status: up
Application status: down
Application status: up
```
