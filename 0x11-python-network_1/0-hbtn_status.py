#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request as urlR


if __name__ == "__main__":
    link = "https://alx-intranet.hbtn.io/status"
    with urlR.urlopen(link) as marko:
        polo = marko.read()
        print("Body response:")
        print("\t- type: {}".format(type(polo)))
        print("\t- content: {}".format(polo))
        print("\t- utf8 content: {}".format(polo.decode()))
