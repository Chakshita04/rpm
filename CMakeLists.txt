
cmake_minimum_required(VERSION 2.8)
project(app_project)
add_executable(myapp main.c)
#add_library( bundle.h)
install(TARGETS myapp DESTINATION bin)



