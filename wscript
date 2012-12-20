#!/usr/bin/env python
import sys, os

def options(opt):
    opt.load('g++')

def configure(cfg):
    cfg.load('g++')
    cfg.env.LIB_PTHREAD = ['pthread']
    cfg.env.CXXFLAGS_PTHREAD = ['-pthread']

def build(bld):
    bld.stlib(
        target          = 'gtest',
        source          = bld.path.ant_glob('src/*.cc'),
        use             = ['PTHREAD'],
        includes        = ['include', '.'],
        export_includes = ['include'],
        cxxflags        = ['-Wall', '-Wextra'],
    )
