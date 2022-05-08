# Vaerks Flask Ecommerce Backend

## Table of Contents:

1. [Getting Started](#getting-started)
2. [Database](docs/DATABASE.md)

# Getting Started

## Cloning the project

Clone the project as you normally would to get the files included in the main module.
The repository includes submodules which will not automatically be cloned along with it. To ensure everything is provided run the following commands.

```
git submodule init
git submodule update
```

If the project is already setup, but no git commands work (other than git status) then the following might fix the problem.
git remote set-url origin https://github-username:github-access-token@github.com/Vaerks/docker-ecommerce-backend.git

## Running the project

If this is a fresh setup, start by generating the certificates needed by nginx, by running:

```
sudo ./init-letsencrypt.sh
```

To start the project in development mode, run the file **docker-compose.yml** with

```
docker-compose up -d
```

and wait for it to build. If there are any problems, attach to the log of the problematic container (often the one running Flask) with the following command:

```
docker logs --tail 1000 -f flask
```

## Webhooks:
