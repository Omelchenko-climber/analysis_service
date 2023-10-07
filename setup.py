from setuptools import setup, find_namespace_packages

setup(
    name="analysis_service",
    version="1.0.0",
    description="This service can analyse folders with logs.",
    url='https://github.com/Omelchenko-climber/analysis_service',
    author="Anton Omelchenko",
    author_email="omelchenko230783@gmail.com",
    license="MIT",
    entry_points={
        "console_scripts": [
            "analysis_service=src:main"
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=['markdown']
)
