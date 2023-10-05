import requests

class TelegrambotOutput:

    @staticmethod
    def telegrambot_output(info: str, bot_token: str, chat_id: str) -> None:

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

        params = {
            'chat_id': chat_id,
            'text': info
        }

        try:
            response = requests.post(url, data=params)

            if response.status_code == 200:
                print('Message sent successfully!')
            else:
                print('Failed to send message. Status code:', response.status_code)

        except Exception as e:
            print('An error occurred:', str(e))

# TOKEN = '6491073642:AAE9MLnsgTHy0mIIOjBN9q6mUrtQuC8VnF0'
#
# chat_id = '521868872'
#
# url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
#
# message_text = 'Hello, you did it!!!'
#
# params = {
#     'chat_id': chat_id,
#     'text': message_text
# }
#
# try:
#     response = requests.post(url, data=params)
#
#     if response.status_code == 200:
#         print('Message sent successfully!')
#     else:
#         print('Failed to send message. Status code:', response.status_code)
#
# except Exception as e:
#     print('An error occurred:', str(e))