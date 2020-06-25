try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import setuptools
config = {
    'description':'A script that creates a project directory and github repo.',
    'author':'Kristian',
    'url':'URL to get it at.',
    'download_url':'Where to download it.',
    'author_email':'kristian.roopnarine@gmail.com',
    'version':'0.1',
    'install_requires':['requests','python-decouple'],
    'packages':setuptools.find_packages(),
    'scripts':[],
    'name':'github-repo'
}

setup(**config)