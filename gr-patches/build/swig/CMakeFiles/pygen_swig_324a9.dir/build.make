# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jspark/git/workspace/gr-patches

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jspark/git/workspace/gr-patches/build

# Utility rule file for pygen_swig_324a9.

# Include the progress variables for this target.
include swig/CMakeFiles/pygen_swig_324a9.dir/progress.make

swig/CMakeFiles/pygen_swig_324a9: swig/patches_swig.pyc
swig/CMakeFiles/pygen_swig_324a9: swig/patches_swig.pyo

swig/patches_swig.pyc: swig/patches_swig.py
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jspark/git/workspace/gr-patches/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating patches_swig.pyc"
	cd /home/jspark/git/workspace/gr-patches/build/swig && /usr/bin/python /home/jspark/git/workspace/gr-patches/build/python_compile_helper.py /home/jspark/git/workspace/gr-patches/build/swig/patches_swig.py /home/jspark/git/workspace/gr-patches/build/swig/patches_swig.pyc

swig/patches_swig.pyo: swig/patches_swig.py
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jspark/git/workspace/gr-patches/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating patches_swig.pyo"
	cd /home/jspark/git/workspace/gr-patches/build/swig && /usr/bin/python -O /home/jspark/git/workspace/gr-patches/build/python_compile_helper.py /home/jspark/git/workspace/gr-patches/build/swig/patches_swig.py /home/jspark/git/workspace/gr-patches/build/swig/patches_swig.pyo

swig/patches_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gnuradio.i
swig/patches_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_extras.i
swig/patches_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_shared_ptr.i
swig/patches_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gnuradio_swig_bug_workaround.h
swig/patches_swigPYTHON_wrap.cxx: ../swig/patches_swig.i
swig/patches_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_types.i
swig/patches_swigPYTHON_wrap.cxx: swig/patches_swig.tag
swig/patches_swigPYTHON_wrap.cxx: ../swig/patches_swig.i
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jspark/git/workspace/gr-patches/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Swig source"
	cd /home/jspark/git/workspace/gr-patches/build/swig && /usr/bin/cmake -E make_directory /home/jspark/git/workspace/gr-patches/build/swig
	cd /home/jspark/git/workspace/gr-patches/build/swig && /usr/bin/swig2.0 -python -fvirtual -modern -keyword -w511 -module patches_swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -I/home/jspark/git/workspace/gr-patches/swig -I/home/jspark/git/workspace/gr-patches/build/swig -outdir /home/jspark/git/workspace/gr-patches/build/swig -c++ -I/home/jspark/git/workspace/gr-patches/lib -I/home/jspark/git/workspace/gr-patches/include -I/home/jspark/git/workspace/gr-patches/build/lib -I/home/jspark/git/workspace/gr-patches/build/include -I/usr/include -I/usr/local/include -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/home/jspark/git/workspace/gr-patches/swig -I/home/jspark/git/workspace/gr-patches/build/swig -o /home/jspark/git/workspace/gr-patches/build/swig/patches_swigPYTHON_wrap.cxx /home/jspark/git/workspace/gr-patches/swig/patches_swig.i

swig/patches_swig.py: swig/patches_swigPYTHON_wrap.cxx

swig/patches_swig.tag: swig/patches_swig_doc.i
swig/patches_swig.tag: swig/_patches_swig_swig_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jspark/git/workspace/gr-patches/build/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating patches_swig.tag"
	cd /home/jspark/git/workspace/gr-patches/build/swig && ./_patches_swig_swig_tag
	cd /home/jspark/git/workspace/gr-patches/build/swig && /usr/bin/cmake -E touch /home/jspark/git/workspace/gr-patches/build/swig/patches_swig.tag

swig/patches_swig_doc.i: swig/patches_swig_doc_swig_docs/xml/index.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jspark/git/workspace/gr-patches/build/CMakeFiles $(CMAKE_PROGRESS_5)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating patches_swig_doc.i"
	cd /home/jspark/git/workspace/gr-patches/docs/doxygen && /usr/bin/python -B /home/jspark/git/workspace/gr-patches/docs/doxygen/swig_doc.py /home/jspark/git/workspace/gr-patches/build/swig/patches_swig_doc_swig_docs/xml /home/jspark/git/workspace/gr-patches/build/swig/patches_swig_doc.i

swig/patches_swig_doc_swig_docs/xml/index.xml: swig/_patches_swig_doc_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jspark/git/workspace/gr-patches/build/CMakeFiles $(CMAKE_PROGRESS_6)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating doxygen xml for patches_swig_doc docs"
	cd /home/jspark/git/workspace/gr-patches/build/swig && ./_patches_swig_doc_tag
	cd /home/jspark/git/workspace/gr-patches/build/swig && /usr/bin/doxygen /home/jspark/git/workspace/gr-patches/build/swig/patches_swig_doc_swig_docs/Doxyfile

pygen_swig_324a9: swig/CMakeFiles/pygen_swig_324a9
pygen_swig_324a9: swig/patches_swig.pyc
pygen_swig_324a9: swig/patches_swig.pyo
pygen_swig_324a9: swig/patches_swigPYTHON_wrap.cxx
pygen_swig_324a9: swig/patches_swig.py
pygen_swig_324a9: swig/patches_swig.tag
pygen_swig_324a9: swig/patches_swig_doc.i
pygen_swig_324a9: swig/patches_swig_doc_swig_docs/xml/index.xml
pygen_swig_324a9: swig/CMakeFiles/pygen_swig_324a9.dir/build.make
.PHONY : pygen_swig_324a9

# Rule to build all files generated by this target.
swig/CMakeFiles/pygen_swig_324a9.dir/build: pygen_swig_324a9
.PHONY : swig/CMakeFiles/pygen_swig_324a9.dir/build

swig/CMakeFiles/pygen_swig_324a9.dir/clean:
	cd /home/jspark/git/workspace/gr-patches/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/pygen_swig_324a9.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/pygen_swig_324a9.dir/clean

swig/CMakeFiles/pygen_swig_324a9.dir/depend:
	cd /home/jspark/git/workspace/gr-patches/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jspark/git/workspace/gr-patches /home/jspark/git/workspace/gr-patches/swig /home/jspark/git/workspace/gr-patches/build /home/jspark/git/workspace/gr-patches/build/swig /home/jspark/git/workspace/gr-patches/build/swig/CMakeFiles/pygen_swig_324a9.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/pygen_swig_324a9.dir/depend

