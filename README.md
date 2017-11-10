>#  roo

## CLI tool for managing containerized Wordpress Apps from GitHub Commits.

### How do I set up roo?

To try out roo, simply enter the following commands to start a Python Viritual Environment and install roo on it:

1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install --editable .`

### Pre-requisites:
1. Docker
2. Python3
3. Pip

### How do I use roo?
In order to use roo, all you need to do is go to the [Wordpress GitHub site](https://github.com/WordPress/WordPress), grab a specific commit (ideally from Master); make sure you grab the non-truncated hash. If you don't provide a hash, roo will build the latest version of master.

Roo has two commands, `build` and `destroy`. You should use these to manage your containers to avoid docker mis-configurations. Please see the examples below.

NB: You can run as many versions of Wordpress as you please providing you have enough compute power. Additionally, to actually access them you need to give them different names, and most importantly different port mappings on your machine. Hence the flags below.

There are a few things at your control:

* Commit - specified by either `--commit` or `-c`.
* Port - specified by either `--port` or `-p`.
* Name - specified by either `--name` or `-p`, this becomes the name of the docker-compose, you will need to remember it to shut down correctly, or simply run `docker ps` and find the name there.

If in doubt, use `roo [command] --help`

```
$ roo build --help
Usage: roo build [OPTIONS]

  Used to deploy a containerized wordpress app.

Options:
  -n, --name TEXT    Provide a human friendly, project name for your wordpress
                     container, defaults to the commit SHA.
  -c, --commit TEXT  Provide a Git commit Hash to pull a specific Wordpress
                     version.
  -p, --port TEXT    Provide a port to access sonarqube over.
  --help             Show this message and exit.
```

### Build Examples

To simply run the latest commit of master:

`roo build`

To build a specific commit on a port and give it a name:

`roo build -c e8229a25d5f4c620ef5f021abe70224cc6c550de -p 24601 -n OliversTestWP`

### Destroy Examples

When destroying, if you gave a name, you must give the name to destroy, otherwise you must provide the commit. This is to ensure that the correct containers are being destroyed. 


If you specified a name on build:

`roo destroy -n OliversTestWP`

If you didn't specify a name on build:

`roo destroy -c e8229a25d5f4c620ef5f021abe70224cc6c550de`
