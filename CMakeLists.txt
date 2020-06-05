cmake_minimum_required(VERSION 3.17.2)
include(${CMAKE_ROOT}/Modules/ExternalProject.cmake)

ExternalProject_Add(project_popup
		URL https://github.com/Chakshita04/rpm/blob/master/rpmbuild/SOURCES/popup-1.0.0-1.tar.gz

PREFIX ${CMAKE_CURRENT_BINARY_DIR}/popup-1.0.0-1
 CONFIGURE_COMMAND ""
 BUILD_COMMAND make
 INSTALL_COMMAND make install
 PREFIX=${CMAKE_CURRENT_BINARY_DIR}/popup-1.0.0-1
  )

  ExternalProject_Get_Property(project_popup install_dir)
#add_library(popup STATIC IMPORTED)
#set_property(TARGET build PROPERTY IMPORTED_LOCATION ${install_dir}/lib/libluajit-5.1.a)
#add_dependencies(popup project_popup)
add_executable(pop main.c)
#include_directories(${install_dir}/include/popup-1.0.0-1)
#target_link_libraries(pop popup)

#//////////////////////////////////////////////////////////////

project(pop)
configure_file(
       "${PROJECT_SOURCE_DIR}/test/bundle.h"

	"${PROJECT_BINARY_DIR}/test/bundle.h"
	
	)

include_directories("$PROJECT_BINARY_DIR}")
include_directories("${PROJECT_SOURCE_DIR}/popup")
add_library(pops main.c)
add_executable(cmake-good  main.c)
target_link_libraries(cmake-good PRIVATE popup)

include_directories(test)
install(TARGETS pop DESTINATION bin)
install(FILES bundle.h DESTINATION test)


