from setuptools import setup, find_packages

setup(
    name="cybercheck",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "colorama",
        "fastapi",
        "uvicorn"
    ],
    entry_points={
        "console_scripts": [
            "cybercheck=cli:main_menu"
        ]
    },
)