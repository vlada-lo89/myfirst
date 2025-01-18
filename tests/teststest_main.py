import pytest
from main import calculate_average

def test_calculate_average_empty_file(tmp_path):
    d = tmp_path / "data.csv"
    d.write_text("Age\n")
    assert calculate_average(str(d)) == 0

def test_calculate_average_normal_data(tmp_path):
    d = tmp_path / "data.csv"
    text = """Age,OtherData,MoreData,Data4,Data5,Data6,AgeColumn
25,,,,,,25
30,,,,,,30
45,,,,,,45
"""
    d.write_text(text)

    assert calculate_average(str(d)) == 33.333333333333336