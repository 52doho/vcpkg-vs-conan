#/usr/bin/bash

[ -d build ] || mkdir build
cd build
conan install ..
cmake ..
make -j 6

echo ""
echo "------> build success and running:"
./ConanVCpkgDemo
