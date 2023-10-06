from src import ErrorAnalyseService, NotifyService, TelegrambotOutput
from test_data import BOT_TOKEN, GROUP_CHAT_ID, TEST_PATH

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH)
info_files = NotifyService.get_file_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_file_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH)
info_files = NotifyService.get_total_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)

analizer = ErrorAnalyseService()
list_of_files = analizer.parse_files(TEST_PATH, True)
info_files = NotifyService.get_total_info(list_of_files)
TelegrambotOutput.telegrambot_output(info_files, BOT_TOKEN, GROUP_CHAT_ID)