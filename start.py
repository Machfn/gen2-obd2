import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
import json
import threading

from comp.openView import openShow

app = typer.Typer()

@app.command("setup")
def sample_func():
    exec(open("./setup.bash").read())


@app.command("run")
def sample_func():
    openPage = threading.Thread(target=openShow)
    openPage.start()
    # startSockets = threading.Thread(target=exec(open("./sockets.py").read()))
    # startSockets.start()
    exec(open("./serv.py").read())



if __name__ == "__main__":
    app()