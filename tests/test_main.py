from gendiff.main import generate_diff
from pathlib import Path
import pytest


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_test_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff(capsys):
    filepath1 = get_test_data_path("plain_file1.json")
    filepath2 = get_test_data_path("plain_file2.json")
    expected_result = read_test_file("expected_plain")
    generate_diff(filepath1, filepath2)
    result = capsys.readouterr()
    assert result.out == expected_result


def test_empty_no_change(capsys):
    filepath1 = get_test_data_path("empty1.json")
    filepath2 = get_test_data_path("empty2.json")
    expected_result = read_test_file("expected_empty")
    generate_diff(filepath1, filepath2)
    result = capsys.readouterr()
    assert result.out == expected_result


def test_add_line(capsys):
    filepath1 = get_test_data_path("add_file1.json")
    filepath2 = get_test_data_path("add_file2.json")
    expected_result = read_test_file("expected_add")
    generate_diff(filepath1, filepath2)
    result = capsys.readouterr()
    assert result.out == expected_result


def test_remove_line(capsys):
    filepath1 = get_test_data_path("remove_file1.json")
    filepath2 = get_test_data_path("remove_file2.json")
    expected_result = read_test_file("expected_remove")
    generate_diff(filepath1, filepath2)
    result = capsys.readouterr()
    assert result.out == expected_result


def test_change_value(capsys):
    filepath1 = get_test_data_path("changevalue_file1.json")
    filepath2 = get_test_data_path("changevalue_file2.json")
    expected_result = read_test_file("expected_changevalue")
    generate_diff(filepath1, filepath2)
    result = capsys.readouterr()
    assert result.out == expected_result


def test_change_line(capsys):
    filepath1 = get_test_data_path("changeline_file1.json")
    filepath2 = get_test_data_path("changeline_file2.json")
    expected_result = read_test_file("expected_changeline")
    generate_diff(filepath1, filepath2)
    result = capsys.readouterr()
    assert result.out == expected_result