add_executable(tests_stitch)

target_sources(tests_stitch PRIVATE
  test_ops.cpp
)

set_target_warnings(tests_stitch) 
target_include_directories(tests_stitch PRIVATE . ../src ${CMAKE_BUILD_DIR}/_deps/catch2-src/src)

target_link_libraries(tests_stitch
  PRIVATE
  stitch
  Catch2::Catch2WithMain
)

install(TARGETS tests_stitch
  RUNTIME DESTINATION ${CMAKE_SOURCE_DIR}/bin
  LIBRARY DESTINATION ${CMAKE_SOURCE_DIR}/bin
  ARCHIVE DESTINATION ${CMAKE_SOURCE_DIR}/bin
)
