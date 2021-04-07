<p align="center">
  <img src="https://github.com/vesoft-inc/nebula/raw/master/docs/logo.png"/>
  <br>中文 | <a href="README.md">English</a>
  <br>能够容纳千亿个顶点和万亿条边，并提供毫秒级查询延时的图数据库解决方案<br>
</p>

<p align="center">
  <a href="https://user-images.githubusercontent.com/38887077/67449282-4362b300-f64c-11e9-878f-7efc373e5e55.jpg"><img src="https://img.shields.io/badge/WeChat-%E5%BE%AE%E4%BF%A1-brightgreen" alt="WeiXin"></a>
  <a href="https://www.zhihu.com/org/nebulagraph/activities"><img src="https://img.shields.io/badge/Zhihu-%E7%9F%A5%E4%B9%8E-blue" alt="Zhihu"></a>
  <a href="https://segmentfault.com/t/nebula"><img src="https://img.shields.io/badge/SegmentFault-%E6%80%9D%E5%90%A6-green" alt="SegmentFault"></a>
  <a href="https://weibo.com/p/1006067122684542/home?from=page_100606&mod=TAB#place"><img src="https://img.shields.io/badge/Weibo-%E5%BE%AE%E5%8D%9A-red" alt="Sina Weibo"></a>
  <a href="http://githubbadges.com/star.svg?user=vesoft-inc&repo=nebula&style=default">
    <img src="http://githubbadges.com/star.svg?user=vesoft-inc&repo=nebula&style=default" alt="nebula star"/>
  </a>
  <a href="http://githubbadges.com/fork.svg?user=vesoft-inc&repo=nebula&style=default">
    <img src="http://githubbadges.com/fork.svg?user=vesoft-inc&repo=nebula&style=default" alt="nebula fork"/>
  </a>
  <a href="https://codecov.io/gh/vesoft-inc/nebula">
    <img src="https://codecov.io/gh/vesoft-inc/nebula/branch/master/graph/badge.svg" alt="codecov"/>
  </a>
</p>

`v2.0.0`分支储存了使用Docker Compose部署Nebula Graph v2.0.0的解决方案。

# Docker Compose部署Nebula Graph

有多种方式可以部署Nebula Graph，但是使用Docker Compose通常是最快的方式。

## 阅读指南

如果您是带着如下问题阅读本文，可以直接单击问题跳转查看对应的说明。

- [部署Nebula Graph之前需要做什么准备工作？](#前提条件)

- [如何通过Docker Compose快速部署Nebula Graph？](#部署和连接Nebula-Graph)

- [如何检查Nebula Graph服务的状态和端口？](#查看Nebula-Graph服务的状态和端口)

- [如何检查Nebula Graph服务的数据和日志？](#查看Nebula-Graph服务的数据和日志)

- [如何停止Nebula Graph服务？](#停止Nebula-Graph服务)

- [如何通过其他方式部署Nebula Graph？](#相关文档)

## 前提条件

- 主机上安装如下应用程序。

    | 应用程序 | 推荐版本 | 官方安装参考 |
    |:---|:---|:---|
    |Docker|最新版本|[Install Docker Engine](https://docs.docker.com/engine/install/) |
    |Docker Compose|最新版本|[Install Docker Compose](https://docs.docker.com/compose/install/)|
    |Git|最新版本|[Download Git](https://git-scm.com/download/)|

- 如果您使用非root用户部署Nebula Graph，请授权该用户Docker相关的权限。详细信息，请参见[Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)。

- 启动主机上的Docker服务。

- 如果您已经通过Docker Compose在主机上部署了另一个版本的Nebula Graph，为避免兼容性问题，需要您删除目录`nebula-docker-compose/data`。

    >**注意**：请先备份需要保留的数据，再删除该目录。

## 部署和连接Nebula Graph

1. 通过Git克隆`nebula-docker-compose`仓库的`v2.0.0`分支到您的主机。

    ```bash
    $ git clone -branch v2.0.0 https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

2. 切换至目录`nebula-docker-compose`。

    ```bash
    $ cd nebula-docker-compose/
    ```

3. 执行如下命令启动Nebula Graph服务。

    >**说明**: 如果长期未更新镜像，请先更新[Nebula Graph镜像](#如何升级nebula-graph)和[Nebula Console镜像](#如何更新nebula-console)。

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

    >**说明**: 上述服务的更多信息，请参见[架构总览](https://docs.nebula-graph.com.cn/2.0.0/1.introduction/3.nebula-graph-architecture/1.architecture-overview/)。

4. 连接Nebula Graph。

    1. 使用Nebula Console镜像启动一个容器，并连接到Nebula Graph服务所在的网络（nebula-docker-compose_nebula-net）中。

    ```bash
    $ docker run --rm -ti --network nebula-docker-compose_nebula-net --entrypoint=/bin/sh vesoft/nebula-console:v2.0.0-ga
    ```

    >**说明**：您的本地网络可能和示例中的`nebula-docker-compose_nebula-net`不同，请使用如下命令查看。

    ```bash
    $ docker network  ls
    NETWORK ID          NAME                               DRIVER              SCOPE
    a74c312b1d16        bridge                             bridge              local
    dbfa82505f0e        host                               host                local
    ed55ccf356ae        nebula-docker-compose_nebula-net   bridge              local
    93ba48b4b288        none                               null                local
    ```

    2. 通过Nebula Console连接Nebula Graph。

    ```bash
    docker> nebula-console -u user -p password --address=graphd --port=9669
    ```

    >**说明**：默认情况下，身份认证功能是关闭的，可以使用任意用户名和密码登录。如果想使用身份认证，请参见[身份认证](https://docs.nebula-graph.com.cn/2.0.0/7.data-security/1.authentication/1.authentication/)。

    3. 执行如下命令检查`nebula-storaged`进程状态。

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

5. 执行两次`exit` 可以退出容器。

## 查看Nebula Graph服务的状态和端口

执行命令`docker-compose ps`可以列出Nebula Graph服务的状态和端口。

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

Nebula Graph默认使用`9669`端口为客户端提供服务，如果需要修改端口，请修改目录`nebula-docker-compose`内的文件`docker-compose.yaml`，然后重启Nebula Graph服务。

## 查看Nebula Graph服务的数据和日志

Nebula Graph的所有数据和日志都持久化存储在`nebula-docker-compose/data`和`nebula-docker-compose/logs`目录中。

目录的结构如下：

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

## 停止Nebula Graph服务

您可以执行如下命令停止Nebula Graph服务：

```bash
$ docker-compose down
```

如果返回如下信息，表示已经成功停止服务。

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

>**说明**：命令`docker-compose down -v`将会**删除**所有本地Nebula Graph的数据。如果您使用的是developing或nightly版本，并且有一些兼容性问题，请尝试这个命令。

## 常见问题

### 如何更新Nebula Graph服务的Docker镜像？

在目录`nebula-docker-compose`内执行命令`docker-compose pull`，可以更新Graph服务、Storage服务和Meta服务的镜像。

### 执行命令`docker-compose pull`报错`ERROR: toomanyrequests`

您可能遇到如下错误：

`ERROR: toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit`

以上错误表示您已达到Docker Hub的速率限制。解决方案请参见[Understanding Docker Hub Rate Limiting](https://www.docker.com/increase-rate-limit)。

### 如何更新Nebula Console？

执行如下命令可以更新Nebula Console客户端镜像。

```bash
docker pull vesoft/nebula-console:v2.0.0-ga
```

### 如何升级用Docker Compose部署的Nebula Graph？

更新Nebula Graph的Docker镜像并重启服务：

1. 在目录`nebula-docker-compose`内，执行命令`docker-compose pull`更新Nebula Graph的Docker镜像。

2. 执行命令`docker-compose down`停止Nebula Graph服务。

3. 执行命令`docker-compose up -d`启动Nebula Graph服务。

### 为什么更新nebula-docker-compose仓库（Nebula Graph 2.0.0-RC）后，无法通过端口`3699`连接Nebula Graph？

在Nebula Graph 2.0.0-RC版本，默认端口从`3699`改为`9669`。请使用`9669`端口连接，或修改配置文件`docker-compose.yaml`内的端口。

### 为什么更新nebula-docker-compose仓库后，无法访问数据？（2021年01月04日）

如果您在2021年01月04日后更新过nebula-docker-compose仓库，而且之前已经有数据，请修改文件`docker-compose.yaml`，将端口修改为之前使用的端口。详情请参见[修改默认端口](https://github.com/vesoft-inc/nebula-docker-compose/commit/2a612f1c4f0e2c31515e971b24b355b3be69420a)。

### 为什么更新nebula-docker-compose仓库后，无法访问数据？（2021年01月27日）

2021年01月27日修改了数据格式，无法兼容之前的数据，请执行命令`docker-compose down -v`删除所有本地数据。

## 相关文档

- [使用源码安装部署Nebula Graph](https://docs.nebula-graph.com.cn/2.0.0/4.deployment-and-installation/2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code/)
- [使用RPM或DEB安装包安装Nebula Graph](https://docs.nebula-graph.com.cn/2.0.0/4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb/)
- [多种方式连接Nebula Graph](https://docs.nebula-graph.com.cn/2.0.0/2.quick-start/3.connect-to-nebula-graph/)