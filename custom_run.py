import sys
from trdg import run

val = 100

argv_sets = [
    # train 1
    [
        "run.py",
        "-l", "mc",
        "-c", f"{128*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\1"
    ],
    # train 2
    [
        "run.py",
        "-l", "mc",
        "-c", f"{128*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\2"
    ],
    # train 3
    [
        "run.py",
        "-l", "mc",
        "-c", f"{32*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\3"
    ],
    # train 4
    [
        "run.py",
        "-l", "mc",
        "-c", f"{32*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\train\4"
    ],
    # val 1
    [
        "run.py",
        "-l", "mc",
        "-c", f"{32*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\val\1"
    ],
    # val 2
    [
        "run.py",
        "-l", "mc",
        "-c", f"{32*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\val\2"
    ],
    # val 3
    [
        "run.py",
        "-l", "mc",
        "-c", f"{8*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\val\3"
    ],
    # val 4
    [
        "run.py",
        "-l", "mc",
        "-c", f"{8*val}",
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
        "--output_dir", r"C:\Users\WONJANGHO\Desktop\datas\val\4"
    ]
]

if __name__ == "__main__":
    for argv in argv_sets:
        sys.argv = argv
        run.main()
