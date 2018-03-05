# -*- coding: utf-8 -*-
"""
~~~~~~~~~~~~~~~~~~~~~~~
kiwivm partial api cli.


:auther vici: heyuhuade@gamil.com

"""

import click
import requests
import yaml
import json


@click.group()
@click.option('--api_key', '-a', help='kvm api token.')
@click.option('--veid', '-v', help='vm id.')
@click.option('--list', '-l', is_flag=True)
@click.pass_context
def cli(ctx, api_key, veid, list):
    if list:
        click.echo(yaml.safe_dump(KvmApi.api_map, default_flow_style=False))
    else:
        ctx.obj['api_box'] = KvmApi(api_key, veid)


@cli.command('info', help='Get vm info.')
@click.pass_context
def get_info(ctx):
    click.echo(ctx.obj['api_box'].get_info())


@cli.command('migrate', help='Get vm ipc locations.')
@click.pass_context
def get_migrate(ctx):
    click.echo(ctx.obj['api_box'].get_migrate_locations())


@cli.command('migrate_start', help='move vm to a new ipc')
@click.argument('location')
@click.pass_context
def migrate_start(ctx, location):
    click.echo(ctx.obj['api_box'].migrate_start(location))


class KvmApi:

    base_url = "https://api.64clouds.com/v1/"
    api_map = {
        'info',
        'migrate',
        'migrate_start',
    }

    def __init__(self, api_key, veid):
        self.api_key = api_key
        self.veid = veid

    def get_info(self):
        """获取vm相信信息
        get information about service
        :return: json
        """

        api = 'getServiceInfo'
        return self._base_request(api)

    def migrate_start(self, location):
        """迁移vm到新机房， 该操作会释放当前vm的ip地址群，同时释放dns绑定。

        """
        api = 'migrate/start'
        return self._base_request(api, location=location)

    def get_migrate_locations(self):
        api = 'migrate/getLocations'
        return self._base_request(api)

    def _base_request(self, api, **kwargs):
        """

        :param api: api name
        :type api: str
        :param kwargs: extract params
        :return:
        """

        url = ''.join((self.base_url, api))
        params = kwargs
        params['api_key'] = self.api_key
        params['veid'] = self.veid
        r = requests.get(url, params=params)
        return yaml.safe_dump(json.loads(r.content), default_flow_style=False)


if __name__ == '__main__':
    cli(obj={})
