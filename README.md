# simple_cli
Use case of a cli to perform tasks 

## Instalation
You will need the following tools/programs already installed:
* [Homebrew](https://brew.sh/) or any other package manager
* [Python 3](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)

An installation example could be like this:
```
brew install python3
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
First, make sure you have activated the virtual environment `source venv/bin/activate`

### Commands
| Command | Description |
| -- | -- |
| python cli.py --help | Shows a list of valid commands |
| python cli.py show-info --character {something}| Will show first character that matches {something} in his/her/its info |
| python cli.py show-info --species {something}| Will show first species that matches {something} in its info |
| python cli.py show-info --film {something}| Will show first film that matches {something} in its info |

To deactivate the virtual env you just have to type:
```
deactivate
```
## Examples

Search for character info that matches `luke`
```
python cli.py show-info --character luke

--  Simple CLI using click  --
Author: Antonio Martín González
Email: ant.martin.gonzalez@gmail.com

- Name: Luke Skywalker
- Species: Human
- Hair color: blond
- Skin color: fair
- Eye color: blue
- Height: 172
- Mass: 77
- Birth year: 19BBY
```

Search for film info that matches `phan`
```
python cli.py show-info --film pha

--  Simple CLI using click  --
Author: Antonio Martín González
Email: ant.martin.gonzalez@gmail.com

- Title: The Phantom Menace
- Episode id: 1
- Director: George Lucas
- Producer: Rick McCallum
- Release date: 1999-05-19
```

Search for species info that matches `droid`
```
python cli.py show-info --species droid

--  Simple CLI using click  --
Author: Antonio Martín González
Email: ant.martin.gonzalez@gmail.com

- Name: Droid
- Homeworld: None
- Avg height: n/a
- Avg lifespan: indefinite
- Classification: artificial
- Designation: sentient
- Eye colors: n/a
- Hair colors: n/a
```

Search without specifying any parameter
```
python cli.py show-info

--  Simple CLI using click  --
Author: Antonio Martín González
Email: ant.martin.gonzalez@gmail.com

No data provided
```
