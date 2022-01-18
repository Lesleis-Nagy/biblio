import typer

import biblio.actions.db as db

from biblio.exceptions import UnsetEnvironmentVariableException


app = typer.Typer()
app.add_typer(db.app, name="db")


def main():
    try:
        app()
    except UnsetEnvironmentVariableException as exp:
        print(f"ERROR: {exp}")
