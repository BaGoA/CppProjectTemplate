cmake_minimum_required(VERSION 3.20.0)

project(stitch
  VERSION 0.1.0
  DESCRIPTION ""
  LANGUAGES CXX
)

include(cmake/CompilerWarnings.cmake)
include(cmake/FetchDependencies.cmake)

add_subdirectory(src)
add_subdirectory(test)
