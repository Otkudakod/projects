import requests
import json

# Add headers
headers = {
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://cityexpert.rs/ru/properties-for-rent/belgrade?currentPage=1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

# Create a list for JSON responses
all_responses = []

for i in range(1, 30):
    params = {
        'req': '{"cityId":1,"rentOrSale":"r","currentPage":'+str(i)+',"searchSource":"regular","sort":"datedsc"}'
    }
    response = requests.get('https://cityexpert.rs/api/Search', params=params, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        json_data = response.json()
        all_responses.append(json_data)
    else:
        print(f'Request for page {i} failed with status code {response.status_code}')

# Write all the responses to a single JSON file
with open('all_responses.json', 'w') as json_file:
    json.dump(all_responses, json_file, indent=4)

print('Saved all_responses.json')

