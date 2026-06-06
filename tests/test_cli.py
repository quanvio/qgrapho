"""Smoke tests for QGrapho CLI."""

import pytest

from qgrapho.cli import main


def test_help_exits_zero():
    with pytest.raises(SystemExit) as exc:
        main(["--help"])
    assert exc.value.code == 0


def test_version_exits_zero():
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0


def test_doctor_runs():
    code = main(["doctor"])
    assert code in (0, 1)
