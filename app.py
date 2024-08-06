import requests
import time

def check_application_health(url):
  """Checks the health of an application based on its HTTP status code.

  Args:
    url: The URL of the application to check.

  Returns:
    A string indicating the application's status: 'up' or 'down'.
  """

  try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
      return 'up'
    else:
      return 'down'
  except requests.exceptions.RequestException as e:
    print(f"Error checking application health: {e}")
    return 'down'

def main():
  """Continuously checks the application health and prints the status."""

  url = "http://google.com"  # Replace with the actual URL

  while True:
    status = check_application_health(url)
    print(f"Application status: {status}")
    time.sleep(60)  # Check every minute

if __name__ == "__main__":
  main()
