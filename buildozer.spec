[app]
title = Ambatukam Virus
package.name = ambatukamvirus
package.domain = org.ambatukam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0
requirements = python3,pygame
orientation = all
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
