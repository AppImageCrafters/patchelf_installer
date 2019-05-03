import os

from conans import ConanFile, CMake, tools


class PatchelfinstallerTestConan(ConanFile):
    build_requires = "cmake_installer/3.13.0@conan/stable"
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            self.run("patchelf --set-rpath testing ./example ", run_environment=True)
            self.run("patchelf --print-rpath ./example", run_environment=True)
