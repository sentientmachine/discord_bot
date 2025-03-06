#!/usr/bin/python3
# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook
import requests
import urllib
import re
from urllib.request import urlopen
import json
import os

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

def members_only_playlist_print():
    global dictionary_of_posts

    channelname = "charitycodes"
    #latest_video = get_latest_video_from_channelname(channelname)
    api_key = global_properties["api_key"]

    channel_id = "UCo1NMrqJxSVNkk8ScVyEreQ"

    #channel_id = "UCo1NMrqJxSVNkk8ScVyEreQ"
    playlistId = "UUMOo1NMrqJxSVNkk8ScVyEreQ"
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/playlistItems?'

    first_url = base_search_url+'key={}&playlistId={}&part=snippet,id&order=date&maxResults=45'.format(api_key, playlistId)

    print("first_url: '" + str(first_url) + "'")

    #first_url = "https://www.youtube.com/playlist?list=UUMOo1NMrqJxSVNkk8ScVyEreQ"
    url = first_url
    resp = requests.get(url)
    resp_json = resp.json()

    print("============================")
    print(type(resp_json))

    video_links = []
    date_links = []
    video_description = []

    #{'kind': 'youtube#playlistItem', 'etag': 'MUPoFHrOktNIZI2wuxzjB6DOPSQ', 'id': 'VVVNT28xTk1ycUp4U1ZOa2s4U2NWeUVyZVEuQzFqM1A1SUxQYVE', 'snippet': {'publishedAt': '2025-03-05T13:12:09Z', 'channelId': 'UCo1NMrqJxSVNkk8ScVyEreQ', 'title': 'Climbing for the win but not how you think | Super Sim Challenge', 'description': "Is it possible to get the bronze lofty achievements climbing award for the Mount Komorebi mountain climbing excursion?\n\nSuper Sim, Series 2, Episode 16: The kids are almost ready to age up to teenagers and then we'll be going to university housing.\n\nSee the rest of the series at https://www.youtube.com/playlist?list=PLad4xijgRPIvAkn8gzCgA_EvqtFUEiltM\n\nJoin this channel to get access to perks:\nhttps://www.youtube.com/channel/UCo1NMrqJxSVNkk8ScVyEreQ/join\n\nJoin my new Discord Server: https://discord.gg/KhCDsMM7KS\n\n#sims4 #supersimchallenge #supersim #thesims4 #ts4 #gameplay #simsletsplay", 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/C1j3P5ILPaQ/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/C1j3P5ILPaQ/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/C1j3P5ILPaQ/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/C1j3P5ILPaQ/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/C1j3P5ILPaQ/maxresdefault.jpg', 'width': 1280, 'height': 720}}, 'channelTitle': 'Charity Codes', 'playlistId': 'UUMOo1NMrqJxSVNkk8ScVyEreQ', 'position': 0, 'resourceId': {'kind': 'youtube#video', 'videoId': 'C1j3P5ILPaQ'}, 'videoOwnerChannelTitle': 'Charity Codes', 'videoOwnerChannelId': 'UCo1NMrqJxSVNkk8ScVyEreQ'}}


    for item in resp_json['items']:
        #print("1=====")
        #print(type(item))
        print("2=====")
        print(item)
        print("3=====")
        
        id_kind_object = str(item["kind"])
        if str(id_kind_object) == "youtube#playlistItem":
            print("adding one")
            video_links.append(base_video_url + item['id'])
            date_links.append(str(item['snippet']['publishedAt']))
            video_description.append(str(item['snippet']['description']))


    #triggerword = "collectibles"

    triggerword = "Komorebi"

    for item_date, videolink, vid_desc in zip(date_links, video_links, video_description):
        print("vid_desc: '" + str(vid_desc) + "'")
        print("triggerword: '" + str(triggerword) + "'")

        if re.findall(triggerword, vid_desc) != []:
            #If it goes from membersonly to public we want to get a discord message.
            superkey = "membersonly " + str(videolink) + " " + str(vid_desc)
            dictionary_of_posts = load_post_data()
            if superkey not in dictionary_of_posts:
                dictionary_of_posts[superkey] = 1
                write_post_data()
                post_message_on_discord("This Members only video contains the triggerword '" + \
                                        str(triggerword) + "' in the description.\n" + \
                                        str(item_date) + "\n" + str(vid_desc) + "\n" + str(videolink))
            else:
                pass


        else:
            print("vid_desc: '" + str(vid_desc) + "'")
            print("does not contain triggerword: " + str(triggerword) + "\n")


    print("done")


def channel_id_list_print():
    global dictionary_of_posts
    channelname = "charitycodes"
    api_key = global_properties["api_key"]

    channel_id = "UCo1NMrqJxSVNkk8ScVyEreQ"

    playlistId = "UUMOo1NMrqJxSVNkk8ScVyEreQ"
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    print("first_url: '" + str(first_url) + "'")

    #first_url = "https://www.youtube.com/playlist?list=UUMOo1NMrqJxSVNkk8ScVyEreQ"
    url = first_url
    resp = requests.get(url)
    resp_json = resp.json()

    print("============================")
    print(type(resp_json))

    print("resp_json: '" + str(resp_json) + "'")
    video_links = []
    video_description = []
    date_links = []

    for item in resp_json['items']:
        #print("1=====")
        #print(type(item))
        #print("2=====")
        #print(item)
        #print("3=====")

        if str(item["id"]["kind"]) == "youtube#video":
            video_description.append(str(item['snippet']['description']))
            video_links.append(base_video_url + item['id']["videoId"])
            date_links.append(str(item['snippet']['publishedAt']))

    #triggerword = "beloved"
    triggerword = "Fabulously"
    #triggerword = "#spideybot"

    for item_date, videolink, vid_desc in zip(date_links, video_links, video_description):

        if re.findall(triggerword, vid_desc) != []:
            print("item_date: '" + str(item_date) + "'")
            print("videolink: '" + str(videolink) + "'")
            print("vid_desc: '" + str(vid_desc) + "'")
            #If it goes from membersonly to public we want to get a discord message.
            superkey = "publicposts " + str(videolink) + " " + str(vid_desc)
            dictionary_of_posts = load_post_data()
            if superkey not in dictionary_of_posts:
                dictionary_of_posts[superkey] = 1
                write_post_data()
                post_message_on_discord("This public video contains the triggerword '" + str(triggerword) + \
                                        "' in the description.\n" + str(item_date) + "\n" + \
                                        str(vid_desc) + "\n" + str(videolink))

        else:
            print("vid_desc: '" + str(vid_desc) + "'")
            print("does not contain triggerword: " + str(triggerword))


    print("done")

global_properties = load_properties_file(".config")
print("global_properties: '" + str(global_properties) + "'")
webhook_url = global_properties["webhook_url"]

def load_post_data():
    global dictionary_of_posts
    if os.path.isfile("postdata.json"):
        with open('postdata.json', 'r') as fp:
            dictionary_of_posts = json.load(fp)
    else:
        dictionary_of_posts = {}
    return dictionary_of_posts

def write_post_data():
    global dictionary_of_posts
    with open('postdata.json', 'w') as fp:
        json.dump(dictionary_of_posts, fp)



channel_id_list_print()
members_only_playlist_print()



