import csv 
import requests
from dotenv import load_dotenv
import os
import argparse
import pandas as pd
import json 

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USERNAMES = (os.getenv("USERNAMES")).split(",")

URL_ENDPOINT = "https://api.untappd.com/v4/user/beers/"
UNTAPPD_MAX_LIMT = 50
DEFAULT_PARAMS = {
  "limit": str(UNTAPPD_MAX_LIMT),
  "sort": "highest_rated_you",
  "client_id": CLIENT_ID,
  "client_secret": CLIENT_SECRET,
}

def main():
  blob_by_user = {} 
  for user in USERNAMES:
    blob = {}
    blob['root'] = []
    request_user_beers(user, blob)
    blob_by_user[user] = blob
  
  write_blob_by_user_to_one_csv(blob_by_user)
  print("Done 🍻")

def get_arguments():
  parser = argparse.ArgumentParser(description='Hit the Untappd API for user data 🍻.',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument("--force", action='store_true', default=False,
                      help="Actually make a request. Used so you don't blow through your Untappd API limit.")

  parser.add_argument("--outfile", type=str, default="data.csv",
                      help="Name of outfile. Should match filename in R script.")

  # NOTE: this wrongly assumes all users have checked in 
  # roughly the same number of beers. Perhaps it's more approriate
  # to pass a list of key value pairs
  parser.add_argument("--number-of-unique-beers", type=int, default=49,
                      help="How many unique beers for each user?")

  return parser.parse_args()

def request_user_beers(user, blob):
    url = URL_ENDPOINT + user

    for offset in range(0, args.number_of_unique_beers, UNTAPPD_MAX_LIMT):
      params = DEFAULT_PARAMS
      if offset > 1:
        params = {**DEFAULT_PARAMS, 'offset': str(o)}
      
      if args.force: 
        r = requests.get(url, params = params)
        response = r.json()
      else: 
        response = { 
          'response': 
            {'beers': 
              {'count': 1, 
              'items': [
                {
                  user: "test-response"
                }
              ]
            }
          }
        }

      print("Fetched response with offset: " + str(offset) + " 🍺...")
      construct_user_json(blob, response)

def construct_user_json(blob, response):
  for beer in response['response']['beers']['items']:
    blob['root'].append(beer)

def write_blob_by_user_to_one_csv(blob_by_user):
  data = pd.concat([read_blob_into_df(blob_by_user[user], user) for user in USERNAMES])
  data.to_csv(args.outfile)

def read_blob_into_df(blob, user):
  # flatten data and read into frame
  df = pd.json_normalize(blob, record_path =["root"])
  # track which user it came from
  df.insert(0, "user", user)
  return df

if __name__ == "__main__":
  args = get_arguments()
  main()
