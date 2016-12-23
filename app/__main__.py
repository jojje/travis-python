import click
from .version import VERSION


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(version=VERSION, message='%(version)s')
@click.option('-v', '--verbose', default=False, is_flag=True, help='Show verbose information')
@click.pass_context
def main(ctx, verbose):
    """
    Program synopsis
    """
    ctx.obj['VERBOSE'] = verbose


@main.command(help='Does something')
@click.argument('arg')
@click.pass_context
def subcmd(ctx, arg):
    """
    Sub command synopsis
    """
    print('Doing thing with {}, verbose: {}'.format(arg, ctx.obj['VERBOSE']))


if __name__ == '__main__':
    main(obj={})
