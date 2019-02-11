#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, urllib, imghdr
from PIL import Image
from gi.repository import GObject, Nautilus

class Acimg(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def img_size(self, window, files):
        if len(files) != 1:
            return

        with Image.open(urllib.unquote(files[0].get_uri()[7:])) as img:
            width, height = img.size

        cmd = 'zenity --info --title="Sizes pictures" --text="{}"'.format(str(width) + "x" + str(height))
        subprocess.call(cmd, shell=True)
        return

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        isImage = imghdr.what(urllib.unquote(files[0].get_uri()[7:]))

        if isImage != 'jpeg' and isImage != 'png' and isImage != 'gif':
            return

        item = Nautilus.MenuItem(
            name="Acimg::ImageSizes",
            label="Sizes pictures",
            tip="Image sizes"
        )

        item.connect('activate', self.img_size, files)
        return [item]
