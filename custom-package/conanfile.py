#coding:utf-8

from conans import ConanFile, CMake, tools
import os

class FaissConan(ConanFile):
    name = "faiss"
    version = "1.6.3"
    url = "https://github.com/facebookresearch/faiss"
    license = "https://github.com/facebookresearch/faiss/blob/master/LICENSE"
    description = "A library for efficient similarity search and clustering of dense vectors."
    settings = "os", "compiler", "build_type", "arch"
    exports = "CMakeLists.txt", "lib*.cmake", "extract_includes.bat.in", "protoc.cmake", "tests.cmake", "change_dylib_names.sh"
    options = {"shared": [True, False], "without_cuda": [True, False], "cuda_path": "ANY", "cuda_arch": "ANY"}
    default_options = {'shared': True, 'without_cuda': True, "cuda_path": "/path/to/cuda-10.1", "cuda_arch": "-gencode=arch=compute_75,code=sm_75 -gencode=arch=compute_72,code=sm_72"}
    generators = "make"
    _source_subfolder = "faiss"

    def source(self):
        source_folder = "faiss-{0}".format(self.version)
        archive_name = "{0}.tar.gz".format(source_folder)
        tools.download("https://github.com/facebookresearch/faiss/archive/v{0}.tar.gz".format(self.version), archive_name)
        tools.untargz(archive_name)
        os.rename(source_folder, self._source_subfolder)

    def build(self):
        with tools.chdir(self._source_subfolder):
            self.run("chmod +x configure")

            args = []
            if self.options.without_cuda:
                args += ['--without-cuda']
            else:
                args += ['--with-cuda=' + self.options.cuda_path]
                args += ['--with-cuda-arch=' + self.options.cuda_arch]

            self.run("./configure %s" % (' '.join(args)))
            cpus = tools.cpu_count()
            self.run("make -j %s" % cpus)

    def package(self):
        self.copy("*.h", dst="include", keep_path=True)
        self.copy("*.hpp", dst="include", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)