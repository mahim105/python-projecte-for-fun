import requests

def track_phone_number(phone_number):
    api_key = 'YOUR_API_KEY'  # Replace with your API key
    url = f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Check if the API response has the expected keys
        if 'valid' in data:
            if data['valid']:
                print(f"Number: {data['number']}")
                print(f"Country: {data['country_name']}")
                print(f"Location: {data['location']}")
                print(f"Carrier: {data['carrier']}")
            else:
                print("Invalid phone number.")
        else:
            print("Error in API response:", data)  # Print the full response for debugging
    except requests.exceptions.RequestException as e:
        print("API request error:", e)

# Get user input for phone number
user_phone_number = input("Please enter the phone number you want to track: ")

# Call the function with the user's input
track_phone_number(user_phone_number)
