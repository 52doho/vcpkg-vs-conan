#include <iostream>

#include <glog/logging.h>
#include <cpprest/version.h>
#include <opencv2/core/version.hpp>
#include <faiss/Index.h>

int main(int argc, char **argv) {
    google::SetStderrLogging(google::INFO);
    google::InitGoogleLogging(argv[0]);

    LOG(INFO) << "from glog";
    LOG(INFO) << "cpprest version: " << CPPREST_VERSION;
    LOG(INFO) << "opencv version: " << CV_VERSION;
    LOG(INFO) << "faiss version: " << FAISS_VERSION_MAJOR << "." << FAISS_VERSION_MINOR << "." << FAISS_VERSION_PATCH;

    return 0;
}