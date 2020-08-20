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

Using Docker Compose is a convenient way to deploy **Nebula Graph** services. This topic guides you through the deployment and shows you how to [check the **Nebula Graph** service status](#check-the-nebula-graph-service-status-and-ports), [data and logs](#check-the-service-data-and-logs), and how to [stop the **Nebula Graph** services](#stop-the-nebula-graph-services).

## Prerequisites

* You have installed [Docker](https://docs.docker.com/engine/install/), [Docker Compose](https://docs.docker.com/compose/install/) and [Git](https://git-scm.com/download/linux) on your host.

    >**Note**: 
    * To use Docker as a non-root user, follow the steps in [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).
    * It is recommended to install the latest version of these applications to make sure they work properly.

* You have started the Docker service on your host.

## How to Deploy

1. Clone the `nebula-docker-compose` repository to your host with Git.

    * To install **Nebula Graph** 1.0, clone the `master` branch with the following code.

    ```shell
    $ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

    * To install **Nebula Graph** 2.0-pre, clone the `v2-preview` branch with the following code.

    ```shell
    $ git clone --branch v2-preview https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

2. Go to the `nebula-docker-compose` directory.

    ```shell
    $ cd nebula-docker-compose/
    ```

    >**NOTICE**: If you have already deployed another version of **Nebula Graph** with Docker Compose on your host, to avoid compatibility issues，backup [the service data](#check-the-service-data-and-logs) if you need, and delete the `nebula-docker-compose/data` directory before you move on to the next step.

3. Use the following command to start all **Nebula Graph** services.

    ```shell
    $ docker-compose up -d
    ```

    The following information is displayed when the services have started:

    ```shell
    Creating nebula-docker-compose_metad2_1 ... done
    Creating nebula-docker-compose_metad1_1 ... done
    Creating nebula-docker-compose_metad0_1 ... done
    Creating nebula-docker-compose_storaged2_1 ... done
    Creating nebula-docker-compose_graphd_1    ... done
    Creating nebula-docker-compose_storaged0_1 ... done
    Creating nebula-docker-compose_storaged1_1 ... done
    ```

    >**NOTE**: For more information of above services, see [Design and Architecture of Nebula Graph](https://docs.nebula-graph.io/manual-EN/1.overview/3.design-and-architecture/1.design-and-architecture/).

4. Use nebula-console to connect to **Nebula Graph**.

    Nebula-console is the native CLI client of **Nebula Graph**. Docker pulls the nebula-console images automatically from Docker Hub according to the path we set in the following commands, and uses it to connect to the graphd service of **Nebula Graph**.

   * For **Nebula Graph** 1.0:

    ```shell
    $ docker run --rm -ti --network=host vesoft/nebula-console:nightly -u <user> -p <password> --addr=127.0.0.1 --port=3699
    ```

   * For **Nebula Graph** 2.0 pre:

    ```shell
    $ docker run --rm -ti --network nebula-docker-compose_nebula-net vesoft/nebula-console:v2-preview-nightly -u <user> -p <password> --address=graphd --port=3699
    ```

    >**NOTE**: By default, the authentication is disabled, and the `-u` and `-p` options are unnecessary. To enbale authentication, see [Authentication Configurations](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/4.account-management-statements/authentication/#authentication).

    The following information is displayed when you have connected to the **Nebula Graph** services:

    ```shell
    Welcome to Nebula Graph (Version 5d10861)

    (user@127.0.0.1) [(none)]>
    ```

## Check the **Nebula Graph** Service Status and Ports

You can list the service information of **Nebula Graph**, such as state and ports, with the following command:

```shell
$ docker-compose ps
```

The following information is displayed:

```shell
Name                     Command                       State                                                   Ports
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
nebula-docker-compose_graphd_1      ./bin/nebula-graphd --flag ...   Up (health: starting)   0.0.0.0:32867->13000/tcp, 0.0.0.0:32866->13002/tcp, 3369/tcp, 0.0.0.0:3699->3699/tcp
nebula-docker-compose_metad0_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:32865->11000/tcp, 0.0.0.0:32864->11002/tcp, 45500/tcp, 45501/tcp
nebula-docker-compose_metad1_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:32863->11000/tcp, 0.0.0.0:32862->11002/tcp, 45500/tcp, 45501/tcp
nebula-docker-compose_metad2_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:32861->11000/tcp, 0.0.0.0:32860->11002/tcp, 45500/tcp, 45501/tcp
nebula-docker-compose_storaged0_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:32879->12000/tcp, 0.0.0.0:32877->12002/tcp, 44500/tcp, 44501/tcp
nebula-docker-compose_storaged1_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:32876->12000/tcp, 0.0.0.0:32872->12002/tcp, 44500/tcp, 44501/tcp
nebula-docker-compose_storaged2_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:32873->12000/tcp, 0.0.0.0:32870->12002/tcp, 44500/tcp, 44501/tcp
```

**Note**: **Nebula Graph** provides services to the clients through port TCP 3699 by default. You can adjust the port number by modifying its [network configurations](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/3.configurations/4.graph-config/#networking_configurations).

## Check the Service Data and Logs

All data and logs of **Nebula Graph** are stored persistently in the `nebula-docker-compose/data` and `nebula-docker-compose/logs` directories.

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

## Stop the **Nebula Graph** Services

You can stop the **Nebula Graph** services with the following command:

```shell
$ docker-compose down -v
```

The following information indicates you have successfully stopped the **Nebula Graph** services:

```shell
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

* [Using Source Code](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/1.build/1.build-source-code/)
* [Using Docker](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/1.build/2.build-by-docker/)
* [Using .rpm or .deb Files](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/2.install/1.install-with-rpm-deb/)

## FAQ

**Q**: How to update the nebula-console client?

**A**: Use the `docker-compose pull` command in the `nebula-docker-compose` directory on your host.

## What to Do Next 

You can start using **Nebula Graph** by creating spaces and inserting data. For more information, see [Quick Start](https://docs.nebula-graph.io/manual-EN/1.overview/2.quick-start/1.get-started/).