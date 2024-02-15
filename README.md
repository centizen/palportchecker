# Palworld Server Open Port Checker

## Why?

Palworld's server uses UDP packets to communicate between your game server and the players clients. This means that regular open port checking tools are unable to properly detect if your port is open or not. Most tools and sites make use of TCP packets, which your server will happily ignore. For more information, check out https://nmap.org/book/scan-methods-udp-scan.html

That is why when you scan your port with a regular checker, it will almost always come back as open-filtered. This tells you that the port is either open, or it's not. Real helpful.

This script will send a specially crafted UDP packet to your server, which if everything is configured correctly, will cause your server to respond and verify that external players should be able to connect to your server.

## To Use:

You can access an interactive jupyter notebook for this script at:

https://colab.research.google.com/drive/1qAkIcJWS9YFH_UcGNPYG2e2yJpNj1BW_?usp=sharing

## Disclaimer

There really isn't any way this can cause problems, but if it does, it's on you. I don't even know how to read. 

For game version 1.4.1

Future game versions may break compatibility with this script.
