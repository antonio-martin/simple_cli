import click
import colorama

from apis.films import get_films
from apis.people import get_people
from apis.species import get_species
from models.film import Film
from models.person import Person
from models.species import Species

__author__ = 'Antonio Martín González'
__email__ = 'ant.martin.gonzalez@gmail.com'

STYLE_MESSAGE = colorama.Fore.GREEN
STYLE_INFO = colorama.Fore.CYAN
STYLE_ERROR = colorama.Fore.RED


@click.group()
def cli():
    click.echo(STYLE_MESSAGE + "")
    click.echo(STYLE_MESSAGE + "--  Simple CLI using click  --")
    click.echo(STYLE_MESSAGE + "Author: " + STYLE_INFO + __author__)
    click.echo(STYLE_MESSAGE + f"Email: " + STYLE_INFO + __email__)
    click.echo(STYLE_MESSAGE + "")


def _is_in(a, b):
    return str(a).lower() in str(b).lower()


def _get_character(character, people: [Person]) -> Person:
    for person in people:
        for attr in vars(person):
            if _is_in(character, person.__getattribute__(attr)):
                return person
    return None


def _get_species(data, species: [Species]) -> Species:
    for spec in species:
        for attr in vars(spec):
            if _is_in(data, spec.__getattribute__(attr)):
                return spec
    return None


def _get_film(data, films: [Film]) -> Film:
    for film in films:
        for attr in vars(film):
            if _is_in(data, film.__getattribute__(attr)):
                return film
    return None


def show_info_character(data):
    person: Person = None
    response = get_people()
    count = response.json().get('count')
    page = 1
    while person is None and count > 0:
        response = get_people(page=page).json().get('results')
        people = [Person.load_from_dict(p) for p in response]
        person = _get_character(data, people)
        count -= 10
        page += 1
    if person is None:
        click.echo(STYLE_ERROR + f"No character found that matches {data}")
    else:
        click.echo(STYLE_MESSAGE + "- Name: " + STYLE_INFO + str(person.name))
        click.echo(STYLE_MESSAGE + "- Species: " + STYLE_INFO + str(person.species()[0].name))
        click.echo(STYLE_MESSAGE + "- Hair color: " + STYLE_INFO + str(person.hair_color))
        click.echo(STYLE_MESSAGE + "- Skin color: " + STYLE_INFO + str(person.skin_color))
        click.echo(STYLE_MESSAGE + "- Eye color: " + STYLE_INFO + str(person.eye_color))
        click.echo(STYLE_MESSAGE + "- Height: " + STYLE_INFO + str(person.height))
        click.echo(STYLE_MESSAGE + "- Mass: " + STYLE_INFO + str(person.mass))
        click.echo(STYLE_MESSAGE + "- Birth year: " + STYLE_INFO + str(person.birth_year))


def show_info_species(data):
    spec: Species = None
    response = get_species()
    count = response.json().get('count')
    page = 1
    while spec is None and count > 0:
        response = get_species(page=page).json().get('results')
        species = [Species.load_from_dict(p) for p in response]
        spec = _get_species(data, species)
        count -= 10
        page += 1
    if spec is None:
        click.echo(STYLE_ERROR + f"No species found that matches {data}")
    else:
        click.echo(STYLE_MESSAGE + f"- Name: " + STYLE_INFO + str(spec.name))
        click.echo(STYLE_MESSAGE + f"- Homeworld: " + STYLE_INFO + str(spec.homeworld))
        click.echo(STYLE_MESSAGE + f"- Avg height: " + STYLE_INFO + str(spec.average_height))
        click.echo(STYLE_MESSAGE + f"- Avg lifespan: " + STYLE_INFO + str(spec.average_lifespan))
        click.echo(STYLE_MESSAGE + f"- Classification: " + STYLE_INFO + str(spec.classification))
        click.echo(STYLE_MESSAGE + f"- Designation: " + STYLE_INFO + str(spec.designation))
        click.echo(STYLE_MESSAGE + f"- Eye colors: " + STYLE_INFO + str(spec.eye_colors))
        click.echo(STYLE_MESSAGE + f"- Hair colors: " + STYLE_INFO + str(spec.hair_colors))


def show_info_film(data):
    film: Film = None
    response = get_films()
    count = response.json().get('count')
    page = 1
    while film is None and count > 0:
        response = get_films(page=page).json().get('results')
        films = [Film.load_from_dict(p) for p in response]
        film = _get_film(data, films)
        count -= 10
        page += 1
    if film is None:
        click.echo(STYLE_ERROR + f"No films found that matches {data}")
    else:
        click.echo(STYLE_MESSAGE + f"- Title: " + STYLE_INFO + str(film.title))
        click.echo(STYLE_MESSAGE + f"- Episode id: " + STYLE_INFO + str(film.episode_id))
        click.echo(STYLE_MESSAGE + f"- Director: " + STYLE_INFO + str(film.director))
        click.echo(STYLE_MESSAGE + f"- Producer: " + STYLE_INFO + str(film.producer))
        click.echo(STYLE_MESSAGE + f"- Release date: " + STYLE_INFO + str(film.release_date))


@cli.command()
@click.option('--character', '-c')
@click.option('--species', '-s')
@click.option('--film', '-f')
def show_info(character, species, film):
    """Show info for the first matching object"""
    if character:
        show_info_character(character)
    elif species:
        show_info_species(species)
    elif film:
        show_info_film(film)
    else:
        click.echo(STYLE_ERROR + "No data provided")


if __name__ == "__main__":
    # cli(['show-info', '-c', 'luke'])
    cli()
