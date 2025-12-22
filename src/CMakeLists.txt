add_library(stitch SHARED)

target_sources(stitch PRIVATE
  ops.hpp ops.cpp
)

set_target_warnings(stitch) 
target_include_directories(stitch PRIVATE .)

install(TARGETS stitch
  RUNTIME DESTINATION ${CMAKE_SOURCE_DIR}/bin
  LIBRARY DESTINATION ${CMAKE_SOURCE_DIR}/bin
  ARCHIVE DESTINATION ${CMAKE_SOURCE_DIR}/bin
)
