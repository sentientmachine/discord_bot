#!/usr/bin/python3
# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook

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

def get_latest_video_from_channelname("charitycodes"):
    latest_video = "...."

    #No Screen Scraping nonsense
    #Do the google app engine oauth2 like before, and get the jason web token to re-oauth2

    #Get latest
    return latest_video

def get_date_of_youtube_video(youtube_video_url):
    date_of_youtube_video = "..."
    return date_of_youtube_video


global_properties = load_properties_file(".config")
print("global_properties: '" + str(global_properties) + "'")

webhook_url = global_properties["webhook_url"]

latest_video = get_latest_video_from_channelname()

print(get_date_of_youtube_video)



#post_message_on_discord("testingasdf")


