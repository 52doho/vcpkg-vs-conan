cmake_minimum_required(VERSION 3.14)
project(ConanVCpkgDemo)

set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(NO_OUTPUT_DIRS)

link_libraries(
        ${CONAN_LIBS}
)

add_executable(${PROJECT_NAME} main.cpp)