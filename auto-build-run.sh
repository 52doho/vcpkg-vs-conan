#/usr/bin/bash

echo "------> install custom library faiss"
cd custom-package
./install-all.sh
cd ..

echo "------> build"
[ -d build ] || mkdir build
cd build
conan install ..
cmake ..
make -j 6

echo ""
echo "------> running"
./ConanVCpkgDemo
