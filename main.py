from flask import Flask, redirect,  render_template, request
app = Flask(__name__)

# encryption-decription process
def encryption_decryption(text):
    res = []
    for i in range(len(text)):
        if text[i]>='a' and text[i]<='z':
            ch = chr(ord('z') - ord(text[i]) + ord('a'))
            res.append(ch)
        elif text[i]>='A' and text[i]<='Z':
            ch = chr(ord('Z') - ord(text[i]) + ord('A'))
            res.append(ch)
        elif text[i]==" ":
            res.append(" ")
    return ''.join(res)

# convert plaintext to ciphertext
@app.route("/", methods = ["POST", "GET"])
def encipher():
    if request.method == "POST":
        plain_text = request.form['plaintext']
        return render_template("index.html", plain_text = encryption_decryption(plain_text))
    else:
        return render_template("index.html")

# convert ciphertext to plaintext
@app.route("/decipher", methods = ["POST"])
def decipher():
    cipher_text = request.form['ciphertext']
    print("d", cipher_text)
    return render_template("index.html", cipher_text = encryption_decryption(cipher_text))

# main
if __name__ == "__main__":
    app.run(debug=True)
