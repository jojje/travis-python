# Travis scaffolding for python apps

Provides a CI pipeline using Github, Travis and PyPi.

Intended for my own reference bootstrapping python projects.

## One time setup
Needed on each machine where the code is being developed.

1. Install travis cli: `gem install -N travis`
2. Install github cli: `brew install hub`
3. Install twine for pypi project registration: `pip install "twine<1.7"`
4. Create a pypy config file for registering projects on PyPi

        cat > ~/.pypirc <<EOF
        [distutils]
        index-servers=
            pypi
            testpypi
        
        [testpypi]
        repository = https://testpypi.python.org/pypi
        username = <username>
        password = <password>
        
        [pypi]
        repository = https://pypi.python.org/pypi
        username = <username>
        password = <password>
        EOF

## Initialize a new project for testing and deploying to PyPi

1. Create a new github repo: `hub create [project-name]`
2. Copy the contents of _this repo_ to the new app _and adjust as needed_
3. Build a package for initial registration in PyPi: `make dist`
4. Register the project in test-pypi: 

        twine register -r testpypi dist/<package>.whl

5. Embed encrypted PyPi passwords in _.travis.yml_: `travis encrypt '<password>'`
6. Push the first commit: `git push -u origin master`
7. Ensure that travis testing works: `travis show`
8. Ensure the package has been pushed to PyPi testing:

        pip install --allow-external -i https://testpypi.python.org/pypi <package>

When deployment to test PyPi works, tag an initial release and repeat the previous check with the production pypo repo (`pip install <package>`).

