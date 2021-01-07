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

# Deploy Nebula Graph with Docker Compose

Using Docker Compose is a convenient way to deploy and manage Nebula Graph.

* [Prerequisites](#prerequisites)
* [How to deploy](#how-to-deploy)
* [Check the Nebula Graph service status and ports](#check-the-nebula-graph-service-status-and-ports)
* [Check the service data and logs](#check-the-service-data-and-logs)
* [Stop the Nebula Graph Services](#stop-the-nebula-graph-services)
* [Other Ways to Install Nebula Graph](#other-ways-to-install-nebula-graph)
* [FAQ](#faq)
* [What to Do Next](#what-to-do-next)

## Prerequisites

* You have installed [Docker](https://docs.docker.com/engine/install/), [Docker Compose](https://docs.docker.com/compose/install/), and [Git](https://git-scm.com/download/linux) on your host.

    >**NOTE**:
    >
    >* To use Docker as a non-root user, follow the steps in [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).
    >* We recommend that you install the latest version of these applications to make sure they work properly.

* You have started the Docker service on your host.

* If you have already deployed another version of Nebula Graph with Docker Compose on your host, to avoid compatibility issues，back up [the service data](#check-the-service-data-and-logs) if you need, and delete the `nebula-docker-compose/data` directory.

## How to deploy

1. Clone the `nebula-docker-compose` repository to your host with Git.

    * To install Nebula Graph 1.0, clone the `v1.0` branch.

    ```bash
    $ git clone --branch v1.0 https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

    * To install Nebula Graph 2.0, clone the `master` branch.

    ```bash
    $ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

2. Go to the `nebula-docker-compose` directory.

    ```bash
    $ cd nebula-docker-compose/
    ```

3. Run the following command to start all the Nebula Graph services.

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

    >**NOTE**: For more information of the preceding services, see [Design and Architecture of Nebula Graph](https://docs.nebula-graph.io/manual-EN/1.overview/3.design-and-architecture/1.design-and-architecture/).

4. Use nebula-console to connect to Nebula Graph.

    Nebula-console is the native CLI client of Nebula Graph. In this step, Docker pulls the nebula-console images automatically from Docker Hub according to the path we set in the following commands and uses it to connect to the graphd service of Nebula Graph. You can use other clients to connect to Nebula Graph instead of Nebula-console, such as [Nebula Graph Studio](https://github.com/vesoft-inc/nebula-web-docker) and [clients for different programming languages](https://docs.nebula-graph.io/manual-EN/1.overview/2.quick-start/3.supported-clients/).

   * For Nebula Graph 1.0:

    ```bash
    $ docker run --rm -ti --network=host vesoft/nebula-console:nightly -u <user> -p <password> --addr=127.0.0.1 --port=3699
    ```

   * For Nebula Graph 2.0:

    ```bash
    $ docker run --rm -ti --network nebula-docker-compose_nebula-net --entrypoint=/bin/sh vesoft/nebula-console:v2-nightly
    docker> nebula-console -u <user> -p <password> --address=graphd --port=9669
    ```

    >**NOTE**: By default, the authentication is disabled, and the `-u` and `-p` options are unnecessary. To enbale authentication, see [Authentication Configurations](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/4.account-management-statements/authentication/#authentication).

    The following information indicates that you have connected to the Nebula Graph services:

    ```bash
    Welcome to Nebula Graph (Version 5d10861)

    (user@127.0.0.1) [(none)]>
    ```

## Check the Nebula Graph service status and ports

Run `docker-compose ps` to list all the services of Nebula Graph and their status and ports.

```bash
$ docker-compose ps
Name                     Command                       State                                                   Ports
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
nebula-docker-compose_graphd1_1     ./bin/nebula-graphd --flag ...   Up (health: starting)   13000/tcp, 13002/tcp, 0.0.0.0:33295->19669/tcp, 0.0.0.0:33291->19670/tcp,
                                                                                             3699/tcp, 0.0.0.0:33298->9669/tcp
nebula-docker-compose_graphd2_1     ./bin/nebula-graphd --flag ...   Up (health: starting)   13000/tcp, 13002/tcp, 0.0.0.0:33285->19669/tcp, 0.0.0.0:33284->19670/tcp,
                                                                                             3699/tcp, 0.0.0.0:33286->9669/tcp
nebula-docker-compose_graphd_1      ./bin/nebula-graphd --flag ...   Up (health: starting)   13000/tcp, 13002/tcp, 0.0.0.0:33288->19669/tcp, 0.0.0.0:33287->19670/tcp,
                                                                                             3699/tcp, 0.0.0.0:9669->9669/tcp
nebula-docker-compose_metad0_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   11000/tcp, 11002/tcp, 0.0.0.0:33276->19559/tcp, 0.0.0.0:33275->19560/tcp,
                                                                                             45500/tcp, 45501/tcp, 0.0.0.0:33278->9559/tcp
nebula-docker-compose_metad1_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   11000/tcp, 11002/tcp, 0.0.0.0:33279->19559/tcp, 0.0.0.0:33277->19560/tcp,
                                                                                             45500/tcp, 45501/tcp, 0.0.0.0:33281->9559/tcp
nebula-docker-compose_metad2_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   11000/tcp, 11002/tcp, 0.0.0.0:33282->19559/tcp, 0.0.0.0:33280->19560/tcp,
                                                                                             45500/tcp, 45501/tcp, 0.0.0.0:33283->9559/tcp
nebula-docker-compose_storaged0_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   12000/tcp, 12002/tcp, 0.0.0.0:33290->19779/tcp, 0.0.0.0:33289->19780/tcp,
                                                                                             44500/tcp, 44501/tcp, 0.0.0.0:33294->9779/tcp
nebula-docker-compose_storaged1_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   12000/tcp, 12002/tcp, 0.0.0.0:33296->19779/tcp, 0.0.0.0:33292->19780/tcp,
                                                                                             44500/tcp, 44501/tcp, 0.0.0.0:33299->9779/tcp
nebula-docker-compose_storaged2_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   12000/tcp, 12002/tcp, 0.0.0.0:33297->19779/tcp, 0.0.0.0:33293->19780/tcp,
                                                                                             44500/tcp, 44501/tcp, 0.0.0.0:33300->9779/tcp
```

>**NOTE**: The Nebula Graph services listen on port `3699` for v1.x and `9669` for v2.x by default. To use other ports, modify the `docker-compose.yaml` file in the `nebula-docker-compose` directory.

## Check the service data and logs

All data and logs of Nebula Graph are stored persistently in the `nebula-docker-compose/data` and `nebula-docker-compose/logs` directories.

The structure of the directories is as follows:

```text
nebula-docker-compose/
  |-- docker-compose.yaml
  |-- data
  |     |- meta0
  |     |- meta1
  |     |- meta2
  |     |- storage0
  |     |- storage1
  |     `- storage2
  `-- logs
        |- meta0
        |- meta1
        |- meta2
        |- storage0
        |- storage1
        |- storage2
        `- graph
```

## Stop the Nebula Graph Services

You can run the following command to stop the Nebula Graph services:

```bash
$ docker-compose down -v
```

The following information indicates you have successfully stopped the Nebula Graph services:

```bash
Stopping nebula-docker-compose_storaged1_1 ... done
Stopping nebula-docker-compose_storaged0_1 ... done
Stopping nebula-docker-compose_graphd_1    ... done
Stopping nebula-docker-compose_storaged2_1 ... done
Stopping nebula-docker-compose_metad0_1    ... done
Stopping nebula-docker-compose_metad1_1    ... done
Stopping nebula-docker-compose_metad2_1    ... done
Removing nebula-docker-compose_storaged1_1 ... done
Removing nebula-docker-compose_storaged0_1 ... done
Removing nebula-docker-compose_graphd_1    ... done
Removing nebula-docker-compose_storaged2_1 ... done
Removing nebula-docker-compose_metad0_1    ... done
Removing nebula-docker-compose_metad1_1    ... done
Removing nebula-docker-compose_metad2_1    ... done
Removing network nebula-docker-compose_nebula-net
```

## Other Ways to Install Nebula Graph

* [Using Source Code](https://docs.nebula-graph.io/2.0/4.deployment-and-installation/2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code/)
* [Using Docker](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/1.build/2.build-by-docker/)
* [Using .rpm or .deb Files](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/2.install/1.install-with-rpm-deb/)

## FAQ

### How to update the nebula-console client?

To update the nebula-console client, use the `docker pull` command in the `nebula-docker-compose` directory on your host. For example, if you want to update nebula-console for the Nebula Graph 1.0 series, run the follow command.

```bash
docker pull vesoft/nebula-console:nightly
```

If you want to update nebula-console for the Nebula Graph v2.0, run the following command instead.

```bash
docker pull vesoft/nebula-console:v2-nightly
```

### How to upgrade Nebula Graph?

To upgrade Nebula Graph, update the Nebula Graph docker images and restart the services.

1. In the `nebula-docker-compose` directory, run `docker compose pull` to update the Nebula Graph docker images.

  > **CAUTION:** Make sure you have backed up all important data before following the next step to stop the Nebula Graph services.

2. Run `docker-compose down` to stop the Nebula Graph services.

3. Run `docker-compose up -d` to start the Nebula Graph services again.

### Why can't I connect to Nebula Graph through port 3699 after updating the nebula-docker-compose repository?

On the release of Nebula Graph 2.0.0-RC, the default port for connection changed from 3699 to 9669. To connect to Nebula Graph after updating the repository, use port 9669 or modify the port number in the `docker-compose.yaml` file.

### Why can't I access the data after updating the nebula-docker-compose repository?

If you updated the nebula-docker-compose repository after Jan 4, 2021 and there are pre-existing data, modify the `docker-compose.yaml` file and change the port numbers to [the previous ones](https://github.com/vesoft-inc/nebula-docker-compose/commit/2a612f1c4f0e2c31515e971b24b355b3be69420a) before connecting to Nebula Graph.

## What to Do Next

You can start using Nebula Graph by creating spaces and inserting data. For more information, see [Quick Start](https://docs.nebula-graph.io/manual-EN/1.overview/2.quick-start/1.get-started/).
