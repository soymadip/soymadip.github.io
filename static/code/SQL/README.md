# SQL

We will be using MySQL...

## DB Setup

Instead of installing locally, we will be using Conntainers to setup MySQL.

1. Install Podman (recommended) or Docker
0. If installed Docker, Start docker daemon service.
0. In the Terminal enter: `./start-db`


### Access

- Access mariadb/mysql at `localhost:3306`
- Access phpmyadmin at `localhost:8080`


## IDE Setup

Instead of zed, I suggest using VsCode or any derivative IDE.

1. Install DBCode extension.
0. From sidebar click on dbcode icon and  click on add conection.
0. Select MariaDB,
   - give connection name like `LearnDB`,
   - host: `localhost`
   - username: `root`
   - password: `my-secret-pw`
   - select a database.
