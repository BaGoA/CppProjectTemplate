# CppProjectTemplate
CppProjectTemplate is C++ template project to create C++ libraries.

We can use it also to create an C++ application with few changes.

## Build
Build of CppProjectTemplate is made by [CMake](https://cmake.org/) with [Ninja](https://ninja-build.org/) build system via python script _bs.py_.

```console
python bs.py init debug
```
This command initialize the project by running cmake configure in _build/debug_ directory and generate the file _compile_commands.json_.

```console
python bs.py build debug
```
This command build the project by running cmake build in _build/debug_ directory following by cmake install in _bin_ directory.

## Test
Test of CppProjectTemplate is made by [Catch2](https://github.com/catchorg/Catch2).

We build an catch2 executable that manages the run of tests, please follow the executable's help if you want run specific test.
