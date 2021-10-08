## vcpkg vs. conan
|  | [vcpkg](https://github.com/microsoft/vcpkg) | [conan](https://github.com/conan-io/conan)
| ---- | --- | ---|
| organization | microsoft | conan.io
| platform | Linux, OSX, Windows | all: Linux, OSX, Windows, Solaris, FreeBSD, embedded and cross-compiling
| host packages | centralized | decentralized: Artifactory, Bintray, private
| build system | [CMake, MSBuild](https://github.com/microsoft/vcpkg/blob/master/docs/users/integration.md) | any: CMake, MSBuild, Makefiles, Meson, etc
| num. of library | ~1350 | ~560 [official unique libraries](https://github.com/conan-io/conan-center-index), 113,369 [Binary Packages Indexed](https://conan.io/center/) + github community
| different versions of library support | [yes](https://devblogs.microsoft.com/cppblog/take-control-of-your-vcpkg-dependencies-with-versioning-support/) using [version field in JSON manifest file](https://github.com/microsoft/vcpkg/blob/master/docs/users/manifests.md#version-fields) | yes
| link type | static ([extra works is required to build shared library](https://github.com/microsoft/vcpkg/blob/master/docs/examples/overlay-triplets-linux-dynamic.md)) | [static, shared](https://docs.conan.io/en/latest/using_packages/conanfile_txt.html#options)
| CMakeLists.txt | manually add include\ and link libraries | automatically
| missing library | 1. [open a feature issue](https://github.com/microsoft/vcpkg/issues)<br/>2. [create package and pull request](https://github.com/microsoft/vcpkg/pulls) | 1. [open a feature issue](https://github.com/conan-io/conan/issues)<br/> 2. [create package](https://docs.conan.io/en/latest/creating_packages.html)

## example
```
git clone https://github.com/52doho/vcpkg-vs-conan.git && \
cd vcpkg-vs-conan && \
./auto-build-run.sh
```

## Steps to use vcpkg
### 1. install vcpkg
#### Prerequisites
* Windows 10, 8.1, 7, Linux, or MacOS
* Visual Studio 2015 Update 3 or newer (on Windows)
* Git
* gcc >= 7 or equivalent clang (on Linux)
* Optional: CMake 3.12.4

#### build vcpkg
```
git clone https://github.com/Microsoft/vcpkg.git && \
cd vcpkg && \
./bootstrap-vcpkg.sh && \
./vcpkg integrate install
```
[be careful for building failed in centos](https://github.com/microsoft/vcpkg/issues/9955)

### 2. search & add library
```
./vcpkg search cpprestsdk
./vcpkg install cpprestsdk
```
(Only v2.10.16 is available. glog install failed in CentOS, success in Ubuntu)

### 3. update CMakeLists.txt
```
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
```

### 4. build
```
cmake .. -DCMAKE_TOOLCHAIN_FILE=/path/to/vcpkg/scripts/buildsystems/vcpkg.cmake && \
make
```

## Steps to use conan
### 1. install conan
#### CentOS
```
sudo yum install python36 python36-devel python36-setuptools && \
sudo easy_install-3.6 pip && \
sudo pip3 install conan
```

#### Ubuntu
```
sudo apt-get install python3.5 python3-pip && \
sudo pip3 install conan
```

### 1.1 add conan source
```
conan remote add conan-center https://conan.bintray.com
conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
conan remote add conan-transit https://conan-transit.bintray.com
conan remote add conan-community https://api.bintray.com/conan/conan-community/conan
conan remote add conan-camposs https://conan.campar.in.tum.de/api/conan/conan-camposs
conan remote add wheelfinder https://api.bintray.com/conan/wheelfinder/public-conan
conan remote add dbely https://api.bintray.com/conan/dbely/conan
conan remote add picoreti https://api.bintray.com/conan/picoreti/is
conan remote add is https://api.bintray.com/conan/labviros/is
conan remote add lasote https://api.bintray.com/conan/lasote/conan-repo
```

### 2. search & add library
```
conan search cpprestsdk
```

add configs in conanfile.txt file:
```
[requires]
cpprestsdk/2.10.13@bincrafters/stable
glog/0.4.0@bincrafters/stable
opencv/3.4.3@conan/stable
faiss/1.6.3@jdai/stable

[options]
*:shared=True
gflags:nothreads=False
gflags:fPIC=True
gflags:namespace=google

[imports]
#bin, *.dll -> ./src/bin
#lib, *.dylib* -> ./src/bin
#lib, *.so* -> ./src/bin

[generators]
cmake
```

### 3. update CMakeLists.txt
```
cmake_minimum_required(VERSION 3.5)
project(vcpkg-vs-conan)

set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(NO_OUTPUT_DIRS)

link_libraries(
    ${CONAN_LIBS}
)

add_executable(${PROJECT_NAME} main.cpp)
```

### 4. build
```
conan install .. && \
cmake .. && \
make
```

## creating conan package
checkout [official doc](https://docs.conan.io/en/latest/creating_packages.html)

a demo is included in ./custom-package/ folder.