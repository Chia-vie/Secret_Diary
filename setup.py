import setuptools
# read in required packages from requirements.txt
with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="SecretDiary",
    version="0.0.0",
    author='Christine Ackerl',
    author_email='ci.a@univie.ac.at',
    description='Ich weiß nicht.',
    long_description='''Ich weiß immer noch nicht.''',
    url="https://github.com/Chia-vie/Secret_Diary",
    license='BSD',
    keywords='encryption,...',
    packages=setuptools.find_packages(),
    package_data={},
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Everybody',
        'Topic :: Encryption ::',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',],
    install_requires=requirements,
    include_package_data=True
)