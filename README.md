<p align="center">
  <img src="https://nebula-graph.io/img/nav-nebula-logo.png"/>
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

There are multiple ways to deploy Nebula Graph, but using Docker Compose is usually considered to be a fast starter. This repository provides a convenient solution to deploy Nebula Graph with Docker Compose.

Choose a nebula-docker-compose branch before you start. The following table lists the most popular nebula-docker-compose branches and the corresponding Nebula Graph GitHub branches and versions.

For minor version of docker images(2.6.2 for instance), please check tags from the docker hub i.e. [here](https://hub.docker.com/r/vesoft/nebula-graphd/tags).

| nebula-docker-compose branch                                                                      | Nebula Graph branch and repository                                                    | Nebula Graph version                       | How to use nebula-docker-compose                                                                                                     |
| :-----------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| [`master`](https://github.com/vesoft-inc/nebula-docker-compose/tree/master)                       | `master` of the [nebula](https://github.com/vesoft-inc/nebula) repository | The latest development <br>version of v3.x | [Deploy Nebula Graph with Docker Compose](https://docs.nebula-graph.io/master/4.deployment-and-installation/2.compile-and-install-nebula-graph/3.deploy-nebula-graph-with-docker-compose/) |
| [`v3.0.1`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v3.0.1)                       | `v3.0.1` of the [nebula](https://github.com/vesoft-inc/nebula) repository | v3.0.1 | [Deploy Nebula Graph with Docker Compose](https://docs.nebula-graph.io/2.0/2.quick-start/2.deploy-nebula-graph-with-docker-compose/) |
| [`v2.6`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v2.6) <br> | `v2.6` of the [nebula](https://github.com/vesoft-inc/nebula) repository                                               | The latest released version of v.2.6.x                                    | [Deploy Nebula Graph with Docker Compose](https://github.com/vesoft-inc/nebula-docker-compose/blob/v2.6/README.md)                 |
| [`v2.5.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v2.5.0) | `v2.5.0` of the [nebula-graph](https://github.com/vesoft-inc/nebula-graph) repository                                              | v.2.5.0                                    | [Deploy Nebula Graph with Docker Compose](https://github.com/vesoft-inc/nebula-docker-compose/blob/v2.5.0/README.md)                 |
| [`v2.0.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v2.0.0)                       | `v2.0.0` of the nebula-graph repository                                               | v.2.0.0-GA                                 | [Deploy Nebula Graph with Docker Compose](https://github.com/vesoft-inc/nebula-docker-compose/blob/v2.0.0/README.md)                 |
| [`v1.0`](https://github.com/vesoft-inc/nebula-docker-compose/tree/v1.0)                           | `master` of the [nebula](https://github.com/vesoft-inc/nebula) repository             | The latest development <br>version of v1.x | [Deploy Nebula Graph with Docker Compose](https://github.com/vesoft-inc/nebula-docker-compose/blob/v1.0/README.md)                   |
