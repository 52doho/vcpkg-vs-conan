#include <iostream>

#include <glog/logging.h>
#include <cpprest/version.h>
#include <opencv2/core/version.hpp>

int main(int argc, char **argv) {
    google::SetStderrLogging(google::INFO);
    google::InitGoogleLogging(argv[0]);

    LOG(INFO) << "from glog";
    LOG(INFO) << "cpprest version: " << CPPREST_VERSION;
    LOG(INFO) << "opencv version: " << CV_VERSION;

    return 0;
}