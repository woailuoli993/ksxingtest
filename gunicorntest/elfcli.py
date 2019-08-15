#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click

from env import set_app_context_server


@click.group()
def cli():
    pass


@click.command()
def run():
    """run a elf script in elf environment"""
    pass


@click.command()
def serve():
    """run gunicorn app"""
    set_app_context_server()
    from wsgi import run_app
    print("start serve")
    run_app()


cli.add_command(serve)
cli.add_command(run)
