# tdd-full-stack-app
Full stack application built with Django and TDD.

***

## Project Goals
Working to implement best practices when it comes to both software development, and specifically Django related development.

## References / Further Reading
- Boost your Django DX - Adam Johnson
- Test-Driven Development with Python - Harry Percival

***

## Installation Instructions

### Pip-tools / Pip-compile
First install pip-tools, which will give you access to pip-compile. You'll need
to run pip-compile in the root project directory to make sure that your
dependencies are gathered correctly depending on your development platform's
operating system.

*This project does not assume virtual environment
management platform (conda, poetry, virtualenv, etc.), but I would advise
configuring that properly first. My personal preference is conda.*

After that, from the project's root directory you should be able to run:
```shell
python -m pip install -r requirements.txt
```

### pre-commit
Next you'll need to install pre-commit to gain the full developer experience.

### Geckodriver for Selenium FTs
To run the functional / integration tests you will need to make sure that
geckodriver for Firefox is accessible via some path.

*If you happen to be using conda as your environment manager, you can look
for the "Script" folder that contains the django-admin executable, and then
move the geckodriver executable to that folder.*
