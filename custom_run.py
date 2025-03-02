import sys
import os
import itertools
from trdg import run

val = 10000
# base_output_dir = "./out"
base_output_dir = "/home/taehwa/remote_dev/generated_data"

# stw_options = [0]
# m_options = [0]
# sw_options = [1]

# stw_options = [0, 1]
# m_options = [0, 1]
# sw_options = [1, 2]

stw_options = [2, 3]
m_options = [0, 1]
sw_options = [1, 2]

combinations = list(itertools.product(stw_options, m_options, sw_options))

base_argv_sets = [
    # [
    #     "run.py",
    #     "-c", f"{1*val}",
    #     "-w", "6",
    #     "-r",
    #     "-t", "32",
    #
    #     "-na", "2",
    #     "-fd", "trdg/fonts/ko",
    #     "-dt", "trdg/dicts/bank.txt",
    #     "-b", "2",
    #     "-fi",
    #
    #     "-k", "0",
    #     "-rk",
    #     "-bl", "3",
    #     "-rbl",
    #     "-d", "0",
    # ],
    # [
    #     "run.py",
    #     "-c", f"{1*val}",
    #     "-w", "6",
    #     "-r",
    #     "-t", "32",
    #
    #     "-na", "2",
    #     "-fd", "trdg/fonts/ko",
    #     "-dt", "trdg/dicts/bank2.txt",
    #     "-b", "2",
    #     "-fi",
    #
    #     "-k", "0",
    #     "-rk",
    #     "-bl", "3",
    #     "-rbl",
    #     "-d", "0",
    # ],
    # [
    #     "run.py",
    #     "-c", f"{10*val}",
    #     "-w", "6",
    #     "-r",
    #     "-t", "32",
    #
    #     "-na", "2",
    #     "-fd", "trdg/fonts/ko",
    #     "-dt", "trdg/dicts/money.txt",
    #     "-l", "ko",
    #     "-b", "2",
    #     "-fi",
    #
    #     "-k", "0",
    #     "-rk",
    #     "-bl", "3",
    #     "-rbl",
    #     "-d", "0",
    # ],
    # [
    #     "run.py",
    #     "-c", f"{1*val}",
    #     "-w", "6",
    #     "-r",
    #     "-t", "32",
    #     "-l", "ko",
    #
    #     "-na", "2",
    #     "-fd", "trdg/fonts/ko",
    #     "-dt", "trdg/dicts/ko.txt",
    #     "-rs",
    #     "-b", "2",
    #     "-fi",
    #
    #     "-k", "0",
    #     "-rk",
    #     "-bl", "3",
    #     "-rbl",
    #     "-d", "0",
    # ],
    ######
    # [
    #     "run.py",
    #     "-c", f"{1*val}",
    #     "-w", "6",
    #     "-r",
    #     "-t", "32",
    #
    #     "-na", "2",
    #     "-fd", "trdg/fonts/ko",
    #     "-dt", "trdg/dicts/num.txt",
    #     "-l", "ko",
    #     "-b", "2",
    #     "-fi",
    #
    #     "-k", "0",
    #     "-rk",
    #     "-bl", "3",
    #     "-rbl",
    #     "-d", "0",
    #     "-rs", "-num", "-sym"
    # ],
    #######
    [
        "run.py",
        "-c", f"{1*val}",
        "-w", "6",
        "-r",
        "-t", "32",

        "-na", "2",
        "-fd", "trdg/fonts/ko",
        "-dt", "trdg/dicts/money.txt",
        "-l", "ko",
        "-b", "2",
        "-fi",

        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-d", "0",
        "-cs", "3"
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

            output_dir = os.path.join(base_output_dir, str(run_count)+"m")
            argv.extend(["--output_dir", output_dir])

            sys.argv = argv
            run.main()

            run_count += 1
