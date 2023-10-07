from src.utils  import ConsoleOutput, NotifyService, ErrorAnalyseService
from test_data import TEST_PATH

analyzer = ErrorAnalyseService()

list_of_files = analyzer.parse_files(TEST_PATH)
info_result = NotifyService.get_file_info(list_of_files)
ConsoleOutput.console_output(info_result)

list_of_files = analyzer.parse_files(TEST_PATH, True)
info_result = NotifyService.get_file_info(list_of_files)
ConsoleOutput.console_output(info_result)

list_of_files = analyzer.parse_files(TEST_PATH)
info_result = NotifyService.get_total_info(list_of_files)
ConsoleOutput.console_output(info_result)

list_of_files = analyzer.parse_files(TEST_PATH, True)
info_result = NotifyService.get_total_info(list_of_files)
ConsoleOutput.console_output(info_result)
