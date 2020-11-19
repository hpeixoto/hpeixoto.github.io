---
layout: post
title: Tarefas de Administração na Arquitetura Multitenant da Oracle
image: /img/lab.png
tags: docker oracle12c multitenant CDB PDB
---

## 1. Ligar à bash do container oracle:
~~~bash
# Descobrir o container-id do Oracle
[user@localhost ~]$ sudo docker ps -a

# Aceder à linha de comandos do container
[user@localhost ~]$ sudo docker exec -it <container-id> bash
~~~

&nbsp;

* * *  

## 2. Passos de ligação a uma CDB ou a uma PDB

#### Ligar à base de dados de root (CDB):

**Como sys as sysdba:**

~~~bash
# Estabelecer ligação à CDB
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1@localhost:1521/ORCLCDB.localdomain as sysdba

# Output:
# SQL*Plus: Release 12.2.0.1.0 Production on Mon Nov 16 05:44:34 2020
# Copyright (c) 1982, 2016, Oracle.  All rights reserved.
# Last Successful login time: Mon Nov 16 2020 04:02:24 +00:00
# Connected to:
# Oracle Database 12c Enterprise Edition Release 12.2.0.1.0 - 64bit Production
# SQL>
~~~

Verificar nome e numero da ligacao: 

~~~sql
-- Consultar nome da ligação:
SQL> show con_name

-- Output:
-- CON_NAME
-- ------------------------------
-- CDB$ROOT

-- Consultar o número da ligação:
SQL> show con_id

-- Output:
-- CON_ID
-- ------------------------------
-- 1
~~~

Mostrar todos os serviços associados à instalação: 

~~~sql
SQL> select name, con_id from v$active_services order by 1;

-- Output:
-- NAME                                                             CON_ID
-- ---------------------------------------------------------------- ----------
-- ORCLCDBXDB                                                       1
-- ORCLCDBXDB                                                       1
-- SYS$BACKGROUND                                                   1
-- SYS$USERS                                                        1
-- orclpdb1.localdomain                                             3
~~~

**Ligar à CDB usando a autenticação do SO:**

~~~bash
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba

# Output:
# SQL*Plus: Release 12.2.0.1.0 Production on Tue Nov 17 06:03:35 2020
# Copyright (c) 1982, 2016, Oracle.  All rights reserved.
# Connected to:
# Oracle Database 12c Enterprise Edition Release 12.2.0.1.0 - 64bit Production
# SQL>
~~~

Verificar nome e numero da ligacao: 

~~~ sql
-- Consultar nome da ligação:
SQL> show con_name

-- Output:
-- CON_NAME
-- ------------------------------
-- CDB$ROOT


-- Consultar o número da ligação:
SQL> show con_id

-- Output:
-- CON_ID
-- ------------------------------
-- 1
~~~

**Ligar a uma Pluggable DataBase (PDB):**

~~~bash
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1@localhost:1521/orclpdb1.localdomain as sysdba
~~~

Verificar nome e numero da ligacao: 

~~~ sql
-- Consultar nome da ligação:
SQL> show con_name

-- Output:
-- CON_NAME
-- ------------------------------
-- ORCLPDB1

-- Consultar o número da ligação:
SQL> show con_id

-- Output:
-- CON_ID
-- ------------------------------
-- 3
~~~

**Ligar a uma PDB através de uma ligação à CDB**

~~~bash
# Aceder à linha de comandos do container
[user@localhost ~]$ sudo docker exec -it <container-id> bash

# Aceder como sysdba à da CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~
~~~sql
-- Estabelecer ligação através da CDB à PDB:
SQL> connect sys/Oradoc_db1@localhost:1521/orclpdb1.localdomain as sysdba

-- Output:
-- Connected.
~~~

&nbsp;

* * *  

## 3. Criar uma PDB a partir da Seed PDB

Antes de começar é necessário criar a pasta para acomodar os ficheiros da nova PDB. Usamos para isso o filesystem do nosso host:

~~~ bash
# Ligar como su:
[user@localhost ~]$ sudo su

# Criar a pasta: 
[user@localhost ~]# sudo mkdir $docker_data/oracle/u02/app/oracle/oradata/ORCL/aebd

# Alterar as permissões:
[user@localhost ~]# chown oracle:oinstall $docker_data/oracle/u02/app/oracle/oradata/ORCL/aebd
~~~

**Ligar à CDB**

Usando a bash do container como anteriormente:

~~~bash
# Aceder à linha de comandos do container
[user@localhost ~]$ sudo docker exec -it <container-id> bash

# Aceder como sysdba à root da CDB:
[oracle@container-id /]$ sqlplus sys/Oradoc_db1 as sysdba  
~~~
~~~sql
-- Comando de criação da PDB através da PDB Seed:
SQL> create pluggable database aebd 
        admin user aebd_admin identified by aebd 
        roles = (DBA) 
        FILE_NAME_CONVERT=('/u02/app/oracle/oradata/ORCL/pdbseed','/u02/app/oracle/oradata/ORCL/aebd');

-- Output:
-- Pluggable database created.
~~~

Verificar o estado da nova PDB criada:

~~~sql
SQL> select pdb_name, status from cdb_pdbs;

-- Output:
-- PDB_NAME                    STATUS
-- ------------------------    ------------
-- AEBD                        NEW
-- PDB$SEED                    NORMAL
-- ORCLPDB1                    NORMAL
~~~

Verificar o open_mode da nova PDB criada (READ WRITE, READ ONLY, MOUNTED):

~~~sql
SQL> select name, open_mode from v$pdbs;

-- Output:
-- NAME                      OPEN_MODE
-- -----------------------   ----------
-- PDB$SEED                  READ ONLY
-- ORCLPDB1                  READ WRITE
-- AEBD                      MOUNTED
~~~

Verificar o Service Name da nova PDB criada:

~~~ sql
SQL> select name, con_id from v$active_services order by 1;

-- Output:
-- NAME                                                          CON_ID
-- ------------------------------------------------------------- ----------
-- ORCLCDB.localdomain                                           1
-- ORCLCDBXDB                                                    1
-- SYS$BACKGROUND                                                1
-- SYS$USERS                                                     1
-- aebd.localdomain                                              5
-- orclpdb1.localdomain                                          3
~~~

Foi criada a nova PDB. É possível ver agora quais os datafiles criados:

~~~ sql
SQL> select name from v$datafile where con_id=4;

-- Output:
-- NAME
-- --------------------------------------------------------------------------------
-- /u02/app/oracle/oradata/ORCL/aebd/system01.dbf
-- /u02/app/oracle/oradata/ORCL/aebd/sysaux01.dbf
-- /u02/app/oracle/oradata/ORCL/aebd/undotbs01.dbf
~~~

* * * 

&nbsp;

* * * 

## 4. Gerir a CDB e as PDB

**Garantir que a ligação estaelecida é à CDB como SYSDBA**

~~~bash
# Aceder à linha de comandos do container
[user@localhost ~]$ sudo docker exec -it <container-id> bash

# Aceder como sysdba à root da CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~
~~~sql
SQL> show con_name

-- Output:
-- CON_NAME
-- ------------------------------
-- CDB$ROOT
~~~

**Desligar a Base de Dados:**

~~~sql
SQL> shutdown immediate

-- Output:
-- Database closed.
-- Database dismounted.
-- ORACLE instance shut down.
~~~

Esta operação desmonta **todas** as PDB, desmonta **todos** os ficheiros de controlo e **desliga** a instância.


**Arrancar a base de dados:**

~~~sql
SQL> startup

-- Output:
-- ORACLE instance started.

-- Total System Global Area 1342177280 bytes
-- Fixed Size                  8792536 bytes
-- Variable Size             620758568 bytes
-- Database Buffers          704643072 bytes
-- Redo Buffers                7983104 bytes
-- Database mounted.
-- Database opened.
~~~

Esta operação monta liga a instância, monta os todos ficheiros de controlo e abre apenas o container de root.

Verificar o open_mode de todos os elementos da instância:

~~~sql
SQL> select name, open_mode from v$pdbs;

-- Output:
-- NAME                          OPEN_MODE
---------------------------   ----------
-- PDB$SEED                      READ ONLY
-- ORCLPDB1                      READ WRITE
-- AEBD                          MOUNTED
~~~

Como é possível observar a PDB ORDCLPDB1 está pronta a trabalhar. Isto acontece porque havia sido criado um trigger no momento da instalação para que isto acontecesse. Iremos de seguida verificar como é possível fazer esse trigger para a PDB AEBD.

**Abrir PDB**

~~~sql
SQL> alter pluggable database AEBD open;

-- Output:
-- Pluggable database altered.

-- Validar o novo estado após a alteração:
SQL> select name, open_mode from v$pdbs;

-- Output:
-- NAME                          OPEN_MODE
-- ---------------------------   ----------
-- PDB$SEED                      READ ONLY
-- ORCLPDB1                      READ WRITE
-- AEBD                          READ WRITE
~~~

**Abrir todas as PDB de uma só vez**

~~~sql
SQL> alter pluggable database all open;

-- Output:
-- Pluggable database altered.
~~~

Fechar PDB

~~~sql
SQL> alter pluggable database AEBD close immediate;

-- Output:
-- Pluggable database altered.

SQL> select name, open_mode from v$pdbs;

-- Output:
-- NAME                          OPEN_MODE
-- ---------------------------   ----------
-- PDB$SEED                      READ ONLY
-- ORCLPDB1                      READ WRITE
-- AEBD                          MOUNTED
~~~

Fechar todas as PDB de uma só vez:

~~~sql
SQL> alter pluggable database all close immediate;

-- Output:
-- Pluggable database altered.
~~~

**Criar trigger para arrancar todas as PDB quando a instância é inciada**

~~~sql
SQL> create or replace trigger Sys.After_Startup after startup on database
begin
   execute immediate 'alter pluggable database all open';
end After_Startup;
/

-- Output:
-- Trigger created.
~~~

Desligar a Base de Dados e Arrncar para verificar o estado das PDB

~~~sql
-- Desligar a base de dados
SQL> shutdown immediate

-- Arrancar a base de dados
SQL> startup

-- Validar estados das PDB
SQL> select name, open_mode from v$pdbs;

-- Output:
-- NAME                          OPEN_MODE
-- ---------------------------   ----------
-- PDB$SEED                      READ ONLY
-- ORCLPDB1                      READ WRITE
-- AEBD                          READ WRITE
~~~

**Alterar o nome de uma PDB**

Ligar à PDB e colocar em open restrict mode:

~~~sql
-- Fechar a base de dados
SQL> alter pluggable database aebd close immediate;

-- Abrir em modo restrito
SQL> alter pluggable database aebd open restricted;

-- Validar o estado
SQL> select name, restricted from v$pdbs;

-- Output:
-- NAME                          RES
-- ---------------------------   ----------
-- PDB$SEED                      NO
-- ORCLPDB1                      NO
-- AEBD                          YES
~~~

Para renomear uma PDB é necessário estar connectado à mesma:

~~~sql
SQL> alter pluggable database aebd rename global_name to aebd;

-- Output:
-- alter pluggable database aebd rename global_name to aebd
-- *
-- ERROR at line 1:
-- ORA-65046: operation not allowed from outside a pluggable database
~~~

~~~sql
-- Ligar à PDB
SQL> connect sys/Oradoc_db1@localhost:1521/aebd.localdomain as sysdba

-- Alterar o nome
SQL> alter pluggable database aebd rename global_name to aebd1;

-- Output:
-- Pluggable database altered.
~~~

Fechar a PDB e de seguida montar para voltar para produção:

~~~sql
-- Fechar a base de dados:
SQL> alter pluggable database close immediate;

-- Abrir a base de dados:
SQL> alter pluggable database open;

-- validar o novo estado
SQL> select name, open_mode from v$pdbs;
~~~

&nbsp;

* * * 

## 5. Gerir o espaço na CDB e nas PDB associadas

**Garantir que a ligação estaelecida é à CDB como SYSDBA**

~~~bash
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~
~~~sql
SQL> show con_name

-- Output:
-- CON_NAME
-- ------------------------------
-- CDB$ROOT
~~~

Verificar quais os tablespaces existentes na CDB

~~~sql
SQL> select tablespace_name, con_id from cdb_tablespaces where con_id=1;

-- Output:
-- TABLESPACE_NAME                    CON_ID
-- ------------------------------ ----------
-- SYSTEM                                  1
-- SYSAUX                                  1
-- UNDOTBS1                                1
-- TEMP                                    1
-- USERS                                   1
~~~

Verificar quais os datafiles existentes na base de dados CDB:

~~~sql
SQL> select file_name, con_id from cdb_data_files where con_id=1;

-- Output:
-- FILE_NAME                                               CON_ID
-- -------------------------------------------------       ---------
-- /u02/app/oracle/oradata/ORCL/users01.dbf                1
-- /u02/app/oracle/oradata/ORCL/undotbs01.dbf              1
-- /u02/app/oracle/oradata/ORCL/system01.dbf               1
-- /u02/app/oracle/oradata/ORCL/sysaux01.dbf               1
~~~

Verificar quais os ficheiros temporários existentes na CDB:

~~~sql
SQL> select file_name, con_id from cdb_temp_files where con_id=1;

-- Output:
-- FILE_NAME                                               CON_ID
-- -------------------------------------------------       ---------
-- /u02/app/oracle/oradata/ORCL/temp01.dbf                1
~~~

Criar um tablespace permanente na root:

~~~sql
SQL> create tablespace cdata datafile '/u02/app/oracle/oradata/ORCL/cdata01.dbf' SIZE 10M;

-- Output:
-- Tablespace criado.
~~~~

Verificar a criação do tablespace:

~~~sql
SQL> select tablespace_name, con_id from cdb_tablespaces order by con_id;

-- Output
-- TABLESPACE_NAME                CON_ID
-- ------------------------------ ----------
-- SYSTEM                         1
-- SYSAUX                         1
-- CDATA                          1
-- UNDOTBS1                       1
-- TEMP                           1
-- USERS                          1
-- SYSTEM                         3
-- SYSAUX                         3
-- UNDOTBS1                       3
-- TEMP                           3
-- AEBD_TEMP                      3

-- TABLESPACE_NAME                CON_ID
-- ------------------------------ ----------
-- HR_TABLES                      3
-- HR_TEMP                        3
-- AEBD_TABLES                    3
-- USERS                          3
-- SYSTEM                         5
-- TEMP                           5
-- UNDOTBS1                       5
-- SYSAUX                         5
~~~

Verificar a criação do datafile:

~~~sql
SQL> select file_name, con_id from cdb_data_files order by con_id;

-- Output:
-- FILE_NAME                                                       CON_ID
-- -------------------------------------------------               ---------
-- /u02/app/oracle/oradata/ORCL/users01.dbf                        1
-- /u02/app/oracle/oradata/ORCL/undotbs01.dbf                      1
-- /u02/app/oracle/oradata/ORCL/system01.dbf                       1
-- /u02/app/oracle/oradata/ORCL/sysaux01.dbf                       1
-- /u02/app/oracle/oradata/ORCL/cdata01.dbf                        1
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/system01.dbf           3
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/sysaux01.dbf           3
-- /u01/app/oracle/product/12.2.0/dbhome_1/dbs/AEBD_FILES_01.dbf   3
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/users01.dbf            3
-- /u01/app/oracle/product/12.2.0/dbhome_1/dbs/HR_FILES_01.dbf     3
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/undotbs01.dbf          3
-- /u02/app/oracle/oradata/ORCL/aebd/system01.dbf                  5
-- /u02/app/oracle/oradata/ORCL/aebd/undotbs01.dbf                 5
-- /u02/app/oracle/oradata/ORCL/aebd/sysaux01.dbf                  5
~~~


**Criar tablespace temporário na CDB:**

~~~sql
SQL> create temporary tablespace temp_root tempfile '/u02/app/oracle/oradata/ORCL/temproot01.dbf' SIZE 10M;

-- Output:
-- Tablespace created.
~~~

Verificar a criação do tablespace temporário:

~~~sql
SQL> select tablespace_name, con_id from cdb_tablespaces where contents='TEMPORARY' and con_id=1;

-- Output
-- TABLESPACE_NAME                CON_ID
-- ------------------------------ ---------
-- TEMP                           1
-- TEMP_ROOT                      1
~~~

Verificar a criação do tempfile:

~~~sql
SQL> select file_name, con_id from cdb_temp_files where con_id=1;

-- Output:
-- FILE_NAME                                                       CON_ID
-- -------------------------------------------------               ---------
-- /u02/app/oracle/oradata/ORCL/temp01.dbf                         1
-- /u02/app/oracle/oradata/ORCL/temproot01.dbf                     1
~~~


**Criar um tablespace numa PDB:**

~~~bash
#Garantir a Ligação à PDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
SQL> connect sys/Oradoc_db1@localhost:1521/orclpdb1.localdomain as sysdba
~~~
~~~sql
create tablespace pdata datafile '/u02/app/oracle/oradata/ORCL/pdata01.dbf' SIZE 10M;

-- Output:
-- Tablespace created.
~~~

Verificar a criação do tablespace e do datafile:

~~~sql
-- Verificar criação do tablespace:
SQL> select tablespace_name, con_id from cdb_tablespaces order by con_id;

-- Output:
-- TABLESPACE_NAME                    CON_ID
-- ------------------------------ ----------
-- SYSTEM                                  3
-- SYSAUX                                  3
-- UNDOTBS1                                3
-- TEMP                                    3
-- USERS                                   3
-- PDATA                                   3

-- Verificar criação do Datafile
SQL> select file_name, con_id from cdb_data_files order by con_id;

-- Output
-- FILE_NAME                                                    CON_ID
-----------------------------------------------------------     ------
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/system01.dbf        3
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/sysaux01.dbf        3
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/undotbs01.dbf       3
-- FILE_NAME                                                    CON_ID
-----------------------------------------------------------     ------
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/users01.dbf         3
-- /u02/app/oracle/oradata/ORCL/pdata01.dbf                     3
~~~


**Criar um tablespace temporário na PDB:**

~~~bash
#Garantir a Ligação à PDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~
~~~sql
SQL> connect sys/Oradoc_db1@localhost:1521/orclpdb1.localdomain as sysdba
~~~

Verificar a criação do tablespace temporário e do tempfile:
~~~sql
-- Criar tablespace temporário:
SQL> create temporary tablespace temp_pdb3 tempfile '/u02/app/oracle/oradata/ORCL/aebd/temppdb301.dbf' SIZE 10M;

-- Output:
-- Tablespace created.

-- Verificar a criação do tablespace temporario:
SQL> select tablespace_name, con_id from cdb_tablespaces where contents='TEMPORARY';

-- Output:
-- TABLESPACE_NAME                    CON_ID
-- ------------------------------ ----------
-- TEMP                                    3
-- TEMP_PDB3                               3


-- Verificar a criação do tempfile:
SQL>  select file_name from dba_temp_files;

-- Output:
-- FILE_NAME
-- --------------------------------------------------------------------------------
-- /u02/app/oracle/oradata/ORCL/aebd/temppdb301.dbf
-- /u02/app/oracle/oradata/ORCLCDB/orclpdb1/temp012017-03-02_07-54-38-075-AM.dbf

~~~

&nbsp;

* * * 

### 6. Gerir a segurança nas PDB

Cada container numa CDB possui utilizadores _local_ e _common_. Cada utilizador, apenas pode exercer os privilégios dentro do container ao qual está ligado.  
        >> **_COMMON_**: São criados na root e automaticamente são replicados para todas as PDB exceto a seed. Podem ligar-se a qualquer PDB. O nome associado a um _common_ user tem de começar por c##.  
        >> **_LOCAL_**: São criados apenas na PDB que serão utilizados. Estes utiliadores só conseguem ligar-se à PDB na qual foram criados e não são visiveis para as restantes PDB na mesma CDB. 

Criar user:
~~~bash
#Garantir a Ligação à CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~

~~~sql
SQL> create user c##1 identified by oracle container=all;

-- Output:
-- User created.
~~~

Verificar a criação do user:

~~~sql
SQL> select username, common, con_id from cdb_users where username like 'C##%';

-- Output:
-- USERNAME                COMMON    CON_ID
-- ----------------------- --------- ---------         
-- C##1                    YES       1
-- C##1                    YES       3
-- C##1                    YES       4
~~~

Ligar com o user criado a uma PDB:

~~~sql
SQL> connect c##1/oracle@localhost:1521/orclpdb1.localdomain

-- Output:
-- ERROR:
-- ORA-01045: user C##1 lacks CREATE SESSION privilege; logon denied
-- Warning: You are no longer connected to ORACLE.
~~~

Falta a criação dos privilégios necessários! Será abordado mais à frente.

**Criar utilizador _local_ numa PDB:**

Ligar à PDB:

~~~bash
#Garantir a Ligação à CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~
~~~sql
-- Ligar à PDB orclpdb1:
SQL> connect sys/Oradoc_db1@localhost:1521/orclpdb1.localdomain as sysdba

SQL> create user novouser identified by oracle;

-- Output:
-- User created.
~~~

Verificar a criação do user:

~~~sql
SQL> select username, common, con_id  from cdb_users where username ='NOVOUSER';

Output
USERNAME                       COMMON    CON_ID
------------------------------ --------- ---------         
NOVOUSER                       NO        3
~~~

**Tentar ligar às PDB existentes:**

~~~sql
SQL>  connect novouser/oracle@localhost:1521/aebd1.localdomain

-- Output:
-- ERROR:
-- ORA-01017: invalid username/password; logon denied
-- Warning: You are no longer connected to ORACLE.
~~~

O utilizador foi criado no container *orclpdb1.localdomain*, como tal não é possível efetuar o login noutra PDB. É como se o utilizador nem existisse.

~~~sql
SQL>  connect novouser/oracle@localhost:1521/orclpdb1.localdomain

-- Output:
-- ERROR:
-- ORA-01045: user NOVOUSER lacks CREATE SESSION privilege; logon denied
~~~

Temos novamente falha nos privilégios!

**Gerir Privilégios Grants & Roles**

Cada container numa CDB possui roles _local_ e _common_.  
        >> **_COMMON ROLES_**: São criados na root e automaticamente são replicados para todas as PDB exceto a seed. O nome associado a um _common_ user tem de começar por c##. Os grants pode ser dados commonly: Operação replicada por todas as PDB excepto a seed; locally: aplicadas apenas no container onde a operação é executada.  
        >> **_LOCAL_**: São criados apenas na PDB que serão utilizados. Estes roles são apenas usados na PDB na qual foram criados e não são visiveis para as restantes PDB na mesma CDB.  


Criar um _common role_

~~~bash
#Garantir a Ligação à CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~

~~~sql
SQL> create role c##r1 container=all;

-- Output:
-- Role created.
~~~

Verificar a criação do role:

~~~sql
SQL> select role, common, con_id from cdb_roles where role='C##R1';

-- Output:
-- ROLE                     COMMON    CON_ID
-- -----------------------  --------- ---------         
-- C##R1                    YES       1
-- C##R1                    YES       3
-- C##R1                    YES       4
~~~


**Criar _role_ numa PDB:**

Ligar à PDB:

~~~bash
#Garantir a Ligação à CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~
~~~sql
-- Ligar à PDB orclpd1.localdomain
SQL> connect sys/Oradoc_db1@localhost:1521/orclpdb1.localdomain as sysdba

SQL> create role hr_manager;

-- Output:
-- Role created.
~~~

Verificar a criação do role:

~~~sql
SQL> select role, common, con_id from cdb_roles where role='HR_MANAGER';

-- Output:
-- ROLE                     COMMON    CON_ID
-- -----------------------  --------- ---------         
-- HR_MANAGER                NO       3
-- ~~~

Tentar criar role global dentro da PDB:

~~~sql
SQL> create role c##r2 container=all;

-- Output:
-- ERROR at line 1:
-- ORA-65050: Common DDLs only allowed in root.
~~~

**Managing Common and Local Privileges**  

Podem ser atríbuidos grants _local_ e _common_ a _users_ ou _roles_. Os privilégios tomam a propriedade de _common_ ou _local_ conforme são atribuídos. São _common_ quando são executados com a clausula CONTAINER=ALL na root.

        >> **_COMMON PRIVILEGES_**: São atrbuidos automaticamente a todas as PDB excepto na seed.
        >> **_LOCAL PRIVILEGES_**: São atribuídos a um _user_ ou _role_ de uma PDB específica.


~~~bash
#Garantir a Ligação à CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~
~~~sql
SQL> grant create session to c##1 container=all;

-- Output:
-- Grant succeeded.

SQL> select grantee, privilege, common, con_id from cdb_sys_privs
where privilege='CREATE SESSION' and grantee='C##1';

-- Output:
-- GRANTEE                              PRIVILEGE       COM     CON_ID
--------------------------------------- ---------       ----    -------
-- C##1                                 CREATE SESSION  YES     1
-- C##1                                 CREATE SESSION  YES     3
-- C##1                                 CREATE SESSION  YES     4

-- Validar os privilegios do user criado na aebd:
SQL> connect c##1/oracle@localhost:1521/aebd1.localdomain

SQL> select * from session_privs;

-- Output:
-- PRIVILEGE
-- ----------------------------------------
-- CREATE SESSION
~~~

&nbsp;

* * *

### 7. Eliminar (drop) PDB
~~~bash
#Garantir a Ligação à CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~

Fechar todas as PDB:

~~~sql
SQL> alter pluggable database all close immediate;

-- Output:
-- Pluggable database altered.
~~~

Verificar que todas as PDB estão fechadas:

~~~sql
SQL> select name, open_mode from v$pdbs;

-- Output:
-- NAME                          OPEN_MODE
-- ---------------------------   ----------
-- PDB$SEED                      READ ONLY
-- ORCLPDB1                      MOUNTED
-- AEBD                          MOUNTED
~~~~

Apagar a PDB incluíndo os datafiles:

~~~sql
SQL> drop pluggable database aebd1 including datafiles;

-- Output:
-- Pluggable database dropped.
~~~

Confirmar que a PDB foi eliminada:

~~~sql
SQL> select name from v$pdbs;

-- Output:
-- NAME
-- --------------------------------------------------------------------------------
-- PDB$SEED
-- ORCLPDB1
~~~

* * *

## 8. Reverter todas as alterações##

Para reverter as alterações aqui executadas deverá:

~~~bash
#Garantir a Ligação à CDB:
[oracle@ddfbc6fee0b5 /]$ sqlplus sys/Oradoc_db1 as sysdba
~~~

Eliminar o utilizador e role _common_ criados:
~~~sql
SQL> drop user c##1;
SQL> drop role c##r1;
~~~

Eliminar os tablespaces criados na root da CDB:
~~~sql
SQL> drop tablespace cdata including contents;
SQL> drop tablespace temp_root including contents;
~~~

Abrir a orclpdb1 e substituir o trigger criado para apenas abir a orclpdb1 no arranque do CDB.
~~~sql
SQL> alter pluggable database orclpdb1 open;

SQL> create or replace trigger Sys.After_Startup after startup on database
        begin
                execute immediate 'alter pluggable database orclpdb1 open';
        end After_Startup;
/
~~~
