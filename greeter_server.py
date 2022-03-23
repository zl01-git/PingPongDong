from concurrent import futures
import logging
import seqlog
import ping_pong_dong_pb2
import ping_pong_dong_pb2_grpc
import grpc


class Greeter(ping_pong_dong_pb2_grpc.GreeterServicer):

    def PingPongDong(self, request, context):
        logger.debug('PingPongDong() was started...')
        if request.ping == 'ping':
            logger.info('request from client is "ping", "pong" was returned')
            return ping_pong_dong_pb2.PongReply(pong="pong")
        else:
            logger.warning('request from client is NOT "ping", "err" was returned')
            return ping_pong_dong_pb2.PongReply(pong='err')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ping_pong_dong_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    seqlog.log_to_seq(
        server_url="http://localhost:5341/",
        api_key="AoldN3r8PI0daedXOw6p",
        level=10,
        batch_size=10,
        auto_flush_timeout=10,
        override_root_logger=True
    )
    logger = logging.getLogger('log.server')

    serve()
    