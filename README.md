#cusatexams-cli [![Build Status](https://travis-ci.org/doylefermi/cusatexams-cli.svg?branch=master)](https://travis-ci.org/doylefermi/cusatexams-cli)

Command line utility for exam.cusat.ac.in
	
	Usage:
	  cusatexams fetch <regno> <sem> <month> <year> <type>
	  cusatexams -h | --help
	  cusatexams --version
	
	Options:
	  -h --help                         Show this screen.
	  --version                         Show version.
	  <regno>                           CUSAT 8 digit register number [Eg: 12140834]
	  <sem>                             Semester number [Eg: 3]
	  <month>                           Month of exam [Eg: November]
	  <year>                            Year of exam [Eg: 2014]
	  <type>                            Type of exam [Eg: Regular, Revaluation, Supplementary, Improvement]
	
	Examples:
	  cusatexams fetch 12140834 3 November 2014 Regular
	
	Help:
	  For help using this tool, please open an issue on the Github repository:
	  https://github.com/doylefermi/cusatexams-cli

##Development

>Note: Reduce pull requests to a single commit.

###Todo

- [x] Scrape from site
- [x] Prepare JSON response
- [ ] Create report card
- [ ] Custom GPA finder (for failed candidates)
- [ ] Easy the long commands
- [ ] Check for all exceptions

###Usage

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