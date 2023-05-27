from bot_studio import *
twitter=bot_studio.twitter()
true=True;false=False
list_of_cookies=[
    {
        "domain": ".twitter.com",
        "expirationDate": 1715236356.257275,
        "hostOnly": false,
        "httpOnly": false,
        "name": "guest_id",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "v1%3A168102195151679771"
    },
    {
        "domain": "twitter.com",
        "expirationDate": 1696574271,
        "hostOnly": true,
        "httpOnly": false,
        "name": "g_state",
        "path": "/",
        "sameSite": "unspecified",
        "secure": false,
        "session": false,
        "storeId": 0,
        "value": "{\"i_l\":0}"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1719708604.775095,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_ga",
        "path": "/",
        "sameSite": "unspecified",
        "secure": false,
        "session": false,
        "storeId": 0,
        "value": "GA1.2.1634364090.1681022282"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1685235004,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_gid",
        "path": "/",
        "sameSite": "unspecified",
        "secure": false,
        "session": false,
        "storeId": 0,
        "value": "GA1.2.1060422423.1685148605"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1715236673.947662,
        "hostOnly": false,
        "httpOnly": true,
        "name": "auth_token",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "0dc3006bbc5fcc8704f17cc1467321c6ca2965c9"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1715236675.292312,
        "hostOnly": false,
        "httpOnly": false,
        "name": "ct0",
        "path": "/",
        "sameSite": "lax",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "8cc635c981c831fb395a0dc819ba5a9128ea48a358236fc8fcf61aa16d36c1e70d13aa0d6f4f5a2211802df4a792971d74adfa6ebf9a12d4efe74c2b396397e88fc087cd7ee05800efbd5f0da4c03511"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1696574278.611481,
        "hostOnly": false,
        "httpOnly": false,
        "name": "d_prefs",
        "path": "/",
        "sameSite": "unspecified",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1719708609.805663,
        "hostOnly": false,
        "httpOnly": false,
        "name": "guest_id_ads",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "v1%3A168102195151679771"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1719708609.80573,
        "hostOnly": false,
        "httpOnly": false,
        "name": "guest_id_marketing",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "v1%3A168102195151679771"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1715236673.947557,
        "hostOnly": false,
        "httpOnly": true,
        "name": "kdt",
        "path": "/",
        "sameSite": "unspecified",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "DuVFGrVgPDD4y1CfzeDlPVNuBBHMxEgLrLBXg4AE"
    },
    {
        "domain": "twitter.com",
        "hostOnly": true,
        "httpOnly": false,
        "name": "lang",
        "path": "/",
        "sameSite": "unspecified",
        "secure": false,
        "session": true,
        "storeId": 0,
        "value": "en"
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1719708609.805767,
        "hostOnly": false,
        "httpOnly": false,
        "name": "personalization_id",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "\"v1_gkiNlP1FYeAIxfQuq1e2lw==\""
    },
    {
        "domain": ".twitter.com",
        "expirationDate": 1716684610.399023,
        "hostOnly": false,
        "httpOnly": false,
        "name": "twid",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": 0,
        "value": "u%3D1427958760157241354"
    }
]

twitter.login_cookie(cookies=list_of_cookies)

# Membuka file tweet_target.txt
with open("tweet_target.txt", "r") as file:
    # Membaca setiap baris dalam file
    for line in file:
        tweet_url = line.strip()  # Menghapus karakter newline (\n)
        twitter.like(tweet_url=tweet_url)
