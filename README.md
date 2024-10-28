# Generate Tiktok msToken

[This is a Tool to Generate valid "msToken" to use in Tiktok Endpoints.]
-
Upon researching the "msToken" value I found out that:

- When using `GET /web/report?msToken={value}`

The length of the returned "msToken" seems to change based on the value provided:

- `108 Characters`: This happens when the request's "msToken" is empty. The response always gives back a 108-character token.
- `116 Characters`: If you use a random, non-TikTok "msToken," like "hgrioahgriog" it generates a 116-character token.
- `124 Characters`: When you visit TikTok.com/@tiktok for the first time with no cookie, you get a 124-character token.
- `148 Characters`: Using the previous 124-character token with the `POST /web/report/?msToken={124_Length_Token}` endpoint results in a 148-character token. (Works In all of the endpoints I tested.)
> The '148' Character "msToken" seems to be the one working in multiple endpoints. Its the only one that did not return an Empty response.

- The script is working as of October 28, 2024, but it still requires improvements in how "strData" value is updated.
--------------------------------------------------
The '148' Character "msToken" Worked in `/api/post/item_list/` and `/api/uniqueid/check/` Endpoint without any issues. 

- Other msTokens (that are not '148' in length) Worked in _some_ endpoints.
--------------------------------------------------
# How-to Use 
Run the Script.
```
>> python main.py
```
Example response: 
```
Making initial GET request...
Initial Token length: '124'

Making POST request...
Final X-Ms-Token: 'ereeNjzNI2CB4KaNgehdo6iIab4e423wqNZkdYt9B57lhspRmsRQr_h-HCIyA9VQuR8ecLHdYjneonZ_w-wWTE_h-F_PNEbcDK76_3Rbb8DJ6x6_QxaEDcD8O_t0uOuEy5cUvRwLZQudAxVrrQ1s'
Token length: '148'
```
You can then use the "Final X-Ms-Token" value normally.

--------------------------------------------------
Contact Telegram: @teeemvn
