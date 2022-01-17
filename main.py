from flask import Flask, redirect,  render_template, request

app = Flask(__name__)

# encryption-decription process
def encryption_decryption(text):
    res = []
    for i in range(len(text)):
        ch = chr(ord('z') - ord(text[i]) + ord('a'))
        res.append(ch)
    return ''.join(res)


# convert plaintext to ciphertext
@app.route("/", methods = ["POST", "GET"])
def encipher():
    if request.method == "POST":
        plain_text = request.form['plaintext']
        return render_template("index.html", plain_text = encryption_decryption(plain_text))
    else:
        return render_template("index.html")


# convert ciphertext to plintext
@app.route("/decipher", methods = ["POST"])
def decipher():
    cipher_text = request.form['ciphertext']
    print("d", cipher_text)
    return render_template("index.html", cipher_text = encryption_decryption(cipher_text))


# main
if __name__ == "__main__":
    app.run(debug=True)
