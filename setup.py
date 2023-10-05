from setuptools import find_packages

setup(
    name="analysis_service",
    version="1.0.0",
    description="My Python Project",
    author="Anton Omelchenko",
    author_email="omelchenko230783@gmail.com",
    license="MIT",
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "analysis_service=src:main"
        ]
    },
    install_requires = ['markdown']
)
