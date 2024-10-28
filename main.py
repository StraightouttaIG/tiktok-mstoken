import requests

def get_mstoken():
    base_url = "https://mssdk-va.tiktok.com"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': "https://www.tiktok.com",
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Referer': "https://www.tiktok.com"
    }

    try:
        # First make a GET request to obtain initial 'msToken'
        session = requests.Session()  
        initial_url = f"{base_url}/web/report?msToken=2LMEoIiNbaxIJGuXzU-vEXj4B8_DTfHnVLHrN2CPpWkQFD15vpH8N0F2K0h7_7FvFBINHNdr-iEIIID9tG8S0pqmC_AEGa5zrFHv8WvkvKUKUM_FIxNidvusIIk="
                                             # Leave this unchanged. ^
        print("Making initial GET request...")
        
        get_response = session.get(initial_url, headers=headers)
        
        initial_token = get_response.headers.get('X-Ms-Token')
        if not initial_token:
            print("No X-Ms-Token found in GET response headers")
            return
        
        print(f"Initial Token length: '{len(initial_token)}'")
      
        post_url = f"{base_url}/web/report?msToken={initial_token}"

        post_data = {
            "magic": 538969122,
            "version": 1,
            "dataType": 8,
            "strData": "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",
            "tspFromClient": 0
        }

        print("\nMaking POST request...")
        post_response = session.post(post_url, json=post_data, headers=headers)
        
        final_token = post_response.headers.get('X-Ms-Token')
        if final_token:
            print(f"Final X-Ms-Token: '{final_token}'")    
            print(f"Token length: '{len(final_token)}'")     
            # final_token length must be '148'
            # if its not '148' then something must've gone wrong           
        else:
            print("No X-Ms-Token found in POST response headers")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_mstoken()