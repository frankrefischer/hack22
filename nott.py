from pathlib import Path
from typing import Tuple, Dict, Iterable, Callable, Any

import pandas as pd

InputData = Dict[str, Any]
InputLineParser = Callable[[str], InputData]
InputFieldDef = Tuple[str, int, Callable]


def duration_in_hours(duration: str) -> float:
    hh, mm = duration.split(':')
    return int(hh) + (int(mm) / 60)


class Input:
    def __init__(self, input_dir: Path):
        self.input_dir = input_dir
        self.students = self.load_students()
        self.exams = self.load_exams()
        self.enrolements = self.load_enrolements()

    def load_students(self):
        line_parser = make_line_parser(
            student=(10, str),
            course=(4, str),
        )
        data = self._parse_file(filename='students',
                                line_parser=line_parser)
        return pd.DataFrame(data=data)

    def load_exams(self):
        line_parser = make_line_parser(
            exam=(8, str),
            descr=(40, str),
            duration=(4, duration_in_hours),
            department=(2, str),
        )
        data = self._parse_file(filename='exams',
                                line_parser=line_parser)
        return pd.DataFrame(data=data)

    def load_enrolements(self):
        line_parser = make_line_parser(
            student=(10, str),
            exam=(8, str),
        )
        data = self._parse_file(filename='enrolements',
                                line_parser=line_parser)
        return pd.DataFrame(data=data)

    def _parse_file(self, filename: str, line_parser: InputLineParser) -> Iterable[InputData]:
        with open(self.input_dir.joinpath(filename)) as fin:
            yield from (line_parser(line)
                        for line in fin.readlines())


def make_line_parser(**field_defs) -> InputLineParser:
    def parser(line: str) -> InputData:
        data = {}
        fstart = 0
        for fname, (fwidth, ftype) in field_defs.items():
            field_as_string = line.strip()[fstart:fstart + fwidth]
            data[fname] = ftype(field_as_string)
            fstart += fwidth + 1
        return data

    return parser


class Nott():
    def __init__(self, input: Input):
        self.input = input


def main():
    input = Input(input_dir=Path('./nott'))
    nott = Nott(input)


if __name__ == '__main__':
    main()
