# Davis County [DC] Study Group

## Summary 2017-10-21


### Location

Met at the Centerville Branch of the Davis County Library. (Librarian said that
study rooms are available for reservation up to a week ahead. Just call in to
the information desk.)


### Introduction to OpenAI.

[Universe](https://blog.openai.com/universe/) is an ambitious project to create
a "wide" AI: something capable of learning and performing well at new games
(instead of just the games for which it is trained.)

[Gym](https://github.com/openai/gym) is a framework 



### Introduction to IPython command line tools and ipdb.

[IPython pdb](https://pypi.python.org/pypi/ipdb) is a handy extension to the
standard python debugger.


### Ran through basic cartpole scenario and attempted a stable solution.

[OpenAI Gym Introduction](https://gym.openai.com/docs/)

We discovered that balancing a pole required more than moving the platform in
the same direction as the pole was falling.


### Setting up VirtualEnv in Ubuntu 

[VirtualEnv Burrito](https://github.com/brainsik/virtualenv-burrito) is a
script to install virtualenvwrapper on a linux or Mac box as easily as possible.

On the Ubuntu machine we [effectively] ran the following.

    curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | exclude_profile=1 $SHELL
    echo "source $VENVBURRITO/startup.sh" >> .bash_aliases


### VirtualEnv links for Microsoft boxes

[VirtualEnv for Powershell](https://virtualenv.pypa.io/en/stable/userguide/?highlight=powershell)

[VirtualEnvWrapper for Powershell](https://pypi.python.org/pypi/virtualenvwrapper-powershell/2.7.1)
