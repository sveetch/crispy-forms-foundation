"""
A portable script to get requirements with their installed versions.

Opposed to a ``pip freeze`` this only care about the direct dependencies, if you just
want the whole list of installed package versions use pip freeze.

It requires Python>=3.8 and 'packaging' library (which should already be installed on
a development environment).
"""
import subprocess
import sys
from collections import defaultdict
from importlib.metadata import (
    PackageNotFoundError, distribution, version as dist_version,
    requires as dist_requires
)
from pathlib import Path

from packaging.requirements import Requirement


class CollectorRequirementNotFoundError(ModuleNotFoundError):
    pass


class InstalledRequirementCollector:
    """
    Collect every requirement with their installed version number from a project.

    The project need to be installed as a package since it is informations are imported
    with ``importlib.metadata``.
    """
    def __init__(self, safe=False):
        self.safe = safe

    def get_requirement_extra(self, marker):
        """
        Get the 'extra' section from marker.

        Arguments:
            marker (packaging.markers.Marker):

        Return:
            string: The 'extra' section value if found else None.
        """
        if not marker:
            return None

        # Patch marker set so it can be splitted in items that we can search for the
        # 'extra' reference
        patched_marker = str(marker).replace(" and ", "/").replace(" or ", "/")
        for mark in patched_marker.split("/"):
            if mark.replace(" ", "").startswith("extra=="):
                return mark.replace(" ", "").replace("extra==", "").replace("\"", "")

        return None

    def parse_requirement(self, requirement):
        """
        Parse requirement string to get package name, version and possible 'extra'
        label.

        Arguments:
            requirement (string): Full requirement string to parse.

        Returns:
            tuple: In order the package name, the version and then the possible 'extra'
            section value.
        """
        req = Requirement(requirement)

        return (req.name, str(req.specifier), self.get_requirement_extra(req.marker))

    def distribution_requirements(self, main_package_name, ignore_pkg=None):
        """
        Get all required dependency names from every requirement sections from a package
        distribution.

        Arguments:
            main_package_name (string): Project package name.

        Keyword Arguments:
            ignore_pkg (list): List of package names to ignore from installed
                dependencies.

        Returns:
            dict: Dictionnary of requirements indexed on their extra label (or None for
                non extra requirements).
        """
        ignore_pkg = ignore_pkg or []
        requirements = defaultdict(list)
        found = dist_requires(main_package_name) or []

        for item in found:
            name, specifier, extra = self.parse_requirement(item)
            if name not in ignore_pkg:
                requirements[extra].append(name)

        return requirements

    def get_install_dependencies(self, requirements, safe=False):
        """
        Get project requirements installed to collect their useful metadata.

        All project requirements are required to be installed except those explicitely
        defined to ignore.

        This may not work well with installed dependencies from a VCS or in editable
        mode if they don't configure the proper package informations.

        Keyword Arguments:
            requirements (list): List of package names to retain from installed
                dependencies. If not given, all installed dependencies are retained.
            ignores (list): List of package names to ignore from installed
                dependencies.
            safe (boolean): If true, a required package that is not installed won't
                raise an exception, instead it will be just commented with a message.

        Returns:
            dict: A dictionnary created with ``collections.defaultdict`` for collected
                requirements indexed on their extra section name, the base requirements
                are stored in the ``None`` item.
        """
        registry = defaultdict(list)

        for extra_name, extra_reqs in requirements.items():
            for name in extra_reqs:
                try:
                    dependency_distrib = distribution(name)
                except PackageNotFoundError as e:
                    if self.safe:
                        registry[extra_name].append(
                            "# Defined but uninstalled package " + name
                        )
                    else:
                        msg = (
                            "Package '{}' is defined in requirements but not "
                            "installed. You should only load this script with all "
                            "defined requirements installed."
                        )
                        raise CollectorRequirementNotFoundError(msg.format(name))
                else:
                    registry[extra_name].append(
                        name + "==" + dependency_distrib.metadata["Version"]
                    )

        return registry

    def collect(self, name, destination=None, safe=False, ignore_pkg=None):
        """
        Get the installed project requirements structured by their 'extra' section and
        build a file to list them.

        Arguments:
            name (string): Project package name to collect its requirements.

        Keyword Arguments:
            destination (Path): A path object to a file where to write collected
                content. If targetted file already exists it will be overwritten. If
                this argument value is empty, the requirement file content will just
                be printed to standard output.
            ignore_pkg (list): List of package names to ignore from installed
                dependencies.

        Returns:
            dict: A dictionnary created with ``collections.defaultdict`` for collected
                requirements indexed on their extra section name, the base requirements
                are stored in the ``None`` item.
        """
        requirements = self.distribution_requirements(name, ignore_pkg=ignore_pkg)
        registry = collector.get_install_dependencies(requirements)

        lines = [
            "# Frozen requirement versions for '{name}=={version}' installation".format(
                name=name,
                version=dist_version(name),
            )
        ]

        for extra_name, extra_reqs in registry.items():
            if extra_name:
                lines.append("# From extra requirements '{}'".format(extra_name))

            for name in extra_reqs:
                lines.append(name)

        content = "\n".join(lines)

        if destination:
            destination.write_text(content)
            print("Frozen requirements written to:", destination)
        else:
            print(content)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Build a requirements file for project requirements with their locally "
            "installed versions. Project must have been installed as a package since "
            "it is imported to get some needed informations. Opposed to a 'pip freeze' "
            "this will only care about explicitely defined project requirements and "
            "not about all installed packages."
        ),
    )
    parser.add_argument(
        "package_name",
        default=None,
        help=(
            "Name of an installed package, it can be your project package or any "
            "other installed package."
        )
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=None,
        help=(
            "A filepath where to write the built requirement file. Be aware that this "
            "won't create missing directories from your path."
        )
    )
    parser.add_argument(
        "--safe",
        action="store_true",
        help=(
            "This will avoid aborting process if a defined package is not "
            "installed, instead the package will just be commented with a message."
        )
    )
    parser.add_argument(
        "--ignore_pkg",
        action="append",
        help=(
            "Can be used multiple times to define some requirement package names to "
            "ignore."
        )
    )

    args = parser.parse_args()

    collector = InstalledRequirementCollector(safe=args.safe)
    collector.collect(
        args.package_name,
        destination=args.destination,
        ignore_pkg=args.ignore_pkg,
    )
