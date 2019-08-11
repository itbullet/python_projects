from flask import Flask, request, url_for, render_template

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

@app.route("/")
def count_and_say_form():
    return render_template('my-form.html')

@app.route("/", methods = ['POST'])
def count_and_say():

    sequence_number = int(request.form['sequence_number'])
    test1 = Solution()
    return """<html><body><pre>"""+test1.countAndSay(sequence_number)+"""</pre></body></html>"""

app.run(host="127.0.0.1", port="8000", debug=True)