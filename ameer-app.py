# Short code
import tweepy
consumer_key = 'kg5MaWSyuM2yKcJuXmjrq7eCk'
consumer_secret = 'XHcELNRB1qr2ZXouiBcQWyz95C8RY0WK9tt4Npn5YGEtNqvYcV'
access_token = '1297164703110582274-HRFFBP4VNHSNss4u0npVcOYwpVBf6J'
secret_access_token = 'GgibeHs5ntOovfWFJOHuG9e88CnzNp7wSYqVCr6qyuTJO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_access_token)
api = tweepy.API(auth)
print('Everything is fine')

import time
while True:
  user = api.get_user('Ameen91741779')
  f = user.followers_count
  api.update_profile(name=f'AMEER {f} Followers')
  print(f'AMEER {f} Followers')
  time.sleep(60)
