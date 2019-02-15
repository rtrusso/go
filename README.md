Go
==

This is a python implementation of the board game Go. It is compatible
with the same board game framework used by
[ultimate_tictactoe](https://github.com/jbradberry/ultimate_tictactoe).

The idea with this project is to enable some experimentation with
machine learning inspired by the AlphaGo and AlphaZero projects.

Known Issues
------------

The author doesn't actually know how to play Go and is attempting to
write correct code based on rule specifications.

- There is some bug with not allowing play in previously-captured intersections.
- Scoring is not implemented correctly.

Requirements
------------

Tested with this version of python:

* Python 3.7.2

Getting Started
---------------

To set up your local environment you should create a virtualenv and
install everything into it.

    $ virtualenv go

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

or with the AI player, see [jbradberry/mcts](https://github.com/rtrusso/mcts) (link to python3 update fork)

    $ board-play.py go jrb.mcts.uct
