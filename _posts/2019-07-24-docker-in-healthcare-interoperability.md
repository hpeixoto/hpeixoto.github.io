---
layout: post
title: Docker for healthcare interoperability
image: /img/docker.png
tags: docker nextgen hl7 interoperability
---

Can Docker, Mirthconnect and HL7 be the answer to healthcare interoperability?

On the last few day I have been messing around with [Docker](https://www.docker.com/ "Docker"), [NextGen®](https://www.nextgen.com/products-and-services/integration-engine "NextGen®") and came up with a little setup for the first experiments!! I will focus on the docker setup for now, and later I will present more detailed info on NextGen channels created!

The goal was to build a framework with 2 nextgen agents, each one based on a mySQL database. The final step establish communication between them by hl7.

I have an Ubuntu Server 16.04LTS freshly installed on my *Virtual Box*, and I started my quest! I followed some tutorials, but you can have all the best information from  [docker docs](https://docs.docker.com/).

1. Update and upgrade the system

        $ sudo apt upgrade
        $ sudo apt update

2. Install docker

        $ sudo apt install docker

3. After docker was installed I had two options: build my own docker or use something already available. I went for the easiest one... I had no time to waste! I used fabrom/mirth-connect-docker from github!

        $ git clone https://github.com/fabrom/mirth-connect-docker.git

4. Since I had no past experience with docker, I had some issues trying to understand how ports and dns works inside the infrastructure! But after some carefull online search I was able to edit  _docker-compose.yml_ according to my needs!   
First of all added the [portainer](https://www.portainer.io/) container for logs and management.


                portainer:
                    image: portainer/portainer
                    command: -H unix:///var/run/docker.sock
                    restart: always
                    ports:
                    - 9000:9000
                    volumes:
                    - "/var/run/docker.sock:/var/run/docker.sock"
                    - "./data/portainer_data:/data"


    The second step was to build 2 containers of each: Two for the mySQL databases and two for the NextGen software. My final _docker-compose.yml_ is here:

            version: '2'
                services:
                portainer:
                    image: portainer/portainer
                    command: -H unix:///var/run/docker.sock
                    restart: always
                    ports:
                    - 9000:9000
                    volumes:
                    - "/var/run/docker.sock:/var/run/docker.sock"
                    - "./data/portainer_data:/data"

                mirthdb1:
                    container_name: mirthdb1
                    image: mysql:5.6
                    command: mysqld --innodb-buffer-pool-size=20M
                    volumes:
                    - "./data/db1:/var/lib/mysql:rw"
                    environment:
                    - "MYSQL_DATABASE=mirthdb"
                    - "MYSQL_USER=mirth"
                    - "MYSQL_PASSWORD=password"
                    - "MYSQL_ROOT_PASSWORD=password"
                    ports:
                    - "3311:3306"

                mirthdb2:
                    container_name: mirthdb2
                    image: mysql:5.6
                    command: mysqld --innodb-buffer-pool-size=20M
                    volumes:
                    - "./data/db2:/var/lib/mysql:rw"
                    environment:
                    - "MYSQL_DATABASE=mirthdb2"
                    - "MYSQL_USER=mirth"
                    - "MYSQL_PASSWORD=password"
                    - "MYSQL_ROOT_PASSWORD=password"
                    ports:
                    - "3312:3306"

                mirthconnect1:
                    build: mirth-connect
                    image: fabrom/mirth-connect
                    container_name: mirthconnect1
                    volumes:
                    - "./mirth-connect/mirth.properties:/opt/mirth-connect/conf/mirth.properties:rw"
                    - "./data/spool_mirth/:/var/spool/mirth/:rw"
                    ports:
                    - "9091:8080"
                    - "9441:8443"
                    links:
                    - mirthdb1
                    depends_on:
                    - mirthdb1

                mirthconnect2:
                    build: mirth-connect
                    image: fabrom/mirth-connect
                    container_name: mirthconnect2
                    volumes:
                    - "./mirth-connect/mirth2.properties:/opt/mirth-connect/conf/mirth.properties:rw"
                    - "./data/spool_mirth2/:/var/spool/mirth/:rw"
                    ports:
                    - "9092:8081"
                    - "9442:8444"
                    - "6661:6661"
                    links:
                    - mirthdb2
                    - mirthconnect1
                    depends_on:
                    - mirthdb2
                    - mirthconnect1

    As one can see, there i the need to link the databases to the NextGen containers and port management should be taken in careful consideration.

    > *NextGen1 (mirthconnect1)* has two ports, both http(9091) and https(9441), depends and links on Mysql1(mirthdb1) with the port (3111)   
    >   
    > *NextGen1 (mirthconnect2)* has three ports, both http(9092) and https(9442) as mirthconnect1, but also 6661 to be the reciever end of hl7 messages, depends and links on Mysql2(mirthdb2) with the port (3112) and *NextGen1(mirthconnect1)*

    As stated by the volumes in NextGen1 and 2, there is the need to correctly define mirth.properties file for each one. Both of those files canbe found in my [github repository](https://github.com/hpeixoto/mirth-connect-docker).

5. The next step is to build the docker image (which can take up some time!):

        $ docker-compose build --force-rm --no-cache --pull --parallel

6. Start the NextGen-docker stack:

        $ docker-compose up -d

7. Stop the NextGen-docker stack:

        $ docker-compose down

Next up I will bring the channels created! stay tunned!
