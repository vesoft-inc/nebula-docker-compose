# Nebula Graph Docker Deployment

In this repository, we provide following methods to deploy a [nebula](https://github.com/vesoft-inc/nebula) cluster:

- `docker-compose`
- `ansible` (coming soon)

## docker-compose

First of all, install `docker` and `docker-compose` in your system.

The nebula services to be deployed:

- 3 replicas of `nebula-metad` service
- 3 replicas of `nebula-storaged` service
- 1 replica of `nebula-graphd` service

**Step 0**: Use `git` to clone this repo to your local directory and `cd` to the root directory of project:

```shell
$ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
$ cd nebula-docker-compose/
```

**Step 1**: Start all services with `docker-compose`

```shell
$ docker-compose up -d
Creating network "docker_nebula-net" with the default driver
Creating docker_metad2_1 ... done
Creating docker_metad0_1 ... done
Creating docker_metad1_1 ... done
Creating docker_graphd_1   ... done
Creating docker_storaged2_1 ... done
Creating docker_storaged0_1 ... done
Creating docker_storaged1_1 ... done
```

**Step 2**: List all nebula services and check their exposed ports

``` shell
$ docker-compose ps
       Name                     Command                       State                                                   Ports
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
docker_graphd_1      ./bin/nebula-graphd --flag ...   Up (health: starting)   0.0.0.0:32867->13000/tcp, 0.0.0.0:32866->13002/tcp, 3369/tcp, 0.0.0.0:32868->3699/tcp
docker_metad0_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:32865->11000/tcp, 0.0.0.0:32864->11002/tcp, 45500/tcp, 45501/tcp
docker_metad1_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:32863->11000/tcp, 0.0.0.0:32862->11002/tcp, 45500/tcp, 45501/tcp
docker_metad2_1      ./bin/nebula-metad --flagf ...   Up (health: starting)   0.0.0.0:32861->11000/tcp, 0.0.0.0:32860->11002/tcp, 45500/tcp, 45501/tcp
docker_storaged0_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:32879->12000/tcp, 0.0.0.0:32877->12002/tcp, 44500/tcp, 44501/tcp
docker_storaged1_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:32876->12000/tcp, 0.0.0.0:32872->12002/tcp, 44500/tcp, 44501/tcp
docker_storaged2_1   ./bin/nebula-storaged --fl ...   Up (health: starting)   0.0.0.0:32873->12000/tcp, 0.0.0.0:32870->12002/tcp, 44500/tcp, 44501/tcp
```

Now we can see the exposed port mapped to `3699` of `docker_graphd_1` container is `32868`.

**Step 3**: Use `nebula-console` docker container to connect to the above **graph service**

``` shell
$ docker run --rm -ti --network=host vesoft/nebula-console --addr=127.0.0.1 --port=32868

Welcome to Nebula Graph (Version 49d651f)

(user@127.0.0.1) [(none)]> SHOW HOSTS;
=============================================================================================
| Ip         | Port  | Status | Leader count | Leader distribution | Partition distribution |
=============================================================================================
| 172.28.2.1 | 44500 | online | 0            |                     |                        |
---------------------------------------------------------------------------------------------
| 172.28.2.2 | 44500 | online | 0            |                     |                        |
---------------------------------------------------------------------------------------------
| 172.28.2.3 | 44500 | online | 0            |                     |                        |
---------------------------------------------------------------------------------------------
Got 3 rows (Time spent: 6479/7619 us)

(user@127.0.0.1) [(none)]> CREATE SPACE test(partition_num=1024, replica_factor=3);
Execution succeeded (Time spent: 19558/20769 us)

(user@127.0.0.1) [(none)]> SHOW SPACES;
========
| Name |
========
| test |
--------
Got 1 rows (Time spent: 1578/2853 us)

(user@127.0.0.1) [(none)]> USE test;
Execution succeeded (Time spent: 1061/1773 us)

(user@127.0.0.1) [test]>
```

**Step 4**: Check cluster data and logs

All nebula service data and logs are stored in local directory: `./data` and `./logs`.

```text
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

**Step 5**: Stop nebula services

```shell
$ docker-compose down -v
Stopping nebula-docker-compose_graphd_1    ... done
Stopping nebula-docker-compose_storaged1_1 ... done
Stopping nebula-docker-compose_storaged0_1 ... done
Stopping nebula-docker-compose_storaged2_1 ... done
Stopping nebula-docker-compose_metad0_1    ... done
Stopping nebula-docker-compose_metad1_1    ... done
Stopping nebula-docker-compose_metad2_1    ... done
Removing nebula-docker-compose_graphd_1    ... done
Removing nebula-docker-compose_storaged1_1 ... done
Removing nebula-docker-compose_storaged0_1 ... done
Removing nebula-docker-compose_storaged2_1 ... done
Removing nebula-docker-compose_metad0_1    ... done
Removing nebula-docker-compose_metad1_1    ... done
Removing nebula-docker-compose_metad2_1    ... done
Removing network nebula-docker-compose_nebula-net
```

Enjoy nebula graph :)

## TODO

- [ ] `prometheus` and `grafana` collect cluster metrics
- [ ] `ansible` deployment tutorial
