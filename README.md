<p align="center">
  <img src="https://github.com/vesoft-inc/nebula/raw/master/docs/logo.png"/>
  <br> English | <a href="README_zh-CN.md">中文</a>
  <br>A distributed, scalable, lightning-fast graph database<br>
</p>
<p align="center">
  <a href="https://github.com/vesoft-inc/nebula-graph/actions?workflow=docker">
    <img src="https://github.com/vesoft-inc/nebula-graph/workflows/docker/badge.svg" alt="build docker image workflow"/>
  </a>
  <a href="http://githubbadges.com/star.svg?user=vesoft-inc&repo=nebula&style=default">
    <img src="http://githubbadges.com/star.svg?user=vesoft-inc&repo=nebula&style=default" alt="nebula star"/>
  </a>
  <a href="http://githubbadges.com/fork.svg?user=vesoft-inc&repo=nebula&style=default">
    <img src="http://githubbadges.com/fork.svg?user=vesoft-inc&repo=nebula&style=default" alt="nebula fork"/>
  </a>
  <br>
</p>

The `v2.0.0` branch stores the Docker Compose deployment solution for Nebula Graph v2.0.0.

# Deploy Nebula Graph with Docker Compose

There are multiple ways to deploy Nebula Graph, but using Docker Compose is usually considered to be a fast starter.

## Reading guide

If you are reading this topic with the questions listed below, click them to jump to their answers.

* [What do I need to do before deploying Nebula Graph?](#prerequisites)
* [How to fast deploy Nebula Graph with Docker Compose?](#how-to-deploy)
* [How to check the status and ports of the Nebula Graph services?](#check-the-nebula-graph-service-status-and-port)
* [How to check the data and logs of the Nebula Graph services?](#check-the-service-data-and-logs)
* [How to stop the Nebula Graph services?](#stop-the-nebula-graph-services)
* [What are the other ways to install Nebula Graph?](#other-ways-to-install-nebula-graph)

## Prerequisites

* You have installed the following applications on your host.

  | Application    | Recommended version | Official installation reference                                    |
  | -------------- | ------------------- | ------------------------------------------------------------------ |
  | Docker         | Latest              | [Install Docker Engine](https://docs.docker.com/engine/install/)   |
  | Docker Compose | Latest              | [Install Docker Compose](https://docs.docker.com/compose/install/) |
  | Git            | Latest              | [Download Git](https://git-scm.com/download/)       |

* If you are deploying Nebula Graph as a non-root user, grant the user with Docker-related privileges. For a detailed instruction, see [Docker document: Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

* You have started the Docker service on your host.

* If you have already deployed another version of Nebula Graph with Docker Compose on your host, to avoid compatibility issues，back up [the service data](#check-the-service-data-and-logs) if you need, and delete the `nebula-docker-compose/data` directory.

## How to deploy

1. Clone the `v2.0.0` branch of the `nebula-docker-compose` repository to your host with Git.

    ```bash
    $ git clone --branch v2.0.0 https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

2. Go to the `nebula-docker-compose` directory.

    ```bash
    $ cd nebula-docker-compose/
    ```

3. Run the following command to start all the Nebula Graph services.

    >**NOTE:** Update the [Nebula Graph images](#how-to-upgrade-nebula-graph-services) and [Nebula Console images](#how-to-update-the-nebula-console-client) first if they are out of date.

    ```bash
    nebula-docker-compose]$ docker-compose up -d
    Creating nebula-docker-compose_metad0_1 ... done
    Creating nebula-docker-compose_metad2_1 ... done
    Creating nebula-docker-compose_metad1_1 ... done
    Creating nebula-docker-compose_graphd2_1   ... done
    Creating nebula-docker-compose_graphd_1    ... done
    Creating nebula-docker-compose_graphd1_1   ... done
    Creating nebula-docker-compose_storaged0_1 ... done
    Creating nebula-docker-compose_storaged2_1 ... done
    Creating nebula-docker-compose_storaged1_1 ... done
    ```

    >**NOTE**: For more information of the preceding services, see [Nebula Graph architecture](../1.introduction/3.nebula-graph-architecture/1.architecture-overview.md).

4. Connect to Nebula Graph.

    1. Run the following command to start a new docker container with the Nebula Console image, and connect the container to the network where Nebula Graph is deployed.

    ```bash
    $ docker run --rm -ti --network nebula-docker-compose_nebula-net --entrypoint=/bin/sh vesoft/nebula-console:v2.0.0-ga
    ```

    > **Note**: Your local network (nebula-docker-compose_nebula-net) may be different from the example above. Use the following command to list the actual local network.

    ```bash
    $ docker network  ls
    NETWORK ID          NAME                               DRIVER              SCOPE
    a74c312b1d16        bridge                             bridge              local
    dbfa82505f0e        host                               host                local
    ed55ccf356ae        nebula-docker-compose_nebula-net   bridge              local
    93ba48b4b288        none                               null                local

    ```

    2. Connect to Nebula Graph with Nebula Console.

    ```bash
    docker> nebula-console -u user -p password --address=graphd --port=9669
    ```

    > **Note**: By default, the authentication is off, you can log in with any user name and password. To turn it on, see [Enable authentication](https://docs.nebula-graph.io/2.0/7.data-security/1.authentication/1.authentication/).

    3. Run the `SHOW HOSTS` statement to check the status of the `nebula-storaged` processes.

    ```bash
    nebula> SHOW HOSTS;
    +-------------+------+----------+--------------+----------------------+------------------------+
    | Host        | Port | Status   | Leader count | Leader distribution  | Partition distribution |
    +-------------+------+----------+--------------+----------------------+------------------------+
    | "storaged0" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
    +-------------+------+----------+--------------+----------------------+------------------------+
    | "storaged1" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
    +-------------+------+----------+--------------+----------------------+------------------------+
    | "storaged2" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
    +-------------+------+----------+--------------+----------------------+------------------------+
    | "Total"     |      |          | 0            |                      |                        |
    +-------------+------+----------+--------------+----------------------+------------------------+
    ```

5. Run `exit` twice to switch back to your terminal (shell). You can run Step 4 to login Nebula Graph again.

## Check the Nebula Graph service status and port

Run `docker-compose ps` to list all the services of Nebula Graph and their status and ports.

```bash
$ docker-compose ps
nebula-docker-compose_graphd1_1     /usr/local/nebula/bin/nebu ...   Up (healthy)   0.0.0.0:33170->19669/tcp, 0.0.0.0:33169->19670/tcp, 0.0.0.0:33173->9669/tcp
nebula-docker-compose_graphd2_1     /usr/local/nebula/bin/nebu ...   Up (healthy)   0.0.0.0:33174->19669/tcp, 0.0.0.0:33171->19670/tcp, 0.0.0.0:33176->9669/tcp
nebula-docker-compose_graphd_1      /usr/local/nebula/bin/nebu ...   Up (healthy)   0.0.0.0:33205->19669/tcp, 0.0.0.0:33204->19670/tcp, 0.0.0.0:9669->9669/tcp
nebula-docker-compose_metad0_1      ./bin/nebula-metad --flagf ...   Up (healthy)   0.0.0.0:33165->19559/tcp, 0.0.0.0:33162->19560/tcp, 0.0.0.0:33167->9559/tcp,
                                                                                    9560/tcp
nebula-docker-compose_metad1_1      ./bin/nebula-metad --flagf ...   Up (healthy)   0.0.0.0:33166->19559/tcp, 0.0.0.0:33163->19560/tcp, 0.0.0.0:33168->9559/tcp,
                                                                                    9560/tcp
nebula-docker-compose_metad2_1      ./bin/nebula-metad --flagf ...   Up (healthy)   0.0.0.0:33161->19559/tcp, 0.0.0.0:33160->19560/tcp, 0.0.0.0:33164->9559/tcp,
                                                                                    9560/tcp
nebula-docker-compose_storaged0_1   ./bin/nebula-storaged --fl ...   Up (healthy)   0.0.0.0:33180->19779/tcp, 0.0.0.0:33178->19780/tcp, 9777/tcp, 9778/tcp,
                                                                                    0.0.0.0:33183->9779/tcp, 9780/tcp
nebula-docker-compose_storaged1_1   ./bin/nebula-storaged --fl ...   Up (healthy)   0.0.0.0:33175->19779/tcp, 0.0.0.0:33172->19780/tcp, 9777/tcp, 9778/tcp,
                                                                                    0.0.0.0:33177->9779/tcp, 9780/tcp
nebula-docker-compose_storaged2_1   ./bin/nebula-storaged --fl ...   Up (healthy)   0.0.0.0:33184->19779/tcp, 0.0.0.0:33181->19780/tcp, 9777/tcp, 9778/tcp,
                                                                                    0.0.0.0:33185->9779/tcp, 9780/tcp
```

Nebula Graph provides services to the clients through port `9669` by default. To use other ports, modify the `docker-compose.yaml` file in the `nebula-docker-compose` directory and restart the Nebula Graph services.

## Check the service data and logs

All the data and logs of Nebula Graph are stored persistently in the `nebula-docker-compose/data` and `nebula-docker-compose/logs` directories.

The structure of the directories is as follows:

```text
nebula-docker-compose/
  |-- docker-compose.yaml
  ├── data
  │   ├── meta0
  │   ├── meta1
  │   ├── meta2
  │   ├── storage0
  │   ├── storage1
  │   └── storage2
  └── logs
      ├── graph
      ├── graph1
      ├── graph2
      ├── meta0
      ├── meta1
      ├── meta2
      ├── storage0
      ├── storage1
      └── storage2
```

## Stop the Nebula Graph services

You can run the following command to stop the Nebula Graph services:

```bash
$ docker-compose down
```

The following information indicates you have successfully stopped the Nebula Graph services:

```bash
Stopping nebula-docker-compose_storaged0_1 ... done
Stopping nebula-docker-compose_graphd1_1   ... done
Stopping nebula-docker-compose_graphd_1    ... done
Stopping nebula-docker-compose_storaged1_1 ... done
Stopping nebula-docker-compose_graphd2_1   ... done
Stopping nebula-docker-compose_storaged2_1 ... done
Stopping nebula-docker-compose_metad0_1    ... done
Stopping nebula-docker-compose_metad2_1    ... done
Stopping nebula-docker-compose_metad1_1    ... done
Removing nebula-docker-compose_storaged0_1 ... done
Removing nebula-docker-compose_graphd1_1   ... done
Removing nebula-docker-compose_graphd_1    ... done
Removing nebula-docker-compose_storaged1_1 ... done
Removing nebula-docker-compose_graphd2_1   ... done
Removing nebula-docker-compose_storaged2_1 ... done
Removing nebula-docker-compose_metad0_1    ... done
Removing nebula-docker-compose_metad2_1    ... done
Removing nebula-docker-compose_metad1_1    ... done
Removing network nebula-docker-compose_nebula-net
```

> **Note**: Command `docker-compose down -v` will **delete** all your local Nebula Graph storage data. Try this command if you're using a developing/nightly version and having some compatibility issues.

## FAQ

### How to update the docker images of Nebula Graph services

To update the images of the Graph Service, Storage Service, and Meta Service, run `docker-compose pull` in the `nebula-docker-compose` directory.

### Why it shows `ERROR: toomanyrequests` when running `docker-compose pull`

You may meet the following error.

`ERROR: toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit`.

You have met the rate limit of Docker Hub. Learn more on [Understanding Docker Hub Rate Limiting](https://www.docker.com/increase-rate-limit).

### How to update the Nebula Console client

To update the Nebula Console client, run the following command.

```bash
docker pull vesoft/nebula-console:v2.0.0-ga
```

### How to upgrade the Nebula Graph services deployed with Docker Compose

To upgrade Nebula Graph, update the Nebula Graph docker images and restart the services.

1. In the `nebula-docker-compose` directory, run `docker-compose pull` to update the Nebula Graph docker images.

<!--
  > **CAUTION:** Make sure that you have backed up all important data before following the next step to stop the Nebula Graph services.
-->

2. Run `docker-compose down` to stop the Nebula Graph services.

3. Run `docker-compose up -d` to start the Nebula Graph services again.

### Why can't I access the data after updating the nebula-docker-compose repository? (Jan 4, 2021)

If you updated the nebula-docker-compose repository after Jan 4, 2021 and there are pre-existing data, modify the `docker-compose.yaml` file and change the port numbers to [the previous ones](https://github.com/vesoft-inc/nebula-docker-compose/commit/2a612f1c4f0e2c31515e971b24b355b3be69420a) before connecting to Nebula Graph.

### Why can't I access the data after updating the nebula-docker-compose repository? (Jan 27, 2021)

The data format is incompatible before and after in Jan 27, 2021. Run `docker-compose down -v` to delete all your local data.

### Where are the data stored when Nebula Graph is deployed with Docker Compose

If deployed with Docker Compose, Nebula Graph stores all data in `nebula-docker-compose/data/`.
