# Palworld Server Open Port Checker

## Why?

Palworld's server uses UDP packets to communicate between your game server and the players clients. This means that regular open port checking tools are unable to properly detect if your port is open or not. Most tools and sites make use of TCP packets, which your server will happily ignore. That is why when you scan your port with a regular checker, it will almost always come back as open-filtered. This tells you that the port is either open, or it's not. Real helpful.

For more information, check out https://nmap.org/book/scan-methods-udp-scan.html

This script will send a specially crafted UDP packet to your server, which if everything is configured correctly, will cause your server to respond and verify that external players should be able to connect to your server.

## To Use:

You can access an interactive jupyter notebook for this script at:

https://colab.research.google.com/drive/1nBvIUY1Xb6H_2oo0y-1ErrtIZdOG_A0g?usp=sharing

## Disclaimer

There really isn't any way this can cause problems, but if it does, it's on you. I don't even know how to read. 

For game version 1.4.1

Future game versions may break compatibility with this script.

## Why isn't my server working?

- Make sure your port forwarding rule is for UDP, or TCP/UDP. A TCP only Port Forward will not work
- Make sure that your external IP/WAN IP you get on your router matches what you get from a checker like icanhazip.com. If it doesn't match, you are behind an additional router and will need to get that sorted out for this to work.
- Make sure you have assigned a static IP to your server and configured the port forwarding rule to that
- Make sure you have also opened the ports in Windows Firewall, nftables, iptables or whatever firewall your OS includes
- Check to make sure your server is actually listening on the expected port by running "netstat -ano" (command is the same on both Windows and linux) and seeing if it comes up in the list
- The only port you actually need to focus on while troubleshooting is the main game port (default 8211). You can ignore all the rest of them; 7777, 27015-6 and 25575 are used for other services.
- Make sure you aren't running any of those stupid VPN services like NordVPN or SurfShark on the PC you are running your server on 
