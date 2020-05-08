#/usr/bin/bash

echo "------> creating conan package: faiss"
echo "[NOTE] openBlas is required: sudo apt-get install libopenblas-dev"
conan create conanfile.py jdai/stable --keep-source --build=missing -s build_type=Release
