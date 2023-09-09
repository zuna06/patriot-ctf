i=1
while read p; do
  echo "$i"
  echo "$p" | nc chal.pctf.competitivecyber.club 9999
  ((i=i+1))
done <animals.txt
