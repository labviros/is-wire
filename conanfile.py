from conans import ConanFile, CMake, tools


class IsWireConan(ConanFile):
    name = "is-wire"
    version = "1.1.5"
    license = "MIT"
    url = "https://github.com/labviros/is-wire"
    description = "C++ implementation of the ::is messaging layer"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "build_tests": [True, False],
        "build_benchmarks": [True, False]
    }
    default_options = ("shared=True", "fPIC=True", "build_tests=False", "build_benchmarks=False")
    generators = "cmake", "cmake_find_package", "cmake_paths"
    requires = (
        "SimpleAmqpClient/2.5.0@is/stable",
        "spdlog/1.1.0@bincrafters/stable",
        "opentracing-cpp/1.4.0@is/stable",
        "prometheus-cpp/0.4.1@is/stable",
        "protobuf/3.6.1@bincrafters/stable",
        "protoc_installer/3.6.1@bincrafters/stable",
        "boost/1.66.0@conan/stable",
    )

    exports_sources = "*"

    def build_requirements(self):
        if self.options.build_benchmarks:
            self.build_requires("benchmark/1.4.1@is/stable")
        if self.options.build_tests:
            self.build_requires("gtest/[>=1.8]@bincrafters/stable")
            self.build_requires("zipkin-cpp-opentracing/0.3.1@is/stable")

    def configure(self):
        self.options["SimpleAmqpClient"].shared = self.options.shared 
        self.options["opentracing-cpp"].shared = self.options.shared 
        self.options["prometheus-cpp"].shared = self.options.shared 
        self.options["protobuf"].shared = self.options.shared 
        self.options["boost"].shared = self.options.shared 

    def build(self):
        cmake = CMake(self, generator='Ninja')
        if not self.options.shared:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["build_tests"] = self.options.build_tests
        cmake.definitions["build_benchmarks"] = self.options.build_benchmarks
        cmake.configure()
        cmake.build()
        if self.options.build_tests:
            cmake.test()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["is-wire-rpc", "is-wire-core"]
