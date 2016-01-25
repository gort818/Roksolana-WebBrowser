#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, WebKit
import os, sys

class Browser:
  def __init__(self):
    self.builder = Gtk.Builder()
   
    self.builder.add_from_file("roksolana.glade")
    self.builder.connect_signals(self)

    self.toolbar1 = self.builder.get_object("toolbar1")
    self.back = self.builder.get_object("back")
    self.forward = self.builder.get_object("forward")
    self.refresh = self.builder.get_object("refresh")
    self.stop = self.builder.get_object("stop")
    self.url = self.builder.get_object("url")
    self.window = self.builder.get_object("window1")
    self.window.connect('destroy', lambda w: Gtk.main_quit())
    self.scrolledwindow = self.builder.get_object("scrolledwindow")
    self.window.show_all()

    self.webview = WebKit.WebView()
    self.scrolledwindow.add(self.webview)
    self.webview.open('http://google.com')
    self.webview.connect('title-changed', self.change_title)
    self.webview.connect('load-committed', self.change_url)
    self.webview.show()	

  
  def on_url_activate(self, widget):
        url = widget.get_text()
        if url.startswith('http://') or url.startswith('https://'):
            self.webview.open(url)
        else:
            url = 'http://' + url
            self.url.set_text(url)
            self.webview.open(url)


  def on_refresh_clicked(self, widget):
    self.webview.reload()

  def on_back_clicked(self, widget):
    self.webview.go_back()
  def on_forward_clicked(self, widget):
     self.webview.go_forward()
  def on_stop_clicked(self, widget):
     self.webview.stop_loading()

  def change_title(self, widget, frame, title):
     self.window.set_title('Roksolana Browser    |     ' + title)
  def change_url(self, widget, frame):
     uri = frame.get_uri()
     self.url.set_text(uri)
  
  

def main ():
  app = Browser()
  Gtk.main()

if __name__ == "__main__":
  main()
