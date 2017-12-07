p5cli.py only runs in Python 2.7

How to make p5cli.py exacutable

step 1) copy code to unix
chmod +x p5cli.py

step 2) change name
rm p5cli.py p5cli

step 3) run exacutable
usage: p5cli [API Argument] [String] [Value] [HTTP Method]

Only first two arguments are need for the API listed below:
md5
factorial
fibonacci
is-prime
slack-alert
kv-retrieve

all 4 arguments must be present If using kv-record
the fourth argument can only be "post" or "put" 
Using kv-record:
	./p5cli kv-record [String] [Value] [POST or PUT]
