from src import ErrorAnalyseService, NotifyService, ConsoleOutput
from test_data import TEST_PATH

analizer = ErrorAnalyseService()

list_of_files = analizer.parse_files(TEST_PATH)
info_result = NotifyService.get_file_info(list_of_files)
ConsoleOutput.console_output(info_result)

list_of_files = analizer.parse_files(TEST_PATH, True)
info_result = NotifyService.get_file_info(list_of_files)
ConsoleOutput.console_output(info_result)

list_of_files = analizer.parse_files(TEST_PATH)
info_result = NotifyService.get_total_info(list_of_files)
ConsoleOutput.console_output(info_result)

list_of_files = analizer.parse_files(TEST_PATH, True)
info_result = NotifyService.get_total_info(list_of_files)
ConsoleOutput.console_output(info_result)
