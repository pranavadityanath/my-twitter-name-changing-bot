# Short code
import tweepy
api_key = 'dE6zSkvmqSFqLpaQSQQ0DXDdH'
api_secret_key = 'Fr6vbc4SBujaKUeCBdWuF3uLDkNppRacC1UBD8b29jz9moKCfQ'
access_token = '1339935823723053058-Fxljvo4mXFWYlF1hQsZv27RvVAV0tg'
secret_access_token = 'fuJlZCHkEqwYuJRvy9eWpnEswFItY5y9JjDLySHflgjvn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_access_token)
api = tweepy.API(auth)
print('Everything is fine')

import time
while True:
  user = api.get_user('ap3des')
  f = user.followers_count
  api.update_profile(name=f'PRANAV {f} Followers')
  print(f'PRANAV {f} Followers')
  time.sleep(60) 
