Go
==

Requirements
------------

Tested with this version of python:

* Python 3.7.2

Getting Started
---------------

To set up your local environment you should create a virtualenv and
install everything into it.

    $ mkvirtualenv go

Pip install this repo, either from a local copy,

    $ pip install -e go

or from github,

    $ pip install git+https://github.com/rtrusso/go

and then install the requirements

    $ pip install -r requirements_server.txt
    $ pip install -r requirements_player.txt

Please note these currently point to the forked copy of the
repositories updated for python3, instead of the original repo created
by jbradberry. This will be corrected once the python3 PRs are picked
up in the original repos.

To run the server with Go

    $ board-serve.py go

Optionally, the server ip address and port number can be added

    $ board-serve.py go 0.0.0.0
    $ board-serve.py go 0.0.0.0 8000

To connect a client as a human player

    $ board-play.py go human
    $ board-play.py go human 192.168.1.1 8000   # with ip addr and port

or with the provided AI player

    $ board-play.py go jrb.mcts.uct
