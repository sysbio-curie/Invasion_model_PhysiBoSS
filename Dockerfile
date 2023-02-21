FROM ubuntu:focal
MAINTAINER Marco Ruscone <marco.ruscone@curie.fr>

USER root

# create user with a home directory
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid 1000 \
    user

RUN apt-get -qq update && apt-get install -yq flex bison python3-pip
RUN pip3 install jupyter notebook scipy matplotlib hublib joblib==1.1.1

WORKDIR /home/user
COPY . /home/user
RUN mkdir /home/user/bin/__pycache__
RUN chown -R 1000 /home/user

USER user
ENV CACHEDIR /home/user/bin/__pycache__

RUN cd /home/user/src; make; cp myproj ../bin; cd ../..

CMD cd /home/user; jupyter notebook --ip=0.0.0.0 --NotebookApp.token=''
