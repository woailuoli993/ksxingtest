# -*- coding: utf-8 -*-
# 今日身体抱恙，脑力不足。只能写点不用动脑子的代码了。

import click
import time

# CONTEXT_SETTINGS = dict(token_normalize_func=lambda x: x.lower())


# @click.command(context_settings=CONTEXT_SETTINGS)
@click.command()
@click.option('--eat')
def medicine(eat):
    click.echo(f'hello, {eat}.')
    # med_name = click.confirm('the medicine name:')
    med_name = click.prompt('the medicine name')
    if med_name != '1':
        print('you will burn up.')
    else:
        # delete all ablove
        click.clear()  # crl + l 清屏但是不删字符
        time.sleep(1)
        for i in range(10):
            click.echo(i)

        cursor_up_one = '\x1b[1A'
        erase_line = '\x1b[1J'
        print(cursor_up_one + erase_line + cursor_up_one)  # 删除当屏所有字符。


if __name__ == '__main__':
    medicine()




