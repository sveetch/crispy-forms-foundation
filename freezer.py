"""
A script to collect every installed dependencies versions from "pip freeze" but
only those ones explicitely required in package configuration.

It will create a "frozen.txt" file which can help users to find an exact list of
dependencies versions which have been tested.

This require a recent install of setuptools (>=39.1.0).

You must call this script with the same Python interpreter used in your virtual
environment.
"""
import subprocess
import sys

import pkg_resources


def flatten_requirement(requirement):
    """
    Return only the package name from a requirement.

    Arguments:
        requirement (pkg_resources.Requirement): A requirement object.

    Returns:
        string: Package name.
    """
    return requirement.key


def extract_pkg_version(package_name):
    """
    Get package version from installed distribution or configuration file if not
    installed

    Arguments:
        package_name (string): Package name to search and extract informations.

    Returns:
        string: Version name.
    """
    return pkg_resources.get_distribution(package_name).version


def extract_pkg_requirements(package_name):
    """
    Get all required dependency names from every requirement sections.

    Arguments:
        package_name (string): Package name to search and extract informations.

    Returns:
        list: A list of all required package names.
    """
    distrib = pkg_resources.get_distribution(package_name)

    requirements = set([])

    for r in distrib.requires():
        requirements.add(flatten_requirement(r))

    for item in distrib.extras:
        for r in distrib.requires(extras=(item,)):
            requirements.add(flatten_requirement(r))

    return list(requirements)


def get_install_dependencies(requirements=None, ignore=[]):
    """
    Use "pip freeze" command to get installed dependencies and possibly filtered
    them from a list of names.

    This does not support installed dependencies from a VCS or in editable mode.

    Keyword Arguments:
        requirements (list): List of package names to retain from installed
            dependencies. If not given, all installed dependencies are retained.
        ignore (list): List of package names to ignore from installed
            dependencies.

    Returns:
        list: List of installed dependencies with their version. Either all or
        only those ones from given ``names``.
    """
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])

    # Filter from requirement names (if any) and ignored ones
    deps = []
    for item in reqs.splitlines():
        pkg = item.decode('utf-8')
        name = pkg.split("==")[0].lower()

        if (
            (requirements is None or name in requirements) and
            name not in ignore
        ):
            deps.append(pkg)

    return deps


def write_frozen_requirements(package_name, filename="frozen.txt"):
    """
    Write a file of frozen requirement versions for current version of a
    package.
    """
    version = extract_pkg_version(package_name)
    requirements = extract_pkg_requirements(package_name)
    installed = get_install_dependencies(requirements)

    lines = [
        "# Frozen requirement versions from '{}' installation".format(version)
    ] + installed

    with open(filename, "w") as fp:
        fp.write("\n".join(lines))

    return filename


if __name__ == "__main__":
    filename = write_frozen_requirements("crispy-forms-foundation")
    print("Created file for frozen dependencies:", filename)
