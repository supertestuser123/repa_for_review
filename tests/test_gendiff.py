import pytest


from gendiff.gendiff import generate_diff


file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'

file1_yaml = 'tests/fixtures/file1.yml'
file2_yaml = 'tests/fixtures/file2.yml'

stylish_path = 'tests/fixtures/check_stylish.txt'
plain_path = 'tests/fixtures/check_plain.txt'
json_path = 'tests/fixtures/check_json.txt'
common_files_path = 'tests/fixtures/check_identical_files.txt'

options = [(file1_json, file2_json, 'stylish', stylish_path),
           (file1_json, file2_json, 'plain', plain_path),
           (file1_json, file2_json, 'json', json_path),
           (file1_yaml, file2_json, 'stylish', stylish_path),
           (file1_yaml, file2_yaml, 'plain', plain_path),
           (file1_yaml, file2_yaml, 'json', json_path),
           (file1_yaml, file2_yaml, 'stylish', common_files_path),
           ]


@pytest.mark.parametrize("path1, path2, format, path_check_file", options)
def test_generate_diff(path1, path2, format, path_check_file):
    res = generate_diff(path1, path2, format)

    with open(path_check_file) as check_file:
        assert res == check_file.read()
