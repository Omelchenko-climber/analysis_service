import os

from src.utils import HtmlOutput, ErrorAnalyseService

TEST_PATH = os.environ.get('TEST_PATH')

analyzer = ErrorAnalyseService()

list_of_files = analyzer.parse_files(TEST_PATH, True)
HtmlOutput.html_output_file(list_of_files)
