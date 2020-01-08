FROM fedora:31

RUN dnf install -y curl java-11-openjdk python
RUN cd /root/ && curl -O https://raw.githubusercontent.com/m0cchi/wait_for_tcp/master/wait_for_tcp.py && chmod +x wait_for_tcp.py
RUN cd /root/ && curl -O https://www-us.apache.org/dist/kafka/2.4.0/kafka_2.13-2.4.0.tgz && tar zxf kafka_2.13-2.4.0.tgz
