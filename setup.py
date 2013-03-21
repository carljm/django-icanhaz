from os.path import join, dirname
import sys

from setuptools import setup, find_packages

here = dirname(__file__)

long_description = (open(join(here, "README.rst")).read() + "\n\n" +
                    open(join(here, "CHANGES.rst")).read() + "\n\n" +
                    open(join(here, "TODO.rst")).read())

def get_version():
    fh = open(join(here, "icanhaz", "__init__.py"))
    try:
        for line in fh.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')
    finally:
        fh.close()

if sys.version_info[0] < 3:
    tests_require = ["Django>=1.2"]
else:
    # py3k is only supported in Django>=1.5
    tests_require = ["Django>=1.5"]

# mock is included in Python 3.3+
if sys.version_info < (3, 3):
    tests_require.append("mock")

setup(
    name="django-icanhaz",
    version=get_version(),
    description="A Django template tag for embedding ICanHaz.js templates safely.",
    long_description=long_description,
    author="Carl Meyer",
    author_email="carl@oddbird.net",
    url="https://github.com/carljm/django-icanhaz/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Framework :: Django",
    ],
    zip_safe=False,
    tests_require=tests_require,
    test_suite="runtests.runtests"
)
