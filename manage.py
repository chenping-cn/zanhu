#!/usr/bin/env python
# ruff: noqa
import os
import sys
from pathlib import Path
from pymysql import install_as_MySQLdb

if __name__ == "__main__":
    install_as_MySQLdb()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    # This allows easy placement of apps within the interior
    # zanhu directory.
    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "zanhu"))

    execute_from_command_line(sys.argv)
