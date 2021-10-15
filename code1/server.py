#!/usr/bin/python3
from flask import Flask
import subprocess
import time

app = Flask("kaaswors")


@app.route("/")
def home():
    print("jaaaa")
    time.sleep(10)
    return "Hello, World!"


# NOTE: Hier is 'n uitsonderlike stadige implementasie, toets met 60000011 en 6000000049 en huil
def is_priem(x):
    deelbaar_tel = 0
    for tel in range(1, x+1):
        if x%tel == 0:
            deelbaar_tel += 1
    return deelbaar_tel == 2


@app.route("/priem/<int:getal>")
def priem(getal):
    print("toetpriem:",getal)
    return "PRIEM!!!!" if is_priem(getal) else "PROEM?"


#
# Voeg 'n funksie by om 'n system call te doen na 'n program wat jy geskryf het wat 'n palidroom as int in neem en dan waar of vals return
# hint subprocess.check_output(['ls', '-l']), skryf 'n python program wat 'n palindroom as command line argument in vat en gebruik subprocess
# om die funksie te roep en die antwoorde terug te gee.
#


app.run()


