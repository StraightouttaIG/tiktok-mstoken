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
