Install NATS server from [nats release page](https://github.com/nats-io/gnatsd/releases), then start it with :

`gnatsd -DV`

-DV is flag to enable debug and trace message, usefull for testing. By default NATS server will listen on port 4222

Install NodeJS

clone this repo and install the dependencies

`git clone https://github.com/nuhamind2/mqtt-web-broadcast.git`

Install NATS python client

`pip install asyncio-nats-client`

Run generator.py

Open example.html

