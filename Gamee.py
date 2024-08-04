import requests
import json
import os

# Define the initial URL and headers
initial_url = "https://api.gamee.com"
initial_headers = {
    "client-language": "en",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
    "sec-ch-ua-mobile": "?1",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOiIxNzIyNzU0NTI1IiwidXNlcklkIjo3OTI5NjkzNCwiaW5zdGFsbFV1aWQiOiIxNDcxYTg2OS0zMTJhLTRhZmItYmYwYy0wMWY4NzUyMTkxMGEiLCJ0eXBlIjoiYXV0aGVudGljYXRpb25Ub2tlbiIsImF1dGhvcml6YXRpb25MZXZlbCI6ImJvdCIsInBsYXRmb3JtIjoiYm90LXRlbGVncmFtIn0.3o7_xCgK8ia8H0mQSL8SXVieyc3yRWYTSDxwFwR8XFU",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; en; TECNO KJ5 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.129 HiBrowser/v2.22.3.2 UWS/ Mobile Safari/537.36",
    "content-type": "text/plain;charset=UTF-8",
    "x-install-uuid": "1471a869-312a-4afb-bf0c-01f87521910a",
    "sec-ch-ua-platform": "Android",
    "accept": "*/*",
    "origin": "https://prizes.gamee.com",
    "x-requested-with": "com.talpa.hibrowser",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://prizes.gamee.com/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=1, i"
}

# Check if Tokens.txt exists and update authorization header with refresh token
if os.path.exists("Tokens.txt"):
    with open("Tokens.txt", "r") as file:
        existing_tokens = json.load(file)
        refresh_token = existing_tokens.get("refresh")
        if refresh_token:
            initial_headers["authorization"] = f"Bearer {refresh_token}"

# Define the initial data payload
initial_data = '[{"jsonrpc":"2.0","id":"app.telegram.get","method":"app.telegram.get","params":{}},{"jsonrpc":"2.0","id":"user.authentication.loginUsingTelegram","method":"user.authentication.loginUsingTelegram","params":{"initData":"user=%7B%22id%22%3A6281741488%2C%22first_name%22%3A%22Muhammad%22%2C%22last_name%22%3A%22Saim%22%2C%22username%22%3A%22hook481%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=-4250461626037554240&chat_type=sender&auth_date=1721934097&hash=6c75594a96d35bcd4d2b2ae45d077a0c4cefcd39b29872f77e3116bb9e1e142f"}}]'

# Send the initial POST request
initial_response = requests.post(initial_url, headers=initial_headers, data=initial_data)

# Check if the initial request was successful
if initial_response.status_code == 200:
    try:
        # Parse the initial response JSON
        initial_response_json = initial_response.json()

        # Extract the authenticate and refresh tokens
        tokens = initial_response_json[1].get('result', {}).get('tokens', {})
        authenticate_token = tokens.get('authenticate')
        refresh_token = tokens.get('refresh')

        if authenticate_token and refresh_token:
            # Check if Tokens.txt exists
            if os.path.exists("Tokens.txt"):
                # Load the existing tokens
                with open("Tokens.txt", "r") as file:
                    existing_tokens = json.load(file)
                
                # Update the tokens
                existing_tokens["authenticate"] = authenticate_token
                existing_tokens["refresh"] = refresh_token
            else:
                # Create a new dictionary for the tokens
                existing_tokens = {
                    "authenticate": authenticate_token,
                    "refresh": refresh_token
                }

            # Save the updated tokens to Tokens.txt
            with open("Tokens.txt", "w") as file:
                json.dump(existing_tokens, file, indent=4)

            print("Tokens have been saved to Tokens.txt")

            # Define the new URL and headers for the subsequent request
            new_url = "https://api.gamee.com"
            new_headers = {
                "client-language": "en",
                "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
                "sec-ch-ua-mobile": "?1",
                "authorization": f"Bearer {authenticate_token}",
                "user-agent": "Mozilla/5.0 (Linux; Android 13; en; TECNO KJ5 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.129 HiBrowser/v2.22.3.2 UWS/ Mobile Safari/537.36",
                "content-type": "text/plain;charset=UTF-8",
                "x-install-uuid": "1471a869-312a-4afb-bf0c-01f87521910a",
                "sec-ch-ua-platform": "Android",
                "accept": "*/*",
                "origin": "https://prizes.gamee.com",
                "x-requested-with": "com.talpa.hibrowser",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://prizes.gamee.com/",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            }

            # Define the new data payload
            new_data = '{"jsonrpc":"2.0","id":"game.saveTelegramMainGameplay","method":"game.saveTelegramMainGameplay","params":{"gameplayData":{"gameId":294,"score":0,"playTime":62,"releaseNumber":4,"createdTime":"2024-07-27T07:59:52+05:00","metadata":{"gameplayId":2},"checksum":"8d50ce3061b5ac7d6c846ee3091813d0","gameStateData":"{\\"usedLives\\":60,\\"reward\\":{\\"WP\\":60,\\"COIN\\":36}}","replayData":"AgAAABIAPHIgUXEAPAAkAQA8","replayVariant":null,"replayDataChecksum":null}}}'

            # Send the new POST request with the updated authenticate token
            new_response = requests.post(new_url, headers=new_headers, data=new_data)

            # Check if the new request was successful
            if new_response.status_code == 200:
                print("New request was successful")
                print(new_response.json())
            else:
                print(f"Failed to send new POST request. Status code: {new_response.status_code}")
                print(f"Response: {new_response.text}")

        else:
            print("Tokens not found in the response")
    except (IndexError, KeyError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")
else:
    print(f"Failed to send initial POST request. Status code: {initial_response.status_code}")
    print(f"Response: {initial_response.text}")
