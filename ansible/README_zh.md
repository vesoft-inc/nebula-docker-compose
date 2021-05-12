# nebula-ansible

Nebula-Graph ansible 安装工具，用于部署 nebula 集群。

## 前提

1. 操作系统是 Centos7
2. 操作机有外网权限，可以下载 OSS 的 RPM 包
3. 部署的机器已经建好用户，而且打通从控制机到部署机的 SSH。
4. 所有机器的端口、数据盘等配置是一样的。

## 步骤

### 准备

部署机，创建用户，给用户目录权限，示例

```bash
useradd nebula
passwd nebula
# 默认安装在 /home/nebula/nebula，也可以自己制定部署目录
mkdir -p /data
chown -R nebula:nebula /data
```

控制机，打通 ssh

```bash
ssh-keygen
ssh-copy-id nebula@{your_deploy_machine}

```

### 安装 ansible

```bash

sudo yum install ansible

```

### 配置 ansible-playbook

* Git clone 工程。
* 修改 `inventory.ini` 文件
    - `install_source_type`，配置安装 GA 还是 nightly 的包。
    - `ansible_ssh_user`， SSH 的 Linux 用户，如 `nebula`
    - `packages_dir`，操作机下载 rpm 包的目录。
    - `deploy_dir`，部署服务所在目录，如 `/home/nebula/nebula`

* 修改 templates 中的各个配置 （如需要）。**注意**，不要更改 `--local_ip` 和 `--meta_server_addrs`

* 运行 `ansible -m ping all` 看是否 ssh 已经打通

### 运行

```bash
# 安装
# 如果只修改配置文件，不会重复覆盖二进制文件。
# 即当目录有二进制文件时不会替换，如果要替换二进制，先执行删除
# 需要安装的 rpm 包，会先下载到执行机的 package 文件夹
ansible-playbook install.yml

# 启动
ansible-playbook start.yml

# 停止
ansible-playbook stop.yml

# 查看状态
ansible-playbook status.yml

# 删除
# 先删除二进制文件，后删除整个部署目录，两个操作分别有提示。
ansible-playbook remove.yml

```
