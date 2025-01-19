#!/usr/bin/python3
# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook

def post_message_on_discord(msg):
    #get discord channel read and write functionality here

    webhook_url = "https://discord.com/api/webhooks/1330601225682554991/vvTYfOY2lZQegnKLpEaFAJb_tCMtd2NJcMKcH9Bq3Fd95X9HVqsmZ6mWVRuCEHzdBPeT"
    webhook = DiscordWebhook(url=webhook_url , content=msg)
    response = webhook.execute()


    print("Done")



post_message_on_discord("This is a test message from thanos through webhook using DiscordWEbhook python 3.10.8")


