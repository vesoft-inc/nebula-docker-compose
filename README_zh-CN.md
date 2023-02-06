<p align="center">
  <img src="https://nebula-website-cn.oss-cn-hangzhou.aliyuncs.com/nebula-website/images/nebulagraph-logo.png"/>
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
更多小版本的 Docker 镜像分支（比如对应 2.6.2 版本的镜像），可以在 Docker Hub 上查询相应 tag，比如[这里](https://hub.docker.com/r/vesoft/nebula-graphd/tags)。

| nebula-docker-compose分支                                                               | Nebula Graph分支与仓库                                                         | Nebula Graph版本     | 如何使用本仓库                                                                                                                    |
| :-------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [`master`](https://github.com/vesoft-inc/nebula-docker-compose/tree/master)                       | `master` of the [nebula repository](https://github.com/vesoft-inc/nebula) | The latest development <br>version of v3.x | [Docker Compose部署Nebula Graph](https://docs.nebula-graph.io/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/) |
| [`v3.4`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v3.4.0)                       | `v3.4.x` of the [nebula](https://github.com/vesoft-inc/nebula) repository | v3.4.x | [Docker Compose部署Nebula Graph](https://docs.nebula-graph.io/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/) |
| [`v3.3`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v3.3.0)                       | `v3.3.x` of the [nebula](https://github.com/vesoft-inc/nebula) repository | v3.3.x | [Deploy Nebula Graph with Docker Compose](https://docs.nebula-graph.io/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/) |
| [`v3.2`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v3.2.0)                       | `v3.2.x` of the [nebula](https://github.com/vesoft-inc/nebula) repository | v3.2.x | [Docker Compose部署Nebula Graph](https://docs.nebula-graph.io/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/) |
| [`v3.1`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v3.1.0)                       | `v3.1.x` of the [nebula](https://github.com/vesoft-inc/nebula) repository | v3.1.x | [Docker Compose部署Nebula Graph](https://docs.nebula-graph.io/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/) |
| [`v3.0.1`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v3.0.1)                       | `v3.0.1` of the [nebula repository](https://github.com/vesoft-inc/nebula) | v3.0.1 | [Docker Compose部署Nebula Graph](https://docs.nebula-graph.io/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/) |
| [`v2.6`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v2.6) <br> | `v2.6` of the nebula-graph repository                                               | The latest released version of v.2.6.x                                    | [Docker Compose部署Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/v2.6/README.md)                 |
| [`v2.5.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v2.5.0) | `v2.5.0` of the nebula-graph repository                                               | v.2.5.0                                    | [Docker Compose部署Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/v2.5.0/README.md)                 |
| [`v2.0.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v2.0.0)                       | `v2.0.0` of the nebula-graph repository                                               | v.2.0.0-GA                                 | [Docker Compose部署Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/v2.0.0/README.md)                 |
| [`v1.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v1.0)                           | `master` of the [nebula](https://github.com/vesoft-inc/nebula) repository             | The latest development <br>version of v1.x | [Docker Compose部署Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/v1.0/README.md)                   |
