from globe.connect import oauth

oauth = oauth.Oauth("p6zgtLrX4XH9diMynocXAeH4E6prtz9j", "22ed6602d22b70f31405964a96f5290b75a5de708675046176c6673c3ab0d160")

# get redirect url
print oauth.getRedirectUrl()

# get access token
print oauth.getAccessToken("G6SLj7j5hBokB5HM4dRKhkBx4GuG6zrqC5KnRgCjMMMzfnonMpFaxKXjsd4Aj6tpGjx9sE4ygnIGnA8rSznXRLhjLrReHkRx5dI5brgnsEj9dgCG5BrgCjpX4XH9diMqq4diXAeH4EBpdCar9zbCBgrzEsynxzxIGErAXHbpXgbhgbAAySo9yREI4gjKzsrxA9Kt8rKrBspdnGxFdzMgGf58ndACrMz7ECAqxKRuALdk4hrbkxkH5B76qhprLbnS")
