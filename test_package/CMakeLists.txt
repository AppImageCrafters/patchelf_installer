cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
