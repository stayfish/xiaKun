from datetime import datetime


def import_succeeded(name: str, suffix='xiaKun'):
    time = datetime.now().strftime('%m-%d %H:%M:%S')
    str = '\033[32m{str}\033[0m'.format(str=time)
    str += (' [\033[34mDEBUG\033[0m]'
            ' \033[36mnonebot\033[0m'
            ' | Succeeded to import "'
            '\033[33m{module}\033[0m"').format(
        module=name)
    if suffix == 'xiaKun':
        str += ' | \033[36m{s}\033[0m'.format(s=suffix)
    print(str)


def run_in(name: str, suffix='xiaKun'):
    time = datetime.now().strftime('%m-%d %H:%M:%S')
    str = '\033[32m{str}\033[0m'.format(str=time)
    str += (' [\033[34mDEBUG\033[0m]'
            ' \033[36mnonebot\033[0m'
            ' | running in "'
            '\033[33m{func}\033[0m"').format(
        func=name)
    if suffix == 'xiaKun':
        str += ' | \033[36m{s}\033[0m'.format(s=suffix)
    print(str)
