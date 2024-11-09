# Important Note
- This Project Is a temporary workaround. Until I am able to Use undetected Firefox & stealth similarly to undetected chrome, when that happens It would be easy to generate `strData` and use the original `POST /web/report/` Method Which is much more Stable

So this implementation may not be the best method yet.

# Generate Tiktok msToken

[This is a Tool to Generate valid "msToken" to use in Tiktok Endpoints.]
-
Upon researching the "msToken" value I found out that:

The length of the returned "msToken" seems to change based on the value provided:

- `108 Characters`: This happens when the request's "msToken" is empty. The response always gives back a 108-character token.
- `116 Characters`: If you use a random, non-TikTok "msToken," like "hgrioahgriog" it generates a 116-character token.
- `124 Characters`: When you visit TikTok.com/@tiktok for the first time with no cookie, you get a 124-character token.
- `[144, 152] Characters`: Using the previous 124-character token with the `POST /web/report/?msToken={124_Length_Token}` endpoint results in a [144, 148, 152] Length token. Length depends on browser used and other settings.
- `148 Characters`: I was only able to generate this one by using a private Firefox window Then waiting until the msToken value updates. It's not possible on any other browser that I tried. Example: '5b2TD_RaPNOL4lQJ5eVWm6yAd0akV7k3cf8QuxevVeWdO110UU8iMwavrkP6lm4DUP4XQoj2-g1WE8L0pMy3o6fY8NRZDRZt0rw43dtX1xeqP5bOJbtlqKKW_niS1Eqg1gj9wuwDezalzgKJmwqL' It is also the only token type that works on 100% of the endpoints I tried. till now I can only generate this manually, Working on a way to automate it.

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

# TODO
- Generate msToken using `/web/report/` Endpoint
- Generate Working `strData`

--------------------------------------------------

Contact Telegram: @teeemvn
