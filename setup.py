import setuptools

setuptools.setup(
    name='temp',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
