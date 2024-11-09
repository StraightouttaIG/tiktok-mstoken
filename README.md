# Generate Tiktok msToken

[This is a Tool to Generate valid "msToken" to use in Tiktok Endpoints.]
-
Upon researching the "msToken" value I found out that:

The length of the returned "msToken" seems to change based on the value provided:

- `108 Characters`: This happens when the request's "msToken" is empty. The response always gives back a 108-character token.
- `116 Characters`: If you use a random, non-TikTok "msToken," like "hgrioahgriog" it generates a 116-character token.
- `124 Characters`: When you visit TikTok.com/@tiktok for the first time with no cookie, you get a 124-character token.
- `[144, 148, 152] Characters`: Using the previous 124-character token with the `POST /web/report/?msToken={124_Length_Token}` endpoint results in a [144, 148, 152] Length token. Length depends on browser used and other settings.

- The `[144, 148, 152]` Character "msToken" Worked in `/api/post/item_list/` and `/api/uniqueid/check/` Endpoint without any issues. 

When Using Stealth Selenium you are able to Generate valid msToken easily using this script.
Not using stealth selenium will result in an invalid msToken!

--------------------------------------------------
# How-to Use 
Install requirements.
```
>> pip install selenium
>> pip install selenium-stealth
```
Run the Script.
```
>> python main.py
```
Example output: 
```
Starting Chrome headless browser...
Waiting for msToken...
[144] Valid msToken found in 2.52 seconds: Y7czM6id2Wg8xCaghVWrhnW6EGWJ90w34sqPEA9oLt0L8KNeS4jdiz7aXtDsPjlv4D8R1elcWdsyLKu80kn0s3TAfyc9xuHHeNZ9Xtlu7-fvd9LqlAYnLeYD7ytEPKgLh6kn_so0otHdRg==
```
You can then use the msToken value normally.

--------------------------------------------------
Contact Telegram: @teeemvn
