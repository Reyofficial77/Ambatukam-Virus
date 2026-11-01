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
android.archs = arm64-v8a
android.accept_sdk_license = True
android.api = 30
android.minapi = 24
android.ndk = 25b
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
