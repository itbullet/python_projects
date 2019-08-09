from flask import Flask, request, url_for

class Solution:
    def countAndSay(self, n):

        num_str = "1"
        tmp_str = ""
        level = 1
        html_str = ""

        if n == 0:

            return "zero"


        while level <= n:

            html_str = html_str+"<p>"+num_str+"</p>"
            str_len = len(num_str)
            i = 0
            j = 0

            while i < str_len:

                char = num_str[i]
                count = 0

                while j < str_len:

                    if num_str[j] == char:

                        count += 1
                        j += 1

                    else:

                        break

                tmp_str = tmp_str+str(count)+char

                i = j

            num_str = tmp_str
            tmp_str = ""
            level += 1

        return html_str

##########

app = Flask(__name__)

@app.route("/count_and_say", methods = ["GET", "POST"])
def count_and_say():

    if request.method == "GET":

        #if request.form['submit_button'] == "Submit":

            #sequence_number = request.form["sequence_number"]
            req = request.form
            test1 = Solution()
            return """<html><body><pre>"""+test1.countAndSay(4)+"""</pre></body></html>"""

@app.route("/")
def index():

    return """<form action="""+url_for("count_and_say")+""" method="GET">
            Enter number of count-and-say sequence: <input type="text" name="sequence_number"><br>
            <input type="submit" name="submit_button" value="Submit">
            </form>"""

app.run(host="172.30.20.132", port="8000")