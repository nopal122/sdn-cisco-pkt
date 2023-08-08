# Software-Defined Networking

Software-Defined Networking (SDN) is an approach to networking that uses software-based controllers or application programming interfaces (APIs) to communicate with underlying hardware infrastructure and direct traffict network

## Project Summary

In this project, I've created an enterprise network topology and managed it through Network Controller in Cisco Packet Tracer and also Telegram Bot using Python. This Telegram Bot will help notify the admin if there's a network issue inside the network. Here's some screenshot of the execution and the network topology:

![Telegram Bot](https://drive.google.com/file/d/1ENKew_LlFLSYyD7YmjWt7BLwDEys_zfG/view?usp=sharing)
![Terminal](image-2.png)
![Network Topology](image-3.png)

## Installation

Follow the installation guide below to try execute the project :

1. [Download](https://www.netacad.com/portal/resources/packet-tracer) Cisco Packet Tracer. 
2. Download the .pkt file and open it in Cisco Packet Tracer
3. Double click on "PC-PT CEO"
4. Head to the programming page
5. Click "Run" on the main.py file to execute the code

Follow the step below to configure the Telegram Bot :

1. Head to [Telegram Web](https://web.telegram.org)
2. Search for @BotFather in Telegram
3. Type ```/newbot``` in the text box
4. Follow the answer of the bot and you will get an API Token from the bot
5. Create a multichat and invite your bot to your multichat
6. Take a note of your chat ID of your multichat (For example : ```web.telegram.org/z/-795654657```). "-**795654657**" is your chat ID of your multichat
7. Replace the ```bot_token``` and ```bot_chatID``` variable with your own token and ID in the python code



