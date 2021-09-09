# setup.py

from setuptools import setup, find_packages

#load the README file
with open(file="README.md", mode="r") as readme_file:
    long_description = readme_file.read()

setup(

    #package name
    name='equities_database',

    #author
    author='Max Herre',

    #author linkedin
    author='www.linkedin.com/in/maxherre/',

    #current version
    version='0.0.1',

    #short description
    description='A client library for collecting price data on US equities',

    #long description
    long_description=long_description,
    long_description_content_type="text/markdown",

    #GitHub URL
    url='https://github.com/maxherre/equities-database-tool',
    
    #requirements
    install_requires=[
        'appdirs==1.4.4',
        'attrs==21.2.0',
        'black==21.7b0',
        'certifi==2021.5.30',
        'charset-normalizer==2.0.4',
        'click==8.0.1',
        'colorama==0.4.4',
        'greenlet==1.1.1',
        'idna==3.2',
        'itsdangerous==2.0.1',
        'lxml==4.6.3',
        'multitasking==0.0.9',
        'mypy-extensions==0.4.3',
        'numpy==1.21.1',
        'pandas==1.3.1',
        'pathspec==0.9.0',
        'python-dateutil==2.8.2',
        'pytz==2021.1',
        'PyYAML==5.4.1',
        'regex==2021.8.3',
        'requests==2.26.0',
        'requests-cache==0.7.2',
        'six==1.16.0',
        'SQLAlchemy==1.4.22',
        'tomli==1.2.1',
        'url-normalize==1.4.3',
        'urllib3==1.26.6',
        'yfinance==0.1.63'
    ],

    #keywords
    keywords='finance, us, equities, price, stockprice, api',

    #packages to include
    packages=find_packages(include=['price_data_db']),

    #classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],

    #required python version
    python_requires='>3.8.6'

)
