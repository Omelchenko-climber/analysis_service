import os

from src.utils import ErrorAnalyseService, NotifyService, EmailOutput

TEST_PATH = os.environ.get('TEST_PATH')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
APP_PASSWORD = os.environ.get('APP_PASSWORD')

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