<div align="center">
  <h1>Nebula Graph Docker Deployment</h1>
  <div>
    <a href="https://github.com/vesoft-inc/nebula-docker-compose/blob/master/README_zh-CN.md">中文</a>
  </div>
  <br>
</div>

# Overview

In this document, we will walk you through the process of deploying a **Nebula Graph** cluster with [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/). We will also show you how to [check the services status of **Nebula Graph**](#checking-the-status-and-ports-of-nebula-graph-services), how to [check the cluster data and logs](#checking-the-cluster-data-and-logs), and how to [stop the services of **Nebula Graph**](#stopping-the-services-of-nebula-graph).

# Prerequisites

Before you start deploying the **Nebula Graph** cluster, ensure that you have installed the latest version of [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/). 

**Note**: If you do not have the `root` privilege for [Docker](https://docs.docker.com/install/), you can refer to [how to set root privileges for Docker](https://docs.docker.com/install/linux/linux-postinstall/).

# Services of **Nebula Graph** to Be Deployed

In this guide, we are going to deploy the following services of **Nebula Graph**:

* 3 replicas of `nebula-metad` service
* 3 replicas of `nebula-storage`d service
* 1 replica of `nebula-graphd` service

# Deploying the **Nebula Graph** Cluster

You can deploy the **Nebula Graph** cluster by the following steps:

1. Clone the `nebula-docker-compose` repository to your local computer.

```shell
$ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
```

2. Change your current directory to the `nebula-docker-compose` directory.

```shell
$ cd nebula-docker-compose/
```

3. Start all the services of **Nebula Graph**.

```shell
$ docker-compose up -d
```

The following information which indicates the services are started is displayed:

```shell
Creating nebula-docker-compose_metad2_1 ... done
Creating nebula-docker-compose_metad1_1 ... done
Creating nebula-docker-compose_metad0_1 ... done
Creating nebula-docker-compose_storaged2_1 ... done
Creating nebula-docker-compose_graphd_1    ... done
Creating nebula-docker-compose_storaged0_1 ... done
Creating nebula-docker-compose_storaged1_1 ... done
```

4. Pull the `vesoft/nebula-console:nightly` image to your local computer.

```shell
$ docker pull vesoft/nebula-console:nightly
```

**Note**:

a. We will use the `nebula-console` docker container to connect to the graph service of **Nebula Graph**.

b. If you have pulled the `vesoft/nebula-console` image before, remove it with the following command before you pull it again:

   * `docker rm $(docker ps -qa -f status=exited) # cleanup exited containers`
   * `docker rmi vesoft/nebula-console:nightly`
   
c. If you have pulled the **Nebula Graph** images before, you can update the images with the following command:

```shell
$ docker-compose pull
```

5. Connect to the graph service of **Nebula Graph**.

```shell
$ docker run --rm -ti --network=host vesoft/nebula-console:nightly --addr=127.0.0.1 --port=3699
```

The following information which indicates that you successfully connect to **Nebula Graph** is displayed:

```shell
Welcome to Nebula Graph (Version 5d10861)

(user@127.0.0.1) [(none)]>

```

**Note**: Now, you can start using **Nebula Graph** by creating spaces, tags and more. For details, refer to [get started](https://github.com/vesoft-inc/nebula/blob/master/docs/manual-EN/1.overview/2.quick-start/1.get-started.md).

# Checking the Status and Ports of **Nebula Graph** Services

You can list all services of **Nebula Graph** and check their exposed ports with the following command:

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

**Note**: We can see that the exposed port mapped to 3699 of the `nebula-docker-compose_graphd_1` container is 3699.

# Checking the Cluster Data and Logs

All services data and logs of **Nebula Graph** are stored in your local directories `nebula-docker-compose/data` and `nebula-docker-compose/logs` respectively.

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

# Stopping the Services of **Nebula Graph**

You can stop the services of **Nebula Graph** with the following command:

```shell
$ docker-compose down -v
```

The following information which indicates you successfully stop the services of **Nebula Graph** is displayed:

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

**Note**: As your data is stored in your local computer, your data will be reserved even after you stop the services of **Nebula Graph**.

## TODO

- [ ] `prometheus` and `grafana` collect cluster metrics
- [ ] `ansible` deployment tutorial
