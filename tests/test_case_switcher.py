import pytest
from src.case_switcher import switch_cases

def test_switch_cases_basic():
    result = switch_cases("Hello", "World")
    assert result == "hELLO wORLD"

def test_switch_cases_mixed_case():
    result = switch_cases("MiXeD", "CaSe")
    assert result == "mIxEd cAsE"

def test_switch_cases_empty_strings():
    result = switch_cases("", "")
    assert result == ""

def test_switch_cases_non_alphabetic():
    result = switch_cases("123", "!@#")
    assert result == "123!@#"

def test_switch_cases_all_uppercase():
    result = switch_cases("HELLO", "WORLD")
    assert result == "hello world"

def test_switch_cases_all_lowercase():
    result = switch_cases("hello", "world")
    assert result == "HELLO WORLD"