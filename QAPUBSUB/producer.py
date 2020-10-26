#!/usr/bin/env python 3
import pika


from QAPUBSUB.base import base_ps
from QAPUBSUB.setting import (qapubsub_ip, qapubsub_password, qapubsub_port,
                              qapubsub_user)

#########  生产者 #########


class publisher(base_ps):
    def __init__(self, host=qapubsub_ip, port=qapubsub_port, user=qapubsub_user, password=qapubsub_password, channel_number=1, queue_name='', routing_key='default',  exchange='', exchange_type='fanout', vhost='/', durable=False):
        super().__init__(host, port, user, password, channel_number,
                         queue_name, routing_key,  exchange, exchange_type, vhost)
        self.channel.queue_declare(
            self.queue_name, auto_delete=True, exclusive=True)
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type='fanout',
                                      passive=False,
                                      durable=durable,
                                      auto_delete=False)
        self.routing_key = routing_key

    def pub(self, text):
        # channel.basic_publish向队列中发送信息
        # exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        # routing_key 指定向哪个队列中发送消息
        # body是要插入的内容, 字符串格式
        if isinstance(text, bytes):
            content_type = 'text/plain'
        elif isinstance(text, str):
            content_type = 'text/plain'
        elif isinstance(text, dict):
            content_type = 'application/json'
        try:
            self.channel.basic_publish(exchange=self.exchange,
                                       routing_key=self.routing_key,
                                       body=text,
                                       properties=pika.BasicProperties(content_type=content_type,
                                                                       delivery_mode=1))
        except Exception as e:
            print(e)
            self.reconnect().channel.basic_publish(exchange=self.exchange,
                                                   routing_key=self.routing_key,
                                                   body=text,
                                                   properties=pika.BasicProperties(content_type=content_type,
                                                                                   delivery_mode=1))

    def exit(self):
        self.connection.close()


class publisher_routing(base_ps):
    def __init__(self, host=qapubsub_ip, port=qapubsub_port, user=qapubsub_user, password=qapubsub_password, channel_number=1, queue_name='', routing_key='default',  exchange='', exchange_type='direct', vhost='/', durable=False):
        super().__init__(host, port, user, password, channel_number,
                         queue_name, routing_key,  exchange, exchange_type, vhost)
        self.routing_key = routing_key
        self.channel.queue_declare(
            self.queue_name, auto_delete=True, exclusive=True)
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type=exchange_type,
                                      passive=False,
                                      durable=durable,
                                      auto_delete=False)

    def pub(self, text, routing_key):
        # channel.basic_publish向队列中发送信息
        # exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        # routing_key 指定向哪个队列中发送消息
        # body是要插入的内容, 字符串格式
        if isinstance(text, bytes):
            content_type = 'text/plain'
        elif isinstance(text, str):
            content_type = 'text/plain'
        elif isinstance(text, dict):
            content_type = 'application/json'
        try:
            self.channel.basic_publish(exchange=self.exchange,
                                       routing_key=routing_key,
                                       body=text,
                                       properties=pika.BasicProperties(content_type=content_type,
                                                                       delivery_mode=1))
        except Exception as e:
            print(e)
            self.reconnect().channel.basic_publish(exchange=self.exchange,
                                                   routing_key=routing_key,
                                                   body=text,
                                                   properties=pika.BasicProperties(content_type=content_type,
                                                                                   delivery_mode=1))

    def exit(self):
        self.connection.close()


class publisher_topic(base_ps):
    def __init__(self, host=qapubsub_ip, port=qapubsub_port, user=qapubsub_user, password=qapubsub_password, channel_number=1, queue_name='', routing_key='default',  exchange='', exchange_type='topic', vhost='/', durable=False):
        super().__init__(host, port, user, password, channel_number,
                         queue_name, routing_key,  exchange, exchange_type, vhost)
        self.routing_key = routing_key
        self.channel.queue_declare(
            self.queue_name, auto_delete=True, exclusive=True)
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type=exchange_type,
                                      passive=False,
                                      durable=durable,
                                      auto_delete=False)

    def pub(self, text, routing_key):
        # channel.basic_publish向队列中发送信息
        # exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        # routing_key 指定向哪个队列中发送消息
        # body是要插入的内容, 字符串格式
        if isinstance(text, bytes):
            content_type = 'text/plain'
        elif isinstance(text, str):
            content_type = 'text/plain'
        elif isinstance(text, dict):
            content_type = 'application/json'
        try:
            self.channel.basic_publish(exchange=self.exchange,
                                       routing_key=routing_key,
                                       body=text,
                                       properties=pika.BasicProperties(content_type=content_type,
                                                                       delivery_mode=1))
        except Exception as e:
            print(e)
            self.reconnect().channel.basic_publish(exchange=self.exchange,
                                                   routing_key=routing_key,
                                                   body=text,
                                                   properties=pika.BasicProperties(content_type=content_type,
                                                                                   delivery_mode=1))

    def exit(self):
        self.connection.close()


if __name__ == '__main__':
    import datetime
    p = publisher(exchange='z3')
    while True:
        print(1)
        p.pub('{}'.format(datetime.datetime.now()))
