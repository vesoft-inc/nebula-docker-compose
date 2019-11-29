# Nebula Graph Docker 部署

本仓库提供如下方式部署 [nebula](https://github.com/vesoft-inc/nebula) 集群：

- `docker-compose`
- `ansible` (开发中)

## docker-compose

首先请确保系统已安装 `docker` 和 `docker-compose`。
已部署的 nebula 服务：

- 3 副本 `nebula-metad` 服务
- 3 副本 `nebula-storaged` 服务
- 1 副本 `nebula-graphd` 服务

**Step 0**: 使用 `git` 将本仓库克隆至本地然后使用 `cd` 切换至仓库根目录：

```shell
$ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
$ cd nebula-docker-compose/
```

**Step 1**： 使用 `docker-compose` 启动所有服务

```shell
$ docker-compose up -d
Creating network "docker_nebula-net" with the default driver
Creating nebula-docker-compose_metad2_1 ... done
Creating nebula-docker-compose_metad1_1 ... done
Creating nebula-docker-compose_metad0_1 ... done
Creating nebula-docker-compose_storaged0_1 ... done
Creating nebula-docker-compose_storaged1_1 ... done
Creating nebula-docker-compose_graphd_1    ... done
Creating nebula-docker-compose_storaged2_1 ... done
```

**Step 2**： 列出所有 nebula 服务及其对应的端口

``` shell
$ docker-compose ps
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

可以看到映射到 `nebula-docker-compose_graphd_1` 容器的 3699 的暴露端口是 3699。

**Step 3**: 使用 `nebula-console` docker 容器连接上述**图服务**

如果本地已经存在 `vesoft/nebula-console:nightly` 镜像，请先删除并重新拉取：

```shell
$ docker rm $(docker ps -qa -f status=exited) # cleanup exited containers
$ docker rmi vesoft/nebula-console:nightly
$ docker pull vesoft/nebula-console:nightly
```

使用以下命令在 `docker-compose.yaml` 文件所在的目录中获取最新的 **Nebula Graph** 镜像。

```bash
docker-compose pull
```

现在，你可以试着使用新版的 `vesoft/nebula-console` 容器链接 graph 服务。

``` shell
$ docker run --rm -ti --network=host vesoft/nebula-console:nightly --addr=127.0.0.1 --port=3699

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

**Step 4**：查看集群数据及日志

所有 nebula 服务的数据及日志均位于本地仓库 `nebula-docker-compose` 的  `./data` 及 `./logs`路径下。

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

**Step 5**: 停止 nebula 服务

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

希望你喜欢 nebula :)
