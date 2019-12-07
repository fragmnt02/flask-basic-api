Learn more or give us feedback
from flask_api import FlaskAPI, exceptions
from person import Person

api = FlaskAPI(__name__)


@api.route("/<int:index>", endpoint='get_name', methods=['GET'])
def get_name(index):
    try:
        new_person = Person(key)
        return new_person.get_name()
    except:
        raise exceptions.NotFound()


@api.route("/age/<int:key>", endpoint='get_age', methods=['GET'])
def get_age(key):
    try:
        new_person = Person(key)
        return new_person.get_age()
    except:
        raise exceptions.NotFound()


@api.route("/company/<int:key>", endpoint='get_company', methods=['GET'])
def get_company(key):
    try:
        new_person = Person(key)
        return new_person.get_company()
    except:
        raise exceptions.NotFound()

if __name__ == '__main__':
    api.run()