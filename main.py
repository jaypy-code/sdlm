import os
from app.episode import Episode
import app.folders as folders
import app.files as files
import app.download as dl
import click


@click.group()
def cli():
    pass


def checkIsEpisode(ctx, param, value):
    if value[0:1] != 'E' and value[0:1] != 'e' and len(value) != 3:
        click.echo("Bad episode! It must be like E01")
        ctx.abort()
    else:
        return value


@click.command()
@click.option('--link', prompt="Your Serial link", help="HTTP URI serial link")
@click.option('--current', prompt="Current episode on link (Like: E01)", callback=checkIsEpisode, help="Witch episode of this like is?")
@click.option('--last', prompt="Last episode (Like: E10)", callback=checkIsEpisode, help="Witch episode of this serial is last episode?")
def add(link, current, last):
    episode = Episode(link, current, last)
    if episode.ok():
        links = episode.getLinks()
        path = files.create(links)
        folders.add(path)
        print("Download files created at", path)
        print("To start download all files try 'sdlm download'")
    else:
        click.echo("Wrong link/episode!")


def confirm(ctx, param, value):
    if not value:
        ctx.abort()


@click.command()
@click.option('-y', prompt="Are you sure?", is_flag=True, callback=confirm, expose_value=False)
def download():
    if files.exists():
        dl.start(files.getPath())
    else:
        print("Sorry but {0} file does not exists T_T".format(files.name))


cli.add_command(add)
cli.add_command(download)

if __name__ == '__main__':
    cli()
