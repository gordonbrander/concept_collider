#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import random
import yaml
from arg_parser import arg_parser
from twitter import Twitter, OAuth

idea_characters = (
    u"🐵💭",
    u"🐔💭",
    u"🦄💭",
    u"😮💭",
    u"😇💭",
    u"🤑💭",
    u"👻💭",
    u"😲💭",
    u"😅💭",
    u"😎💭",
    u"😈💭",
    u"😺💭",
    u"🤔💭",
    u"🤖💭",
    u"🗿💭",
    u"🐻💭",
    u"💸💭",
    u"🚀💭"
)

future_characters = (
    u"👋🔮",
)

def template(data, reply_to=None):
    story = u"" + random.choice(data["story"])
    tech, tech2 = random.sample(data["tech"], 2)
    space = data["terrain"] + data["mood"] + data["thing"] + data["startups"]
    application = data["terrain"] + data["thing"] + data["startups"]
    zeit = data["arc"] + data["mood"]
    msg = story.format(
        tech=tech,
        tech2=tech2,
        terrain=random.choice(data["terrain"]),
        arc=random.choice(data["arc"]),
        time=random.choice(data["time"]),
        application=random.choice(application),
        space=random.choice(space),
        zeit=random.choice(zeit),
        future_char=random.choice(future_characters),
        idea_char=random.choice(idea_characters)
    )
    return msg

def cmd_main():
    args = arg_parser.parse_args()
    data = yaml.load(args.file.read())
    msg = template(data, reply_to=args.reply_to)
    if args.publish and args.credentials:
        credentials = yaml.load(args.credentials.read())
        auth = OAuth(
            credentials["token"],
            credentials["token_secret"],
            credentials["consumer_key"],
            credentials["consumer_secret"]
        )
        twitter = Twitter(auth=auth)
        twitter.statuses.update(status=msg)
        print(msg)
    else:
        print(msg)

if __name__ == '__main__':
    cmd_main()
