<p align="center">
  <img src="https://nebula-graph.io/img/nav-nebula-logo.png"/>
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

部署Nebula Graph的方式有很多，使用Docker Compose是其中较方便的一种。本仓库中保存了使用Docker Compose快速部署Nebula Graph的解决方案。

在使用本仓库前，请选择好您需要使用的分支。下表列出了常用分支以及与其相对应的Nebula Graph分支和版本。

| nebula-docker-compose分支                                                               | Nebula Graph分支与仓库                                                         | Nebula Graph版本     | 如何使用本仓库                                                                                                                    |
| :-------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [`master`](https://github.com/vesoft-inc/nebula-docker-compose/tree/master)             | [nebula-graph仓库](https://github.com/vesoft-inc/nebula-graph)的`master`分支   | 最新的v2.x开发版本   | [Docker Compose部署Nebula Graph](https://docs.nebula-graph.com.cn/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/)   |
| [`v2.0.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v2.0.0)（**推荐**） | nebula-graph仓库的`v2.0.0`分支                                                 | v.2.0.0-GA           | [Docker Compose部署Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/v2.0.0/README_zh-CN.md)                 |
| [`v1.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v1.0)                 | [nebula](https://github.com/vesoft-inc/nebula)仓库的`master`分支               | 最新的v1.x开发版本   | [Docker Compose部署Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/v1.0/README_zh-CN.md)                   |

## FAQ

### Running in M1 macOS

如果您使用 Docker Desktop，只需要执行：

```bash
docker compose up -d
```

或者，如果您想使用 [lima](https://github.com/lima-vm/lima)：

- 安装 lima `brew install lima`
- 启动 lima VM `limactl start`
- 然后您可以在 lima VM 中执行指令： `lima <command>` ，比如 `lima uname -a`

- 在这之后，就可以用 `lima nerdctl` 替代 `docker` 这个命令行了，值得注意的是因为这里用的是 `nerdctl` 而不是 docker-compose，需要引用 `docker-compose-nerdctl.yaml`。

```bash
rm -fr data logs
mkdir -p data/{meta,storage}{0..2}/nebula logs/{meta,storage,graph}{0..2} logs/graph
lima nerdctl compose --file docker-compose-nerdctl.yaml up -d
```

- 从 lima VM 里用 console 接入 nebula：

```bash
lima ./nebula-console-linux-arm64-v2.6.0 -addr host.lima.internal -port 9669 -user root -p password
```

### Running with nerdctl

如果您使用 [nerdctl](https://github.com/containerd/nerdctl)，可以用下边的兼容的 yaml 文件，这个情况下需要先创建 data、logs 目录。

```bash
mkdir -p data/{meta,storage}{0..2}/nebula logs/{meta,storage,graph}{0..2} logs/graph

nerdctl compose --file docker-compose-nerdctl.yaml up -d
```
