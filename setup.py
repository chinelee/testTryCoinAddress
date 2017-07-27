try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='testtcoaddr',
    version='1.0',
    description="Generate trycoin addresses.",
    author="chinelee",
    author_email='lclunyu100@gmail.com',
    url='https://github.com/chinelee/testTryCoinAddress',
    scripts=['testtcoaddr'],
    license='LICENSE',
)