from setuptools import setup

setup(
    name='Flask-Boilerplate',
    version='1.0',
    packages=['cli'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        boilerplate=cli.cli:cli
    """,
)
