<div align="center">
  <h1>Nebula Graph Docker Deployment</h1>
  <div>
    <a href="https://github.com/vesoft-inc/nebula-docker-compose/blob/master/README.md">英文</a>
  </div>
  <br>
</div>

# Nebula Graph Docker 部署

## 概述

在本文档中，我们将指导您使用 [Docker](https://docs.docker.com/install/) 和 [Docker Compose](https://docs.docker.com/compose/install/) 来部署 **Nebula Graph** 集群。我们将向您展示如何[查看 **Nebula Graph** 的服务状态和端口](#查看-Nebula-Graph-服务状态和端口)，如何[查看集群数据和日志](#查看集群数据和日志), 以及如何[停止 **Nebula Graph** 服务](#停止-Nebula-Graph-服务)。

## 前提条件

在开始部署 **Nebula Graph** 集群前，确保您已部署最新版本的 [Docker](https://docs.docker.com/install/) 和 [Docker Compose](https://docs.docker.com/compose/install/)。

**注意**：如果您没有 [Docker](https://docs.docker.com/install/) 的 `root` 权限，请参考 [如何设置 Docker 的 root 权限](https://docs.docker.com/install/linux/linux-postinstall/)。

## 要部署的 **Nebula Graph** 服务

在本指南中我们将部署以下 **Nebula Graph** 服务：

* 3 副本 `nebula-metad` 服务
* 3 副本 `nebula-storaged` 服务
* 1 副本 `nebula-graphd` 服务

## 部署 **Nebula Graph** 集群

您可以通过以下命令部署 **Nebula Graph** 集群：

1. 把 `nebula-docker-compose` 库拷贝到您的本地电脑。

```shell
$ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
```

2. 把当前路径更改为 `nebula-docker-compose` 路径。

```shell
$ cd nebula-docker-compose/
```

3. 启动所有 **Nebula Graph** 服务。

```shell
$ docker-compose up -d
```

显示以下信息表明服务已启动：

```shell
Creating nebula-docker-compose_metad2_1 ... done
Creating nebula-docker-compose_metad1_1 ... done
Creating nebula-docker-compose_metad0_1 ... done
Creating nebula-docker-compose_storaged2_1 ... done
Creating nebula-docker-compose_graphd_1    ... done
Creating nebula-docker-compose_storaged0_1 ... done
Creating nebula-docker-compose_storaged1_1 ... done
```

4. 把 `vesoft/nebula-console:nightly` 镜像下拉到您的本地电脑。

```shell
$ docker pull vesoft/nebula-console:nightly
```

国内从 Docker Hub 拉取镜像有时会遇到困难，此时可以配置加速镜像。例如:

* Azure 中国镜像 https://dockerhub.azk8s.cn
* 七牛云 https://reg-mirror.qiniu.com

对于 Linux 用户，请在 `/etc/docker/daemon.json` 中写入如下内容（如果文件不存在请新建该文件）：

```bash
{
  "registry-mirrors": [
    "https://dockerhub.azk8s.cn",
    "https://reg-mirror.qiniu.com"
  ]
}
```

对于 macOS 用户，请点击任务栏中 Docker Desktop 图标 -> Preferences -> Daemon -> Registry mirrors。在列表中添加 https://dockerhub.azk8s.cn 和 https://reg-mirror.qiniu.com。修改完成后，点击 Apply & Restart 按钮，重启 Docker。

**注意**：

a. 我们将使用 `nebula-console` docker 容器来连接 **Nebula Graph** 的图服务。

b. 如果您之前拉取了 `vesoft/nebula-console` 镜像，使用以下命令先删除该镜像然后再拉取：

   * `docker rm $(docker ps -qa -f status=exited) # cleanup exited containers`
   * `docker rmi vesoft/nebula-console:nightly`

c. 如果您之前拉取了 **Nebula Graph** 镜像，您可以通过以下命令更新镜像：

```shell
$ docker-compose pull
```

5. 连接到 **Nebula Graph** 的图服务。

```shell
$ docker run --rm -ti --network=host vesoft/nebula-console:nightly --addr=127.0.0.1 --port=3699
```

显示以下信息表明您已成功连接到 **Nebula Graph**：

```shell
Welcome to Nebula Graph (Version 5d10861)

(user@127.0.0.1) [(none)]>

```

**注意**: 现在您可以通过创建空间、tag、space 等操作来使用 **Nebula Graph**。 获取详细信息，请参考 [快速入门](https://github.com/vesoft-inc/nebula/blob/master/docs/manual-CN/1.overview/2.quick-start/1.get-started.md)。

## 查看 **Nebula Graph** 服务状态和端口

您可以在终端输入以下命令把所有 **Nebula Graph** 服务以列表的形式显示出来并查看其暴露的端口：

```shell
$ docker-compose ps
```

显示以下信息：

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

**注意**： 可以看到映射到 `nebula-docker-compose_graphd_1` 容器的 3699 的暴露端口是 3699。

## 查看集群数据和日志

 **Nebula Graph** 的所有服务数据和日志分别存储在您本地目录 `nebula-docker-compose/data` 和 `nebula-docker-compose/logs`。

目录结构如下所示：

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

## 停止 **Nebula Graph** 服务

您可以通过以下命令停止 **Nebula Graph** 的服务：

```shell
$ docker-compose down -v
```

显示以下信息表明您已成功停止 **Nebula Graph** 服务：

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

**注意**： 由于您的数据存储在您的本地电脑上，所以即使您停止 **Nebula Graph** 服务，数据也会保留在您的本地电脑。
