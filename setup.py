from distutils.core import setup

setup(
    name='Go',
    version='0.1.0-dev',
    author='Richard Russo',
    author_email='',
    packages=['go'],
    entry_points={
        'jrb_board.games': 'go = go.board:Board',
    },
    license='LICENSE',
    description="An implementation of Go.",
)
