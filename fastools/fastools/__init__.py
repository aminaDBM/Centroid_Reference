"""
fastools: Various tools for the analysis and manipulation of FASTA/FASTQ files.

"""
__version_info__ = ('0', '14', '1')

__version__ = '.'.join(__version_info__)
__author__ = 'LUMC, Jeroen F.J. Laros'
__contact__ = 'J.F.J.Laros@lumc.nl'
__homepage__ = 'https://git.lumc.nl/j.f.j.laros/fastools'

usage = __doc__.split("\n\n\n")


def doc_split(func):
    return func.__doc__.split("\n\n")[0]


def version(name):
    return "%s version %s\n\nAuthor   : %s <%s>\nHomepage : %s" % (name,
        __version__, __author__, __contact__, __homepage__)
