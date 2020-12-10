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

## 使用 Docker Compose 部署 Nebula Graph

Docker Compose 可以帮助您快速部署 Nebula Graph 服务。

- [使用 Docker Compose 部署 Nebula Graph](#使用-docker-compose-部署-nebula-graph)
- [前提条件](#前提条件)
- [部署流程](#部署流程)
- [查看 Nebula Graph 服务状态和端口](#查看-nebula-graph-服务状态和端口)
- [查看服务数据与日志](#查看服务数据与日志)
- [停止 Nebula Graph 服务](#停止-nebula-graph-服务)
- [安装 Nebula Graph 的其它方法](#安装-nebula-graph-的其它方法)
- [常见问题](#常见问题)
- [下一步](#下一步)

## 前提条件

* 已在主机中安装了[Docker](https://docs.docker.com/engine/install/)、[Docker Compose](https://docs.docker.com/compose/install/) 和 [Git](https://git-scm.com/download/linux)。

    >**说明**：
    >* 使用 Docker 时，如果您的用户没有 root 权限，请参见[以非 root 权限用户管理 Docker](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)。
    >* 为了确保这些应用正常工作，建议您安装其最新版本。

* 已在主机中启动了 Docker 服务。

* 如果您在该主机上使用 Docker Compose 部署过其它版本的 Nebula Graph，为了避免兼容性问题，请先备份需要保留的[服务数据](#查看服务数据与日志)，然后删除`nebula-docker-compose/data`目录。

## 部署流程

1. 使用 Git 将 `nebula-docker-compose` 库拷贝到您的主机。

   * 安装 Nebula Graph 1.0 版本请拷贝 `v1.0` 分支。

    ```shell
    $ git clone --branch v1.0 https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

   * 安装 Nebula Graph 2.0 版本请拷贝 `master` 分支。

    ```shell
    $ git clone https://github.com/vesoft-inc/nebula-docker-compose.git
    ```

2. 进入 `nebula-docker-compose` 目录。

    ```shell
    $ cd nebula-docker-compose/
    ```

3. 启动所有 Nebula Graph 服务。

    ```shell
    $ docker-compose up -d
    ```

    以下返回信息表明服务已启动：

    ```shell
    Creating nebula-docker-compose_metad2_1 ... done
    Creating nebula-docker-compose_metad1_1 ... done
    Creating nebula-docker-compose_metad0_1 ... done
    Creating nebula-docker-compose_storaged2_1 ... done
    Creating nebula-docker-compose_graphd_1    ... done
    Creating nebula-docker-compose_storaged0_1 ... done
    Creating nebula-docker-compose_storaged1_1 ... done
    ```

    >**说明**：如需了解上述服务的详情，请参见[ Nebula Graph 设计与架构](https://docs.nebula-graph.com.cn/manual-CN/1.overview/3.design-and-architecture/1.design-and-architecture/)。

4. 连接到 Nebula Graph。

    Nebula-console 是 Nebula Graph 的原生命令行客户端。在当前步骤中，Docker 会按下方命令中指定的 Docker Hub 路径将 nebula-console 镜像文件下载到本地主机，并用其连接 Nebula Graph 的 graphd 服务。您也可以使用其它客户端连接Nebula Graph，例如 [Nebula Graph Studio](https://github.com/vesoft-inc/nebula-web-docker) 以及[其它编程语言的客户端](https://docs.nebula-graph.com.cn/manual-CN/1.overview/2.quick-start/3.supported-clients/)。

   * 连接到 Nebula Graph 1.0 版本：

    ```shell
    $ docker run --rm -ti --network=host vesoft/nebula-console:nightly -u <user> -p <password> --addr=127.0.0.1 --port=3699
    ```

    * 连接到 Nebula Graph 2.0 版本：

   ```shell
    $ docker run --rm -ti --network nebula-docker-compose_nebula-net --entrypoint=/bin/sh vesoft/nebula-console:v2-preview-nightly
    docker> nebula-console -u <user> -p <password> --address=graphd --port=3699
    ```

    >**说明**：Nebula Graph 默认不开启身份验证功能，此时可以省略上述命令中的 `-u` 和 `-p` 选项。如需开启验证，请参见[身份验证](https://docs.nebula-graph.com.cn/manual-CN/3.build-develop-and-administration/4.account-management-statements/authentication/)。

    显示以下信息表明您已成功连接到 Nebula Graph：

    ```shell
    Welcome to Nebula Graph (Version 5d10861)

    (user@127.0.0.1) [(none)]>
    ```

## 查看 Nebula Graph 服务状态和端口

您可以使用如下命令查看 Nebula Graph 服务的详细信息，包括服务状态及端口号等：

```shell
$ docker-compose ps
```

返回结果的示例如下：

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

**说明**： Nebula Graph 默认通过 TCP3699 端口向客户端提供服务，您可以在[网络配置](https://docs.nebula-graph.com.cn/manual-CN/3.build-develop-and-administration/3.configurations/4.graph-config/#networking)中自定义端口号。

## 查看服务数据与日志

 Nebula Graph 的服务数据和日志被持久化地保存在主机的 `nebula-docker-compose/data` 和 `nebula-docker-compose/logs` 目录中。

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

## 停止 Nebula Graph 服务

您可以通过以下命令停止 Nebula Graph 服务：

```shell
$ docker-compose down -v
```

以下返回结果表明您已成功停止 Nebula Graph 服务：

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

## 安装 Nebula Graph 的其它方法
* [使用源代码](https://docs.nebula-graph.com.cn/manual-CN/3.build-develop-and-administration/1.build/1.build-source-code/)
* [使用 Docker](https://docs.nebula-graph.com.cn/manual-CN/3.build-develop-and-administration/1.build/2.build-by-docker/)
* [使用 .rpm 或 .deb 文件](https://docs.nebula-graph.com.cn/manual-CN/3.build-develop-and-administration/2.install/1.install-with-rpm-deb/)

## 常见问题

**问**：如何更新 nebula-console 客户端？

**答**：在主机的`nebula-docker-compose`目录中使用`docker pull`命令。例如，要更新 Nebula Graph 1.0 系列对应的 nebula-console，运行如下命令：

```Shell
docker pull vesoft/nebula-console:nightly
```

如需更新 Nebula Graph 2.0 pre 版本对应的 nebula-console，则运行如下命令：

```Shell
docker pull vesoft/nebula-console:v2-preview-nightly
```

# 下一步
您可以进行创建图空间和插入数据等操作，详情请参见[ Nebula Graph 快速入门](https://docs.nebula-graph.com.cn/manual-CN/1.overview/2.quick-start/1.get-started/)。