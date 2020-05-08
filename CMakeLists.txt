cmake_minimum_required(VERSION 3.5)
project(vcpkg-vs-conan)

set(CMAKE_CXX_STANDARD 11)

find_package(cpprestsdk CONFIG REQUIRED)
find_package(OpenCV CONFIG REQUIRED)
find_package(glog CONFIG REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME}
        cpprestsdk::cpprest
        ${OpenCV_LIBS}
        glog::glog
        )