import re
import argparse

def twitter_handle(handle):
    return handle if re.match("^@", handle) else "@" + handle

arg_parser = argparse.ArgumentParser(
    description="""
    """,
)
arg_parser.add_argument(
    "-f", "--file",
    help="YAML file to load suites and kinds from",
    type=argparse.FileType('r'),
    default="data.yaml"
)
arg_parser.add_argument(
    "-r", "--reply_to",
    help="Formatted as a reply",
    type=twitter_handle,
    default=None
)
arg_parser.add_argument(
    "-c", "--credentials",
    help="YAML file to load credentials from",
    type=argparse.FileType('r')
    # default="twitter_credentials.yaml"
)
arg_parser.add_argument(
    "-p", "--publish",
    help="Publish to Twitter (requires credentials file)",
    type=bool,
    default=False
)