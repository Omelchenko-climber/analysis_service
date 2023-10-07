import os
import re
from datetime import datetime, date

from src.data.dto import FileInfo


class EmptyFileError(Exception):

    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f'The file "{filename}" is empty!\n')


class ErrorAnalyseService:
    total_log_records = 0
    total_log_errors = 0
    total_first_error_date = False
    total_last_error_date = False

    def parse_files(self, path_to_folder: str,
                    recursively=False) -> list:
        ''' Function parse files in the folder. It can be recursively or not. '''

        list_files = []

        dict_files = self._find_all_files(path_to_folder, recursively)  #

        for name, path in dict_files.items():
            log_records = 0
            log_errors = 0
            first_error_date = False
            last_error_date = False
            full_path = path + '/' + name
            try:
                if os.path.getsize(full_path) == 0:
                    raise EmptyFileError(full_path)
            except EmptyFileError as e:
                print(e)
                continue
            with open(full_path, 'r', encoding='utf-8') as log_file:
                for line in log_file:
                    if re.search(r'^\d{4}|^[A-Z]\w{2}', line):
                        log_records += 1
                        if re.search(r'(<err>)|(ERROR)|(SEVERE)', line):
                            log_errors += 1
                            date_error = re.findall('(^[A-Za-z]{3} [A-Za-z]{3} {1,2}\d{1,2}|^\d{4}-\d{2}-\d{2})', line)[
                                0]
                            date_error = self._get_normalize_date(date_error, full_path)
                            if not first_error_date or first_error_date > date_error:
                                first_error_date = date_error
                            else:
                                last_error_date = date_error

                list_files.append(FileInfo(name, log_records, log_errors, first_error_date, last_error_date))

        return list_files

    def _find_all_files(self, path_to_folder: str,
                        recursively=False) -> dict:  # Find all files in the folder recursively or not and return dict with key=files name and value=full path to the file
        dict_files = {}

        if recursively:
            for root, _, files in os.walk(path_to_folder):
                dict_files.update({name: root for name in files})
        else:
            dict_files = {name: path_to_folder for name in os.listdir(path_to_folder) if
                          os.path.isfile(os.path.join(path_to_folder, name))}

        return dict_files

    def _get_normalize_date(self, str_date: str,
                            file_path: str = None) -> date:  # From date in the str type this function returns date in the date type with "yyyy-mm-dd" format.
        if re.match('[A-Za-z]{3} [A-Za-z]{3} {1,2}\d{1,2}', str_date):
            creation_year = date.fromtimestamp(os.path.getctime(file_path)).year
            parsed_date = datetime.strptime(str_date, '%a %b %d')
            normalize_date = parsed_date.replace(year=creation_year).date()
            if normalize_date > datetime.today().date():
                normalize_date = parsed_date.replace(year=creation_year - 1).date()
        else:
            normalize_date = datetime.strptime(str_date, '%Y-%m-%d').date()

        return normalize_date
