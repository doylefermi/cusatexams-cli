from setuptools import setup

setup(name='cusatexams-api',
      version='1.0',
      description='API to scrape exam.cusat.ac.in',
      author='Doyle Fermi',
      author_email='doylefermi@gmail.com',
      url='https://github.com/doylefermi/cusatexams-cli',
      install_requires=['Flask>=0.7.2', 'MarkupSafe','requests'],
      )
