from utils import ErrorAnalyseService, NotifyService, EmailOutput, ConsoleOutput, TelegrambotOutput


def check_input(var: str, example: list) -> str:
    while var not in example:
        var = input('Please, check your input and try again: ')
    return var

def main():
    path_to_folder: str = input('Enter the full path to your folder with logs: ')
    recursive_search = input('Do you want to search recursively? y/n: ')
    recursive_search = check_input(recursive_search, ['y', 'n'])

    recursive_search = True if recursive_search == 'y' else False

    info_output_option = input('Do you want to get info about logs separately or in general? s/g: ')
    info_output_option = check_input(info_output_option, ['s', 'g'])

    analysis_folder = ErrorAnalyseService()
    list_of_files = analysis_folder.parse_files(path_to_folder, recursive_search)

    if info_output_option == 's':
        analysis_result = NotifyService.get_file_info(list_of_files)
    else:
        analysis_result = NotifyService.get_total_info(list_of_files)

    get_result: str = input('How do you want to get the result? (email, telegrambot, console): ')
    get_result = check_input(get_result, ['email', 'telegrambot'])

    if get_result == 'email':
        sender_email = input('Enter sender email address: ')
        app_password = input('Enter your password or app password: ')
        reciever_email = input('Enter receiver email address: ')
        EmailOutput.email_output(analysis_result, sender_email, app_password, reciever_email)
    elif get_result == 'telegrambot':
        bot_token = input('Enter token from your bot: ')
        chat_id = input('Enter chat or group chat id: ')
        TelegrambotOutput.telegrambot_output(analysis_result, bot_token, chat_id)
    elif get_result == 'console':
        ConsoleOutput.console_output(analysis_result)


if __name__ == '__main__':
    main()
