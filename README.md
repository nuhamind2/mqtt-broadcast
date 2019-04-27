# mqtt-web-broadcast
Broadcast data to multiple client

Broadcast data from server to multiple clients (like browser), backed by NATS server. Useful for stuff like server sent event. Originally written for ~~me to learn nodejs~~ realtime web application.

#### What is NATS server
NATS server is high-performance, lightweight topic based PUB-SUB broker. Kind of Kafka without persistence and queuing, or like MQTT without QOS 1 and QOS 2 semantic

#### How does it work
Client(s) send subscription request toward mqtt-web-broadcast which then translate the request and forward to NATS server. Whenever NATS server publish matching message, it is forwarded to the original client. If multiple client subscribe to the same topic, only the first request is forwarded to the NATS server. Later request is simply recorded for broadcasting target. Example, if 10 clients subscibr to the same topic,only one subscription request is forwarded and so NATS server only publish matching message *once* (instead of ten times)

#### Client protocol
mqtt-web-broadcast use MQTT (obviously) for client protocol but do not perform topic matching by itself. Client to client communication is impossible unlike regular mqtt broker. Published message from client is ignored. Browser client may use websocket but it is also support plain TCP transport.

#### Monitoring
There is http based monitoring endpoint. 
- /clients

  get client list

- /disconnect/{_clientId_}

  forcefully disconnect client with clientId _clientId_

- /subscriptions

  get subscription list (who subscribe to what)


#### Architecture
See docs/assets/

#### Example
See example/

### Similar (and better) project
These program below can be used to implement server sent event (and probably better than this application)
- [centrifugo](https://github.com/centrifugal/centrifugo)
- [resgate](https://github.com/jirenius/resgate)




