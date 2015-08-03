#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()