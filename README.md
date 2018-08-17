catchpycli
==========


python  client library for [catchpy][catchpy_repo] [rest api][catchpy_api]


install
--------

`catchpycli` requires that the catchpy project be installed in your
virtual enviroment. Have `catchpy` and `catchpycli` at the same directory level
and install both from source in your virtualenv

    $> git clone https://github.com/nmaekawa/catchpy.git
    $> git clone https://github.com/nmaekawa/catchpycli.git
    $> source PATH_TO_VIRTUALENV/bin/activate
    [VENV] $> cd catchpy; pip install catchpy/requirements/dev.txt
    [VENV] $> cd catchpy; pip install -e .
    [VENV] $> cd ../catchpycli; pip install requirements/dev.txt
    [VENV] $> cd ../catchpycli; pip install -e .



cli
----

This client comes with a command line interface to perform a simple test the
catchpy crud api. The cli needs a dotenv file to configure catchpy django app.

Check what the dotenv file looks like in `catchpycli/dotenvfile_example.env`.
Note that the only relevant env var is `DJANGO_SETTINGS_MODULE`, the other vars
just need to be defined but are not used by catchpycli.

To check how to use the command line client do:

    [VENV] $> cd catchpycli
    [VENV] $> CATCHPY_DOTENV_PATH=./dotenvfile_example.env catchpycli --help


license
-------

catchpy is licensed under Apache 2.0 license


Credits
---------

This package was created with [Cookiecutter][cookiecutter] and the
[`audreyr/cookiecutter-pypackage` project template][cookiecutter_pypackage].



[catchpy_repo]: https://github.com/nmaekawa/catchpy
[catchpy_api]:
https://github.com/nmaekawa/catchpy/blob/master/anno/static/anno/catch_api.json
[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter_pypackage]: https://github.com/audreyr/cookiecutter-pypackage
