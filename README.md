# Vaerks Flask Ecommerce Backend

## Table of Contents:

1. [Getting Started](#getting-started)
2. [Database](docs/DATABASE.md)

# Getting Started

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
