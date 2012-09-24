#!/usr/bin/env python
import sys, os

def options(opt):
    opt.load('g++')

def configure(cfg):
    cfg.load('g++')
    cfg.env.INCLUDES_GTEST = ['include', '.']
    cfg.env.LIB_GTEST      = ['pthread']

def build(bld):
    bld.stlib(
        target   = 'gtest',
        source   = bld.path.ant_glob('src/*.cc'),
        use      = ['GTEST'],
        cxxflags = ['-Wall', '-Wextra'],
    )
