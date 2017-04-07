import os
import click

cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')
cmd_prefix = 'cmd_'


class AliasedMC(click.MultiCommand):
    def list_commands(self, ctx):
        # Get a list of all the availabe commands
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith(cmd_prefix):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        # Get a command by looing up the module
        ns = {}
        fn = os.path.join(cmd_folder, cmd_prefix + name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


@click.command(cls=AliasedMC)
def cli():
    pass
