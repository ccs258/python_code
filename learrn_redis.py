# -*- coding: utf-8 -*-
# @Time    : 19-1-23 下午11:12
# @Author  : ccs

kwargs = {}
kwargs.update({
                        'connection_class': 'SSLConnection',
                        'ssl_keyfile': 'ssl_keyfile',
                        'ssl_certfile': 'ssl_certfile',
                        'ssl_cert_reqs': 'ssl_cert_reqs',
                        'ssl_ca_certs': 'ssl_ca_certs',
                    })
print(kwargs)
shard_hint = kwargs.pop('shard_hint', None)

connection_class = kwargs.pop('connection_class')

print(shard_hint) #结果为None

print(connection_class) #结果为SSLConnection


####不同的层抛出不同的异常

while response is False:
    try:
        if HIREDIS_USE_BYTE_BUFFER:
            bufflen = recv_into(self._sock, self._buffer)
            if bufflen == 0:
                raise socket.error(SERVER_CLOSED_CONNECTION_ERROR)
        else:
            buffer = recv(self._sock, socket_read_size)
            # an empty string indicates the server shutdown the socket
            if not isinstance(buffer, bytes) or len(buffer) == 0:
                raise socket.error(SERVER_CLOSED_CONNECTION_ERROR)
    except socket.timeout:
        raise TimeoutError("Timeout reading from socket")
    except socket.error:
        e = sys.exc_info()[1]
        raise ConnectionError("Error while reading from socket: %s" %
                              (e.args,))

#redis协议存取数据操作；跟数据库类比；
#建立连接，连接池操作，删除连接；
