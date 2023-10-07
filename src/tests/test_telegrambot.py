from src.utils import ErrorAnalyseService, NotifyService, TelegrambotOutput
from test_data import BOT_TOKEN, GROUP_CHAT_ID, TEST_PATH

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH)
info_files = NotifyService.get_file_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_file_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH)
info_files = NotifyService.get_total_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)

analyzer = ErrorAnalyseService()
list_of_files = analyzer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_total_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)