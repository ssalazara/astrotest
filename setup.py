#!/usr/bin/env python
from distutils.core import setup
import setuptools
import astrotest

setup(
    name='astrotest',
    version='0.0.1',
    description="Library test that creates light curves embeddings using ASTROMER",
    #long_description=long_description,
    #long_description_content_type='text/markdown',
    author="Simon Salazar",
    author_email='ssalazara@udec.cl',
    url='https://github.com/ssalazara/Tutorial_libreria_python',


    packages=[
        'Tutorial_libreria_python'
    ],
    package_dir={
        'Tutorial_libreria_python': 'astrotest'
    },

    
    include_package_data=True,
    install_requires= ['tensorflow>=2.6', 'joblib', 'pytest', 'numpy', 'pandas', 'tqdm', 'seaborn', 'scipy'],
    license="MIT",
    zip_safe=False,
    keywords='astro-test',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
        
    ],
    #test_suite='tests',
    #tests_require=test_requirements
)
