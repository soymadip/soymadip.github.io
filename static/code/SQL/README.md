# SQL

We will be using MySQL.

## DB Setup

Instead of installing it locally, we will use containers to set up MySQL.

1. Install Podman (recommended) or Docker
2. If Docker is installed, start the Docker daemon.
3. In the terminal, run `./start-db`, or `./start-db -d` to run in the background.
4. To stop all project containers, run: `./start-db down`

- Access at [`localhost:3306`](http://localhost:3306)
- Default Database name: `practice-db`


## DB GUI Setup

1. Head to [`localhost:4224`](http://localhost:4224).
2. Select the `New Connection` option in the center or top-left.
3. Select `MySQL` and click Next.
4. Enter these details:
    - Connection name: `PracticeDB`
    - Host: `mysql`
    - Port: `3306`
    - User: `root`
    - Password: `my-secret-pw`


## IDE Setup

I recommend to use DBX (Above DB GUI). If urgently needed, use VS Code or any derivative IDE.

1. Install DBCode extension.
2. From the sidebar, click the DBCode icon and select **Add Connection**.
3. Select `MySQL`:
    - Host: `localhost`
    - Connection Name, Port, Username, Passowrd see from above.
