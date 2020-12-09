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

  - [Prerequisites](#prerequisites)
  - [How to deploy](#how-to-deploy)
  - [Check the Nebula Graph service status and ports](#check-the-nebula-graph-service-status-and-ports)
  - [Check the service data and logs](#check-the-service-data-and-logs)
  - [Stop the Nebula Graph Services](#stop-the-nebula-graph-services)
  - [Other Ways to Install Nebula Graph](#other-ways-to-install-nebula-graph)
  - [FAQ](#faq)
  - [What to Do Next](#what-to-do-next)

## Prerequisites

* You have installed [Docker](https://docs.docker.com/engine/install/), [Docker Compose](https://docs.docker.com/compose/install/), and [Git](https://git-scm.com/download/linux) on your host.

    >**NOTE**: 
    >* To use Docker as a non-root user, follow the steps in [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).
    >* We recommend that you install the latest version of these applications to make sure they work properly.

* You have started the Docker service on your host.

* If you have already deployed another version of Nebula Graph with Docker Compose on your host, to avoid compatibility issues，back up [the service data](#check-the-service-data-and-logs) if you need, and delete the `nebula-docker-compose/data` directory.

## How to deploy

1. Clone the `nebula-docker-compose` repository to your host with Git.

    * To install Nebula Graph 1.0, clone the `v1.0` branch.

    ```shell
    $ git clone --branch v1.0 https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

    * To install Nebula Graph 2.0, clone the `master` branch.

    ```shell
    $ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

2. Go to the `nebula-docker-compose` directory.

    ```shell
    $ cd nebula-docker-compose/
    ```

3. Run the following command to start all the Nebula Graph services.

    ```shell
    $ docker-compose up -d
    ```

    The following information indicates the services have started:

    ```shell
    Creating nebula-docker-compose_metad2_1 ... done
    Creating nebula-docker-compose_metad1_1 ... done
    Creating nebula-docker-compose_metad0_1 ... done
    Creating nebula-docker-compose_storaged2_1 ... done
    Creating nebula-docker-compose_graphd_1    ... done
    Creating nebula-docker-compose_storaged0_1 ... done
    Creating nebula-docker-compose_storaged1_1 ... done
    ```

    >**NOTE**: For more information of the preceding services, see [Design and Architecture of Nebula Graph](https://docs.nebula-graph.io/manual-EN/1.overview/3.design-and-architecture/1.design-and-architecture/).

4. Use nebula-console to connect to Nebula Graph.

    Nebula-console is the native CLI client of Nebula Graph. In this step, Docker pulls the nebula-console images automatically from Docker Hub according to the path we set in the following commands and uses it to connect to the graphd service of Nebula Graph. You can use other clients to connect to Nebula Graph instead of Nebula-console, such as [Nebula Graph Studio](https://github.com/vesoft-inc/nebula-web-docker) and [clients for different programming languages](https://docs.nebula-graph.io/manual-EN/1.overview/2.quick-start/3.supported-clients/).

   * For Nebula Graph 1.0:

    ```shell
    $ docker run --rm -ti --network=host vesoft/nebula-console:nightly -u <user> -p <password> --addr=127.0.0.1 --port=3699
    ```

   * For Nebula Graph 2.0 pre:

    ```shell
    $ docker run --rm -ti --network nebula-docker-compose_nebula-net vesoft/nebula-console:v2-preview-nightly -u <user> -p <password> --address=graphd --port=3699
    ```

    >**NOTE**: By default, the authentication is disabled, and the `-u` and `-p` options are unnecessary. To enbale authentication, see [Authentication Configurations](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/4.account-management-statements/authentication/#authentication).

    The following information indicates that you have connected to the Nebula Graph services:

    ```shell
    Welcome to Nebula Graph (Version 5d10861)

    (user@127.0.0.1) [(none)]>
    ```

## Check the Nebula Graph service status and ports

Running the following command to list the service information of Nebula Graph, such as state and ports.

```shell
$ docker-compose ps
```

The following information is displayed:

```shell
Name                     Command                       State                                                   Ports
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
nebula-docker-compose_graphd0_1     ./bin/nebula-graphd --flag ...   Up (health: starting)   0.0.0.0:33453->13000/tcp, 0.0.0.0:33449->13002/tcp, 0.0.0.0:3699->3699/tcp
nebula-docker-compose_graphd1_1     ./bin/nebula-graphd --flag ...   Up (health: starting)   0.0.0.0:33455->13000/tcp, 0.0.0.0:33450->13002/tcp, 0.0.0.0:3700->3699/tcp
nebula-docker-compose_graphd2_1     ./bin/nebula-graphd --flag ...   Up (health: starting)   0.0.0.0:33448->13000/tcp, 0.0.0.0:33447->13002/tcp, 0.0.0.0:3701->3699/tcp
nebula-docker-compose_metad0_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:33446->11000/tcp, 0.0.0.0:33444->11002/tcp, 0.0.0.0:45500->45500/tcp, 45501/tcp
nebula-docker-compose_metad1_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:33442->11000/tcp, 0.0.0.0:33441->11002/tcp, 0.0.0.0:45501->45500/tcp, 45501/tcp
nebula-docker-compose_metad2_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:33445->11000/tcp, 0.0.0.0:33443->11002/tcp, 0.0.0.0:45502->45500/tcp, 45501/tcp
nebula-docker-compose_storaged0_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:33457->12000/tcp, 0.0.0.0:33452->12002/tcp, 0.0.0.0:44500->44500/tcp, 44501/tcp
nebula-docker-compose_storaged1_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:33456->12000/tcp, 0.0.0.0:33451->12002/tcp, 0.0.0.0:44501->44500/tcp, 44501/tcp
nebula-docker-compose_storaged2_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:33458->12000/tcp, 0.0.0.0:33454->12002/tcp, 0.0.0.0:44502->44500/tcp, 44501/tcp
```

>**NOTE**: Nebula Graph provides services to the clients through port TCP3699 by default. You can adjust the port number by modifying the [network configurations](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/3.configurations/3.meta-config/#networking_configurations).

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
        |- graph0
        |- graph1
        `- graph2
```

## Stop the Nebula Graph Services

You can run the following command to stop the Nebula Graph services:

```shell
$ docker-compose down -v
```

The following information indicates you have successfully stopped the Nebula Graph services:

```shell
Stopping nebula-docker-compose_storaged0_1 ... done
Stopping nebula-docker-compose_graphd1_1   ... done
Stopping nebula-docker-compose_storaged2_1 ... done
Stopping nebula-docker-compose_graphd0_1   ... done
Stopping nebula-docker-compose_storaged1_1 ... done
Stopping nebula-docker-compose_graphd2_1   ... done
Stopping nebula-docker-compose_metad0_1    ... done
Stopping nebula-docker-compose_metad2_1    ... done
Stopping nebula-docker-compose_metad1_1    ... done
Removing nebula-docker-compose_storaged0_1 ... done
Removing nebula-docker-compose_graphd1_1   ... done
Removing nebula-docker-compose_storaged2_1 ... done
Removing nebula-docker-compose_graphd0_1   ... done
Removing nebula-docker-compose_storaged1_1 ... done
Removing nebula-docker-compose_graphd2_1   ... done
Removing nebula-docker-compose_metad0_1    ... done
Removing nebula-docker-compose_metad2_1    ... done
Removing nebula-docker-compose_metad1_1    ... done
Removing network nebula-docker-compose_nebula-net
```

## Other Ways to Install Nebula Graph

* [Using Source Code](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/1.build/1.build-source-code/)
* [Using Docker](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/1.build/2.build-by-docker/)
* [Using .rpm or .deb Files](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/2.install/1.install-with-rpm-deb/)

## FAQ

**Q**: How to update the nebula-console client?

**A**: To update the nebula-console client, use the `docker pull` command in the `nebula-docker-compose` directory on your host. For example, if you want to update nebula-console for the Nebula Graph 1.0 series, run the follow command.

```Shell
docker pull vesoft/nebula-console:nightly
```

If you want to update nebula-console for the Nebula Graph 2.0 pre-release, run the following command instead.

```Shell
docker pull vesoft/nebula-console:v2-preview-nightly
```

## What to Do Next 

You can start using Nebula Graph by creating spaces and inserting data. For more information, see [Quick Start](https://docs.nebula-graph.io/manual-EN/1.overview/2.quick-start/1.get-started/).
