# -*- coding: utf-8 -*-
import os

# featureimages 图片名称格式

# path = '/data/Documents/pycharm-workspace/xzhou-amszaure.github.io/themes/matery/source/medias/featureimages'
import sys

media_dirs = {
    'banner': './banner/',
    'feature': './featureimages/'
}

media_names = {
    'banner': '- /medias/banner/',
    'feature': '- /medias/featureimages/'
}


def print_list(dir_name):
    img_path = media_dirs[dir_name]

    if img_path is not None:
        files = sorted(os.listdir(img_path), key=lambda x: int(x.split('.')[0]))
        # print(files)
    else:
        files = None
        print('[`path` is None, invalid input!]')

    names_prefix = media_names[dir_name]

    for item in files:
        if files is not None:
            media_name = names_prefix + item
            print(media_name)
        else:
            print('[`files` is None, invalid input!]')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        err_msg = u'[Error]:[no directory specified!]\n' \
                  u'  Available directories:\n' \
                  u'  "b" or "banner": /medias/banner\n' \
                  u'  "f" or "feature": /medias/banner\n'
        print(err_msg)
    else:
        if sys.argv[1].lower() in ['b',  'banner', 'bannerimages']:
            print_list('banner')
        elif sys.argv[1].lower() in ['f', 'feature', 'featureimages']:
            print_list('feature')
    pass
