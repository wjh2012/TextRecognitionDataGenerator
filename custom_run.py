import itertools
import sys
import os
from trdg import run

val = 50000
base_output_dir = r"C:\Users\WONJANGHO\Desktop\micr_source"

m_options = [0, 1]
sw_options = [1, 2]
cs_options = [0, 2]

combinations = list(itertools.product(cs_options, m_options, sw_options))

base_argv_sets = [
    [
        "run.py",
        "-c", f"{1*val}",
        "-w", "6",
        "-r",
        "-t", "8",

        "-na", "2",
        "-fd", "trdg/fonts/mc",
        "-b", "2",
        "-fi",

        "-d", "3",
        "-k", "1",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-d", "0",
        "-rs",
        "-num",
        "-tc",
        "#000000,#282828"
    ]
]

if __name__ == "__main__":
    run_count = 1

    for base_argv in base_argv_sets:
        for cs, m, sw in combinations:
            argv = base_argv.copy()  # 기본 설정 복사
            argv.extend(["-cs", str(cs)])
            argv.extend(["-m", str(m)])
            argv.extend(["-sw", str(sw)])

            output_dir = os.path.join(base_output_dir, str(run_count))
            argv.extend(["--output_dir", output_dir])

            sys.argv = argv
            run.main()

            run_count += 1
