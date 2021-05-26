"""Snakemake wrapper for `dammit rename-transcriptome` subcommand"""

__author__    = "Camille Scott"
__copyright__ = "Copyright 2019, Camille Scott"
__email__     = "cswel@ucdavis.edu"
__license__   = "MIT"

import os

from snakemake.shell import shell

if not hasattr(snakemake.output, 'fasta'):
    raise ValueError('Must specifiy a `fasta` output variable.')
if not hasattr(snakemake.output, 'names'):
    raise ValueError('Must specifiy a `names` output variable.')

opts = []

if snakemake.params.get('basename', False):
    opts.extend(['--basename', snakemake.params.get('basename')])

if snakemake.params.get('split_regex', False):
    opts.extend(['--split-regex', '"{0}"'.format(snakemake.params.get('split_regex'))])

if snakemake.params.get('fail_on_repeats', False):
    opts.append('--fail-on-repeats')

opts.extend([str(snakemake.input), snakemake.output.fasta, snakemake.output.names])

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
opts = ' '.join(opts)

shell('dammit rename-fasta {opts} {log}')
