from adapters.cli import create_cli
from composites.consumer import MessageBus

if __name__ == '__main__':
    cli = create_cli(MessageBus)
    cli()
