#!/usr/bin/env python
import sys, os

def options(opt):
    opt.load('g++')

def configure(cfg):
    cfg.load('g++')
    cfg.env.INCLUDES_GTEST = ['include', '.']
    cfg.env.LIB_GTEST      = ['pthread']

def build(bld):
    src = bld.path.get_src().ant_glob('src/*.cc')

    bld.stlib(
        target   = 'gtest',
        source   = src,
        use      = ['GTEST'],
        cxxflags = ['-Wall', '-Wextra'],
    )
