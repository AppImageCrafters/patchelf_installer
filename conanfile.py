from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
import os

class PatchelfinstallerConan(ConanFile):
    name = "patchelf_installer"
    version = "0.10"
    license = "GPL v3.0"
    author = "Alexis Lopez Zubieta contact@azubieta.net"
    url = "https://github.com/appimage-conan-community/patchelf_installer"
    description = "A small utility to modify the dynamic linker and RPATH of ELF executables"
    topics = ("utility", "elf")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/NixOS/patchelf.git -b 0.10")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        with tools.environment_append(env_build.vars):
            self.run("cd patchelf && ./bootstrap.sh")
            self.run("cd patchelf && ./configure --prefix=/");
            self.run("cd patchelf && make && DESTDIR=%s make install" % self.package_folder)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def deploy(self):
        self.copy("*", dst="bin", src="bin")
