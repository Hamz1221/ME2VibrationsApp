from distutils.core import setup

setup(
    # Application name:
    name="ME2VibrationsApp",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Mohammed Islam Nasir",
    author_email="mohammed.islam-nasir17@imperial.ac.uk",

    # Packages
    packages=["apps"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "numpy",
        "dash",
        "plotly",
        "dash_core_components",
        "dash_html_components",
        "astroid",
        "Brotli",
        "certifi",
        "click",
        "colorama",
        "dash-bootstrap-components",
        "dash-renderer",
        "dash-table",
        "Flask-Compress",
        "future",
        "gunicorn",
        "isort",
        "itsdangerous",
        "Jinja2",
        "lazy-object-proxy",
        "MarkupSafe",
        "mccabe",
        "pandas",
        "pylint",
        "python-dateutil",
        "pytz",
        "retrying",
        "six",
        "toml",
        "typed-ast",
        "Werkzeug",
        "wincertstore",
        "wrapt",

    ],
)