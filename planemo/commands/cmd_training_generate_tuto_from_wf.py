"""Module describing the planemo ``training_generate_tuto_from_wf`` command."""

import click

from planemo import options
from planemo import training
from planemo.cli import command_function


@click.command('training_generate_tuto_from_wf')
@options.optional_tools_arg(multiple=True, allow_uris=True)
@options.training_generate_tuto_from_wf_options()
@options.galaxy_serve_options()
@command_function
def cli(ctx, uris, **kwds):
    """Create tutorial skeleton from workflow."""
    kwds["no_dependency_resolution"] = True
    training.generate_tuto_from_wf(ctx, kwds)
