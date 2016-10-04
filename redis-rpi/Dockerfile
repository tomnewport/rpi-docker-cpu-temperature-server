FROM sdhibit/rpi-raspbian:latest

RUN apt update
RUN apt install -y make wget build-essential

WORKDIR /tmp/
RUN wget http://download.redis.io/redis-stable.tar.gz
RUN tar xvzf redis-stable.tar.gz

WORKDIR /tmp/redis-stable/deps/
RUN make hiredis jemalloc linenoise lua geohash-int

WORKDIR /tmp/redis-stable/
RUN make install

EXPOSE 6379

CMD redis-server /etc/redis.conf
