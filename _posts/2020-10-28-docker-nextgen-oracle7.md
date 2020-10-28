---
layout: post
title: Install NextGen to connect to Oracle7 and Oracle12
image: /img/lab.png
tags: docker nextgen oracle7 
---


1. In your server run login to [https://hub.docker.com](https://hub.docker.com). This image is private, therefore you will need user and password. Reach out to me!

        # docker login

2. Pull the necessary docker image:

        # docker pull aidahitech/nextgen


3. Create the docker-compose.yml file:

        # nano docker-compose.yml

        version: '3'
        services:
          portainer:
            container_name: portainer
            image: portainer/portainer-ce
            command: -H unix:///var/run/docker.sock
            restart: always
            ports:
              - 9000:9000
            volumes:
              - "/var/run/docker.sock:/var/run/docker.sock"
              - "./data/portainer:/data"
              - "/etc/timezone:/etc/timezone:ro"
              - "/etc/localtime:/etc/localtime:ro"

          nextgendb:
            container_name: nextgendb
            network_mode: bridge
            image: mysql
            command: mysqld --innodb-buffer-pool-size=20M
            volumes:
              - "./data/nextgendb:/var/lib/mysql"
            environment:
              - "MYSQL_DATABASE=nextgendb"
              - "MYSQL_USER=nextgen"
              - "MYSQL_PASSWORD=nextgenpwd"
              - "MYSQL_ROOT_PASSWORD=nextgenrootpwd"
            ports:
              - "3306:3306"
            expose:
              - "3306"

          nextgen:
            network_mode: bridge
            image: aidahitech/nextgen
            container_name: nextgen
            environment:
              - DATABASE=mysql
              - DATABASE_URL=jdbc:mysql://nextgen:3306/nextgendb
              - DATABASE_MAX_CONNECTIONS=20
              - DATABASE_USERNAME=nextgen
              - DATABASE_PASSWORD=nextgenpwd
            volumes:
              - "./data/nextgen/:/var/spool/mirth"
            ports:
              - "9090:8080"
              - "8443:8443"
              - "4001:4001"
              - "4002:4002"
            links:
              - nextgendb
            depends_on:
              - nextgendb

4. Run the docker-compose

        # docker-compose up -d

5. After this you will have the mirthserver up and running!

6. Connect to your Administrator via [https://host:8443](https://host:8443)

7. Access Mirth settings then Resources

8. Click on "Add Resource" and chose any name you want. Let's say ora7 for example.

9. In the directory field fill: "custom-lib/ora"

10. Make sure "[Default Resource]" has "Include all subdirecotries" *unselected* and hit save.

11. After this hit refresh and verify that you have oracle.jar lodaded in bottom shelf.

And that is it! Whenever you wanna connect to oracle7 you just need to select the ora7 library loaded in the channel "Summary" -> "Dependencies" settings. Imagine you want to connect to oracle7 and write to oracle12, you need to set your source controler to ora7 and destination controler to the Default Resource.