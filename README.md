swnamer
=======

swnamer is a name generator that uses Star Wars characters, species and planets to create unique names.

Usage
-----

There are two ways of using swnamer. The first one is using the console app you get when installing it. The other is using the library in python code.

Installing is as simple as:

    $ pip install swnamer

Using with the console
----------------------

Console usage works like this:

    $ swnamer
    Nar-Shaddaa-Gamorrean-General-Grievous

These are all the available options:

    $ swnamer --without-planets --without-species --without-characters --separator="_" --lower

Please note that if you use all three --without flags, you'll get nothing in return.

Using as a library
------------------

Using in your python code is very simple:

    from swnamer import NameGenerator

    def create_a_server():
        generator = NameGenerator(lowercase=True, separator="_")
        return generator.generate()

This would return something like "nar-shaddaa-gamorrean-general-grievous".

These are all the available flags (and their defaults):

    use_characters=True
    use_species=True
    use_planets=True
    separator='-'
    lowercase=False
    seed=None

Contributing
------------

Fork, Commit, Pull Request.

License
-------

All star wars names and characters are property of their licensed owners.

Names retrieved from the following pages:

* http://en.wikipedia.org/wiki/List_of_Star_Wars_planets
* http://en.wikipedia.org/wiki/List_of_Star_Wars_species_(U%E2%80%93Z)
* http://en.wikipedia.org/wiki/List_of_Star_Wars_characters

The software is licensed under MIT.
