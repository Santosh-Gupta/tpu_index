import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='TPUIndex',
    version='0.0.1',
    author='Text2Vec Team',
    author_email='',
    description='TPUIndex is a package for fast similarity search over large collections of high dimension vectors on TPUs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/srihari-humbarwadi/TPUIndex',
    packages=setuptools.find_packages(),
    install_requires=['tensorflow>=2.0.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
