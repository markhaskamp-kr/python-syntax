## unit tests to explore python syntax

### one time setup

- checkout the repository
- create virtual environment  *virtualenv*
    - from project root directory  
> python3 -m venv env

### daily use



- activate *python* from virtual environment
    - from project root directory
> . env/bin/activate

then

**unittest help**

> python -m unittest -h

**run all the tests**

> python -m unittest discover -s test -v  

or with shortcut shell script  

> . discover [-v]

**run specific tests**

> python -m unittest test/test\_foo.py -v

or with shortcut shell script

> . tests test/test\_foo.py -v  
> . tests test/test\_foo.py -k helloworld -v  
> . test test/test\_datetime.py -k strptime -v

**deactivate virtual environment**

> deactivate
