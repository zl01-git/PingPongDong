from __future__ import print_function
from email import message
import logging
from flask import request
import seqlog
import grpc
import ping_pong_dong_pb2
import ping_pong_dong_pb2_grpc
import time
import sys

def run():
    
    with grpc.insecure_channel('localhost:8080') as channel:
        logger.debug('insecure chanell was opened')
        stub = ping_pong_dong_pb2_grpc.GreeterStub(channel)
        count = 0
        while True:
            count += 1
            if count % 5 == 0:
                response = stub.PingPongDong(ping_pong_dong_pb2.PingRequest(ping='dong'))
                logger.error(f'request "dong" to server was sended, {response.pong} was returned')
            else:
                response = stub.PingPongDong(ping_pong_dong_pb2.PingRequest(ping='ping'))
                logger.info('request "ping" to server was sended')
                print(f'ping\n{response.pong}')
            time.sleep(2)
            


if __name__ == '__main__':
    seqlog.log_to_seq(
        server_url='http://localhost:5341/',
        api_key='qFoArSYdrJ9ZqbK9S3qc',
        level=10,
        batch_size=10,
        auto_flush_timeout=10,
        override_root_logger=True
    )
    logger = logging.getLogger('log.client')
    logger.setLevel(level=30)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.debug('start client function run()')
    run()
    
