import typer

import biblio.actions.db as db
import biblio.actions.abstract as abstract

from biblio.exceptions import UnsetEnvironmentVariableException


app = typer.Typer()
app.add_typer(db.app, name="db")
app.add_typer(abstract.app, name="abstract")


def main():
    try:
        app()
    except UnsetEnvironmentVariableException as exp:
        print(f"ERROR: {exp}")
