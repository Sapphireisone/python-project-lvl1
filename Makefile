install:
		poetry install

brain-games:
		poetry run brain-games

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		pipx install --force dist/*.whl

make lint:
		poetry run flake8 brain_games

brain-even:
		poetry run brain-even