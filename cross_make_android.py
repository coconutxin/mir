# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shutil

ANDROID_NDK = ""

def call(cmd):
    returnCode = subprocess.call(cmd, shell=True)
    if returnCode != 0:
        print(returnCode)
        os.system("color c")
        sys.exit(returnCode)

def main():

    ANDROID_NDK = "D:/Android/android-ndk-r22"
    if not os.path.exists(ANDROID_NDK):
        ANDROID_NDK = "D:/Android/android-ndk-r16b"
    if not os.path.exists(ANDROID_NDK):
        ANDROID_NDK = "C:/Android/android-ndk-r22"

    cur_path = os.path.dirname(os.path.abspath(__file__)) + "/"

    ninja_path = cur_path + "ninja/ninja.exe"
    DCMAKE_TOOLCHAIN_FILE = ANDROID_NDK + "/build/cmake/android.toolchain.cmake"

    publish = "-DCOC_PUBLISH=OFF"

    #build armv7
    if not os.path.exists("build_android_v7a"):
        os.makedirs("build_android_v7a")

    os.chdir(cur_path + "build_android_v7a")

    call("cmake -DANDROID_ABI=armeabi-v7a -DCMAKE_TOOLCHAIN_FILE=%s -DANDROID_NDK=%s -DCMAKE_MAKE_PROGRAM=%s -DCMAKE_GENERATOR=Ninja -DANDROID_NATIVE_API_LEVEL=android-21 -DCMAKE_BUILD_TYPE=Release %s .." %
         (DCMAKE_TOOLCHAIN_FILE, ANDROID_NDK, ninja_path, publish))
    call(ninja_path)

    #build arm64
    os.chdir(cur_path)

    if not os.path.exists("build_android_arm64"):
        os.makedirs("build_android_arm64")

    os.chdir(cur_path + "build_android_arm64")

    call("cmake -DANDROID_ABI=arm64-v8a -DCMAKE_TOOLCHAIN_FILE=%s -DANDROID_NDK=%s -DCMAKE_MAKE_PROGRAM=%s -DCMAKE_GENERATOR=Ninja -DANDROID_NATIVE_API_LEVEL=android-21 -DCMAKE_BUILD_TYPE=Release %s .." %
         (DCMAKE_TOOLCHAIN_FILE, ANDROID_NDK, ninja_path, publish))
    call(ninja_path)

    os.system('pause')

if __name__ == '__main__':
    main()
