from setuptools import setup, find_packages


setup(
    name='gaia',
    version='0.0.3',

    url='https://github.com/Jorgelzn/Gaia',
    author='Jorge Lizcano',
    author_email='jorgelizgo@gmail.com',

    long_description_content_type='text/markdown',
    long_description=open('README.md').read().replace('<img src="gaia.jpg" alt="drawing" width="100"/>',''),

    packages=find_packages(include=['gaia']),

    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=4'],
    test_suite='tests'
)