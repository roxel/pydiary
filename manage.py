from app import create_app
from app.database import db
from flask import url_for
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

app = create_app('config.ProductionConfig')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Routes(Command):

    help = description = 'Lists all route rules added to the app'

    def run(self):
        links = []
        for rule in app.url_map.iter_rules():
            # Filter out rules we can't navigate to in a browser
            # and rules that require parameters
            if "GET" in rule.methods and has_no_empty_params(rule):
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append((url, rule.endpoint))
                # links is now a list of url, endpoint tuples
        for l in links:
            print(l)

manager.add_command('routes', Routes)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


if __name__ == '__main__':
    manager.run()
