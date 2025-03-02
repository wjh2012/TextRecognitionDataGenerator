python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 0 -fi
python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 0
python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 1 -fi
python trdg/run.py -l mc -c 20 -w 6 -r -na 2 -rs -num -let -k 0 -rk -bl 3 -rbl -b 2 -d 0 -m 1

python trdg/run.py -c 20 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/ko.txt -l ko -rs -b 2 -fi -k 0 -rk -bl 3 -rbl -d 0 -stw 1 -m 0 -sw 2
python trdg/run.py -c 10 -w 6 -r -na 2 -fd trdg/fonts/ko -dt trdg/dicts/money.txt -l ko -b 2 -fi -k 0 -rk -bl 3 -rbl -d 0 -stw 1 -m 0 -sw 2 


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