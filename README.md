**cusatexams-cli**  [![build status](https://gitlab.com/doylefermi/cusatexams-cli/badges/master/build.svg)](https://gitlab.com/doylefermi/cusatexams-cli/commits/master)
==============

**Todo**

- [x] Scrape from site
- [x] Prepare JSON response
- [ ] Create report card
- [ ] Custom GPA finder (for failed candidates)
- [ ] Easy the long commands

**Usage**

Clone the repo. Dive into the folder now.

> $ cd cusatexams-cli

Install *python3*. Use the virtual environment available. To do so first setup the [python virtual environment] in your host system.

> $ virtualenv -p /usr/bin/python3 venv –no-site-packages

Now issue the following to run the virtual environment:

> $ source venv/bin/activate

All packages installed via pip must be added to *setup.py*. Inorder to setup the environment and install any packages required run:

> $ pip install -e .

Install any additional packages using *pip* (Note: Packages will be installed in the virtual environment only):

> $ pip install &lt;package-name&gt;

Install application using (each time code is changed run this):

> $ python setup.py install

Run application using:

> $ cusatexams

All packages installed by *pip* can be listed using:

> $ pip freeze

After your work is done, exit from the virtual environment using the command:

> $ deactivate

  [python virtual environment]: http://docs.python-guide.org/en/latest/dev/virtualenvs/