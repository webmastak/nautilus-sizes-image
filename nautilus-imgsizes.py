#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
from PIL import Image
from gi.repository import Nautilus, GObject

class ColumnExtension(GObject.GObject, Nautilus.ColumnProvider, Nautilus.InfoProvider):
    def __init__(self):
        pass

    def get_columns(self):
        return (Nautilus.Column(
            name="NautilusPython::ImageResolution", 
            attribute="resolution", 
            label="Resolution", 
            description="Resolution picture"),)
     
    def update_file_info(self, file):
        if file.get_uri_scheme() != 'file':
            return

        filename = urllib.unquote(file.get_uri()[7:]) 
        with Image.open(filename) as img:
            width, height = img.size
                    
        file.add_string_attribute('resolution', str(width) + "x" + str(height))
        
