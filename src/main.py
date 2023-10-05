from utils import NotifyService
from utils import ErrorAnalyseService, email_output_service, telegrambot_output_service

logs_str = 'C:/Users/User/PycharmProjects/Utils/test_log_folder/'

test = ErrorAnalyseService()
files = test.parse_files(logs_str, True)
info_to_send = NotifyService.get_file_info(files)
# print(NotifyService.get_file_info(files))
# print(NotifyService.get_total_info(files))
# email_output_service.EmailOutput.email_output(info_to_send)
# telegrambot_output_service.TelegrambotOutput.telegrambot_output(info_to_send)
