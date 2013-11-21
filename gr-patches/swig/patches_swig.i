/* -*- c++ -*- */

#define PATCHES_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "patches_swig_doc.i"

%{
#include "patches/quadrature_demod.h"
%}


%include "patches/quadrature_demod.h"
GR_SWIG_BLOCK_MAGIC2(patches, quadrature_demod);
