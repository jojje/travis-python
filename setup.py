from setuptools import setup, find_packages
from app.version import VERSION
import os


def readme():
    if os.path.exists('README.rst'):
        with open('README.rst') as f:
            return f.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='cli-ci-scaffold',
    version=VERSION,
    url='https://github.com/jojje/travis-python',
    author='Jonas Tingeborn',
    author_email='contact-me@github',
    description='Sample CLI app built, tested and deployed using Github and Travis',
    long_description=readme(),
    license='http://opensource.org/licenses/MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords=['bootstrap', 'cli', 'scaffold', 'plumbing'],
    packages=find_packages(exclude=["test"]),
    install_requires=required,
    entry_points='''
        [console_scripts]
        my-cli=app.__main__:main
    '''
)
