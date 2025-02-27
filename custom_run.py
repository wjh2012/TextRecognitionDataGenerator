import sys
from trdg import run

val = 100

argv_sets = [
    # train 1
    [
        "run.py",
        "-l", "en",
        "-c", f"{256*val}",
        "-w", "6",
        "-r",
        "-na", "2",
        "-rs",
        "-num",
        "-let",
        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-b", "2",
        "-d", "0",
        "-m", "0",
        "-fi",
        "-fd", "trdg/fonts/th",
        "-t", "8",
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\5"
    ],
    # train 2
    [
        "run.py",
        "-l", "en",
        "-c", f"{256*val}",
        "-w", "6",
        "-r",
        "-na", "2",
        "-rs",
        "-num",
        "-let",
        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-b", "2",
        "-d", "0",
        "-m", "0",
        "-fd", "trdg/fonts/th",
        "-t", "8",
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\6"
    ],
    # train 3
    [
        "run.py",
        "-l", "en",
        "-c", f"{64*val}",
        "-w", "6",
        "-r",
        "-na", "2",
        "-rs",
        "-num",
        "-let",
        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-b", "2",
        "-d", "0",
        "-m", "1",
        "-fi",
        "-fd", "trdg/fonts/th",
        "-t", "8",
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\7"
    ],
    # train 4
    [
        "run.py",
        "-l", "en",
        "-c", f"{64*val}",
        "-w", "6",
        "-r",
        "-na", "2",
        "-rs",
        "-num",
        "-let",
        "-k", "0",
        "-rk",
        "-bl", "3",
        "-rbl",
        "-b", "2",
        "-d", "0",
        "-m", "1",
        "-fd", "trdg/fonts/th",
        "-t", "8",
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\8"
    ],
]

if __name__ == "__main__":
    for argv in argv_sets:
        sys.argv = argv
        run.main()
