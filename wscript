#!/usr/bin/env python
import sys, os

def options(opt):
    opt.load('compiler_cxx')

def configure(cfg):
    cfg.load('compiler_cxx')
    cfg.check_cxx(lib='pthread', cxxflags='-pthread')

def build(bld):
    bld.stlib(
        target          = 'gtest',
        source          = bld.path.ant_glob('src/*.cc'),
        use             = ['PTHREAD'],
        includes        = ['include', '.'],
        export_includes = ['include'],
        cxxflags        = ['-Wall', '-Wextra'],
    )
