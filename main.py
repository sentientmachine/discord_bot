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
    #get discord channel read and write functionality here

    webhook = DiscordWebhook(url=webhook_url , content=msg)
    response = webhook.execute()

    print("Done")


global_properties = load_properties_file(".config")
print("properties: '" + str(properties) + "'")

webhook_url = global_properties["webhook_url"]

post_message_on_discord("testingasdf")


