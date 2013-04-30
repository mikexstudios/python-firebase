from setuptools import setup, find_packages

setup(
    name = 'python-firebase',
    packages = find_packages(),
    version = '0.1.0',
    description = "Simple wrapper around Firebase's REST API",
    author = 'Michael Huynh',
    author_email = 'mike@mikexstudios.com',
    url = 'http://github.com/mikexstudios/python-firebase',
    install_requires = ['requests >=1.2.0,<1.2.99'], 
    classifiers = [
        'Programming Language :: Python', 
        'License :: OSI Approved :: BSD License',
    ]
)

