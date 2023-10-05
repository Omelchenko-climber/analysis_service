class NotifyService:  # print notifications to the console

    @staticmethod
    def get_file_info(data: list) -> str:
        all_files = []
        for info in data:
            all_files.append(str(info))

        return '\n'.join(all_files)

    @staticmethod
    def get_total_info(data: list) -> str:
        total_log_records = sum([file.log_records for file in data])
        total_log_errors = sum([file.log_errors for file in data])

        total_first_error_date = min([file.first_error_date for file in data])
        total_last_error_date = max([file.last_error_date for file in data])

        return 'Folder information: Files {: ^10} Records {: ^10} Errors {: ^10} Date: First error  {: ^15} Last error {: ^15}'.format(
            len(data), total_log_records, total_log_errors, total_first_error_date.strftime('%Y-%m-%d'),
            total_last_error_date.strftime('%Y-%m-%d'))
