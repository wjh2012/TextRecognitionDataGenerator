python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 0 -fi
python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 0
python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 1 -fi
python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 1

python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/ko.txt -m 0 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -rs -sw 1 -stw 1 -t 8
python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/ko.txt -m 0 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -rs -sw 2 -t 8
python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/ko.txt -m 1 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -rs -sw 1 -t 8
python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/ko.txt -m 1 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -rs -sw 2 -t 8

python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/bank.txt -m 0 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -sw 1 -t 8
python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/bank.txt -m 0 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -sw 2 -t 8 -stw 1
python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/bank.txt -m 1 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -sw 1 -t 8
python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/bank.txt -m 1 -fi -k 0 -rk -bl 3 -rbl -b 2 -d 0 -sw 2 -t 8 -stw 1


-l (language)
-c (count)
-w (word count)
-r (word count random)
-na 2 (label.txt)
-rs -num -let (random sequence number and letter)
-k (skew)
-rk (random skew)
-bl 1(gaussian blur)
-rbl (gaussian blur 0 to bl)
-b (background)
-d (distortion)