from src.utils import ErrorAnalyseService, NotifyService, EmailOutput
from test_data import SENDER_EMAIL, APP_PASSWORD, TEST_PATH

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH)
info_files = NotifyService.get_file_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_file_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH)
info_files = NotifyService.get_total_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_total_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')