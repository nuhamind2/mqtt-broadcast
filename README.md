# mqtt-web-broadcast
Broadcast data to multiple client

Broadcast data from server to multiple clients (like browser), backed by NATS server. Useful for stuff like server sent event. Originally written for realtime web application.

#### What is NATS server
NATS server is high-performance, lightweight topic based PUB-SUB broker. Kind of Kafka without persistence and queuing, or like MQTT without QOS 1 and QOS 2 semantic

#### How does it work
Client(s) send subscription request toward mqtt-web-broadcast which then translate the request and forward to NATS server. Whenever NATS server publish matching message, it is forwarded to the original client. If multiple client subscribe to the same topic, only the first request is forwarded to the NATS server. Later request is simply recorded for broadcasting target. Example, if 10 clients subscibr to the same topic, NATS server only sent any matching message *once*.

#### Client protocol
mqtt-web-broadcast use MQTT (obviously) for client protocol but do not perform topic matching by itself. Client to client communication is impossible unlike regular mqtt broker. Publish message from client is ignored. Browser client can use websocket but it is also support plain TCP transport.




