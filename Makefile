install:
		poetry install

brain-games:
		poetry run python3 brain_games/scripts/brain_game.py

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --force dist/*.whl

make lint:
		poetry run flake8 brain_games

brain-even:
		poetry run brain-even

brain-calc:
		poetry run brain-calc

brain-gcd:
		poetry run brain-gcd

brain-progression:
		poetry run brain-progression

brain-prime:
		poetry run brain-prime