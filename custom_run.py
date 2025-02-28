import sys
import os
import itertools
from trdg import run

val = 10
base_output_dir = r"C:\Users\WONJANGHO\Desktop\datas\train"

stw_options = [0, 1]
m_options = [0, 1]
sw_options = [1, 2]

combinations = list(itertools.product(stw_options, m_options, sw_options))

base_argv_sets = [
    [
        "run.py",
        "-c", f"{1*val}",
        "-w", "6",
        "-r",
        "-t", "8",

        "-na", "2",
        "-fd", "trdg/fonts/ko",
        "-dt", "trdg/dicts/bank.txt",
        "-b", "2",
        "-fi",

        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-d", "0",
    ],
    [
        "run.py",
        "-c", f"{1*val}",
        "-w", "6",
        "-r",
        "-t", "8",

        "-na", "2",
        "-fd", "trdg/fonts/ko",
        "-dt", "trdg/dicts/bank2.txt",
        "-b", "2",
        "-fi",

        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-d", "0",
    ],
    [
        "run.py",
        "-c", f"{1*val}",
        "-w", "6",
        "-r",
        "-t", "8",

        "-na", "2",
        "-fd", "trdg/fonts/ko",
        "-dt", "trdg/dicts/ko.txt",
        "-l ko"
        "-rs",
        "-b", "2",
        "-fi",

        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-d", "0",
    ],
    [
        "run.py",
        "-c", f"{1*val}",
        "-w", "6",
        "-r",
        "-t", "8",

        "-na", "2",
        "-fd", "trdg/fonts/ko",
        "-dt", "trdg/dicts/ko.txt",
        "-l ko"
        "-rs",
        "-b", "2",
        "-fi",

        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-d", "0",
    ],
]

if __name__ == "__main__":
    run_count = 1

    for base_argv in base_argv_sets:
        for stw, m, sw in combinations:
            argv = base_argv.copy()  # 기본 설정 복사
            argv.extend(["-stw", str(stw)])
            argv.extend(["-m", str(m)])
            argv.extend(["-sw", str(sw)])

            output_dir = os.path.join(base_output_dir, str(run_count))
            argv.extend(["--output_dir", output_dir])

            sys.argv = argv
            run.main()

            run_count += 1
