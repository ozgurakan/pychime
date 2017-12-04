from setuptools import setup

setup(
    name='pychime',
    version='0.1',
    description='A library to use Amazon Chime Web Hooks',
    author='Oz Akan',
    author_email='oz@akan.me',
    url='https://github.com/ozgurakan/pychime',
    keywords=['rss', 'feed', 'aws', 'dynamodb'],
    classifiers=[],
    packages=['pychime'],
    install_requires=['requests', 'json'],
    python_requires='>=3',
)
