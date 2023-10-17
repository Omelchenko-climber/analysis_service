import dataclasses
from datetime import date


@dataclasses.dataclass
class FileInfo:  # this dto class contains info about logs in the file

    def __init__(self, name: str, log_records: int, log_errors: int, first_error_date: date,
                 last_error_date: date) -> None:
        self.name = name
        self.log_records = log_records
        self.log_errors = log_errors
        self.first_error_date = first_error_date
        self.last_error_date = last_error_date

    def __str__(self) -> str:
        return 'File information: Name -{: ^15}- Records {: ^10} Errors {: ^10} Date: First error {: ^15} Last error {: ^15}\n'.format(
            self.name, self.log_records, self.log_errors, self.first_error_date.strftime('%Y-%m-%d'),
            self.last_error_date.strftime('%Y-%m-%d'))
