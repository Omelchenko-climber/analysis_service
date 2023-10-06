from src import ErrorAnalyseService, NotifyService, EmailOutput
from test_data import SENDER_EMAIL, APP_PASSWORD, TEST_PATH

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH)
info_files = NotifyService.get_file_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_file_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH)
info_files = NotifyService.get_total_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_total_info(list_of_files)
EmailOutput.email_output(info_files, SENDER_EMAIL, APP_PASSWORD, 'omelchenko230783@gmail.com')