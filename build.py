from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager(username="uilianries")
    builder.add_common_builds(shared_option_name="zlib:shared", pure_c=True)
    filtered_builds = []
    for settings, options in builder.builds:
        if settings["compiler.version"] == "4.1" and settings["arch"] == "x86_64":
            filtered_builds.append([settings, options])
    builder.builds = filtered_builds
    builder.run()
