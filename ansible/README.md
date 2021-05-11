# nebula-ansible

English | [中文](README_zh.md)

**Attention**: Now nebula-ansible is only usable for CentOS 7

## Introduction

nebula-ansible is a `Nebula` cluster deployment tool based on [ansible playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html).

## Usage

### Prepare

Prepare linux user, nebula directory on deployment machine.

```bash
useradd nebula
passwd nebula
# nebula directory is  '/home/nebula/nebula' by default. Could change it by yourself.
mkdir -p /data
chown -R nebula:nebula /data
```

Perform SSH login without password on control machine.

```bash
ssh-keygen
ssh-copy-id nebula@{your_deployment_machine}

```

### Install ansible

```bash

sudo yum install ansible

```

Execute

```shell
ansible --version
```

and make sure your ansible version is > `2.5`.

Other installation methods can be seen [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

### Config ansible-playbook

* Git clone the project.
* Change `inventory.ini`
    - `install_source_type`, choose nebula package type, `GA` or `nightly`.
    - `ansible_ssh_user`, the Linux ssh user, e.g. `nebula`
    - `packages_dir`, RPM download directory on control machine.
    - `deploy_dir`, nebula directory on deployment machine. e.g. `/home/nebula/nebula`

* Change templates configuration if needed.  **IMPORTANT**, DO NOT CHANGE `--local_ip` and `--meta_server_addrs`

* Run `ansible -m ping all` to verify if all machines can be reached via SSH.

### Run playbooks

```bash
# install
ansible-playbook install.yml

# start
ansible-playbook start.yml

# stop
ansible-playbook stop.yml

# status
ansible-playbook status.yml

# remove
# remote binary firstly, then remove the whole directory.
ansible-playbook remove.yml

```
