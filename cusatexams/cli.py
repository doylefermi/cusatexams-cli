"""
cusatexams

Usage:
  cusatexams fetch <regno> <sem> <month> <year> <type>
  cusatexams report [-t] <regno> <start_year> <end_year> [--format=<format>] [--custom-gpa=<gpa>] [--semester=<sem>] 
  cusatexams batch <start_regno> <end_regno> <sem> <month> <year> <type>
  cusatexams -h | --help
  cusatexams --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -t --trimmed                      Display trimmed output.
  --custom-gpa=<gpa>                Set custom GPA even if GPA not obtained for that Sem. [Default: 5]
  --semester=<sem>                  Choose a semester. Accepts a string of semesters separated by space. See example. [Default: all]
  --format=<format>                 Output format (json|dict|none). [Default: none]
  <regno>                           CUSAT 8 digit register number [Eg: 12140834]
  <sem>                             Semester number [Eg: 3]
  <month>                           Month of exam [Eg: November]
  <year>                            Year of exam [Eg: 2014]
  <type>                            Type of exam [Eg: Regular, Revaluation, Supplementary, Improvement]

Examples:
  cusatexams fetch 12140834 3 November 2014 Regular
  cusatexams report 12140834 2014 2015 --custom-gpa=7 --sem="1&2 4 5"
  cusatexams report 12140834 2014 2016 --trimmed
  cusatexams batch 12140800 12140929 6 April 2016 Regular

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/doylefermi/cusatexams-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    from . import commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.items():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            try:
                command.run()
            except:
                print("Exited abnormally. Rerun task.")
            
