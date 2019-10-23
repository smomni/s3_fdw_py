FROM postgres:11.1

RUN apt-get update -yqq && \
    apt-get install -yqq python3-pip python3-dev git && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install --upgrade pip

RUN apt-get install -yqq postgresql-server-dev-11

COPY . /s3_fdw/
WORKDIR /s3_fdw

RUN git clone git://github.com/Kozea/Multicorn.git && \
    cd Multicorn && \
    git checkout 9ff78759665b0d04315f707b81a45c66ecb2d8c7 && \
    make && make install

RUN pip install -r requirements.txt && \
    pip install .