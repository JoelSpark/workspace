#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jspark/git/workspace/gr-patches/python
export PATH=/home/jspark/git/workspace/gr-patches/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/jspark/git/workspace/gr-patches/build/swig:$PYTHONPATH
/usr/bin/python /home/jspark/git/workspace/gr-patches/python/qa_quadrature_demod.py 
