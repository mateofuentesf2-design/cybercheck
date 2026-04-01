from setuptools import setup, find_packages

setup(
    name='cybercheck',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'rich',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'cybercheck=cli:run'
        ]
    },

)