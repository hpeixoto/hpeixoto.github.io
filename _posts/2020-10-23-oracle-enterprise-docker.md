---
layout: post
title: Install Oracle Enterprise 12 with Docker
image: /img/oracle.jpg
tags: docker database oracle
---

Oracle has been one of the most successfull RDBMs in the world over the last decades!  And the main goal of this howTO is to build an Oracle and Docker infrastructure for lectures and testing.

Host server is running *CentOS 7* and running docker and docker-compose, let us start:

- Register in [Dockerhub.com](https://hub.docker.com/)

- Follow to [Oracle Enterprise 12c](https://hub.docker.com/_/oracle-database-enterprise-edition) official docker image, and subscribe to it clicking on the "Proceed to check out" button.

- Login to Dockerhub in your server using dockerhub credentials:

        # docker login

- Pull Oracle Image:

        # docker pull store/oracle/database-enterprise:12.2.0.1

- Ensure Oracle Image is ok:

        # docker image ls


- One of the most hard tasks is to ensure the right permissions to write the new volume on host server, to be able to access to your data. First of all, it is necessary to create users, folders and permissions. Assuming my user is *uminho*, I executed the following commands:

        -- Add users:
        # groupadd -g 54321 oinstall 
        # groupadd -g 54322 dba 
        # useradd -u 54321 -g oinstall -G dba oracle
        
        -- Create project folder
        # cd /home/uminho
        # mkdir dockers

        -- Create data folder for the containers
        # cd /home/uminho/dockers
        # mkdir data

        -- create folder for oracle container
        # cd /home/uminho/dockers/data/
        # mkdir oracle

        -- Ensure Permissions
        # chown -R oracle:dba /home/uminho/dockers/data/oracle 
        # chmod 777 -R /home/uminho/dockers/data/oracle

- Create docker-compose.yml file in /home/uminho/dockers

        version: '3'
        services: 
           oracle:
              container_name: oracledb
              image: store/oracle/database-enterprise:12.2.0.1
           ports:
              - 1521:1521
              - 5500:5500
           volumes:
              - "./data/oracle:/ORCL"
           env_file:
              - ora.conf

- Create ora.conf file inside /home/uminho/dockers/
        
        DB_SID=ORCLCDB
        DB_PDB=orclpdb1

- Start you container
	
        # cd /home/uminho/dockers/
        # docker-compose up -d

- Check if it is running

        # docker ps -a

- Your container should provide "health: starting" as status. After a few minutes it should go live and the status changes to "healthy".

And thats it!! You should have a running Oracle Database in your system! To start creating schemas you should connect to your PDB and use *system* as your user. Default password is **Oradoc_db1**.

