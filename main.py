#!/usr/bin/python3
# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook

import requests
import urllib
from urllib.request import urlopen
import json

def load_properties_file(filepath, sep='=', comment_char='#'):
    #Read the file passed as parameter as a properties file.
    props = {}
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value
    return props

def post_message_on_discord(msg):
    webhook = DiscordWebhook(url=webhook_url , content=msg)
    response = webhook.execute()
    print("Done")

def get_latest_video_from_channelname(channelname):
    latest_video = "...."

    #On Thanos, in HistoricalData_Coinbase_cdp.py there is an example of oauth2 with google

    #No Screen Scraping nonsense
    #https://developers.google.com/youtube/v3/
   
    #Use the oauth2 example code

    #Do the google app engine oauth2 like before, and get the jason web token to re-oauth2

    #Get latest
    return latest_video

def get_date_of_youtube_video(youtube_video_url):
    date_of_youtube_video = "..."
    return date_of_youtube_video

global_properties = load_properties_file(".config")
print("global_properties: '" + str(global_properties) + "'")

webhook_url = global_properties["webhook_url"]

channelname = "charitycodes"
#latest_video = get_latest_video_from_channelname(channelname)

#print(get_date_of_youtube_video(...))


api_key = global_properties["api_key"]

channel_id = "UC4uDAtrSnv_qj-hkS0NYSxA"

base_video_url = 'https://www.youtube.com/watch?v='
base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
url = first_url
resp = requests.get(url)
resp_json = resp.json()

video_links = []
date_links = []
for i in resp_json['items']:
    print(i)
    print("")
    #if i['id']['kind'] == "youtube#search":
    if str(i['id']['kind']) == "youtube#video":
        video_links.append(base_video_url + i['id']['videoId'])
        date_links.append(str(i['snippet']['publishedAt']))

print("video_links: '" + str(video_links) + "'")
print("date_links: '" + str(date_links) + "'")


print("done")








#post_message_on_discord("testingasdf")


