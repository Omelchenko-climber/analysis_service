from setuptools import setup

setup(
    name="analysis_service",
    version="2.1.0",
    description="This service can analyse folders with logs.",
    url='https://github.com/Omelchenko-climber/analysis_service',
    author="Anton Omelchenko",
    packages=[
        'src',
        'src.data',
        'src.utils',
    ],
    install_requires=[
        'certifi>=2023.7',
        'charset-normalizer>=3.3',
        'idna==3.4',
        'requests>=2.31',
        'urllib3>=2.0'
    ],
    author_email="omelchenko230783@gmail.com",
    license="MIT",
    entry_points={
        "console_scripts": [
            "analysis-service=src.main:run"
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
