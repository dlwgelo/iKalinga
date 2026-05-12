[app]
title = iKalinga Appointment System
package.name = ikalinga
package.domain = org.ikalinga
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,requests,certifi,plyer,pydub,setuptools,pytz,python-dateutil
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.sdk = 31
android.accept_sdk_license = True
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,ACCESS_FINE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
