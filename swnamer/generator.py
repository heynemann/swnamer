#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of swnamer.
# https://github.com/heynemann/swnamer

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

import sys
import argparse
import random

from swnamer.collections import PLANETS_LIST, SPECIES_LIST, CHARACTER_LIST


class NameGenerator(object):
    def __init__(self, use_characters=True, use_species=True, use_planets=True, separator='-', lowercase=False, seed=None):
        self.use_characters = use_characters
        self.use_species = use_species
        self.use_planets = use_planets
        self.separator = separator
        self.lowercase = lowercase

        if seed is not None:
            random.seed(seed)

    def generate(self):
        parts = []

        if self.use_planets:
            parts.append(self.separator.join(random.choice(PLANETS_LIST).split('-')))

        if self.use_species:
            parts.append(self.separator.join(random.choice(SPECIES_LIST).split('-')))

        if self.use_characters:
            parts.append(self.separator.join(random.choice(CHARACTER_LIST).split('-')))

        name = self.separator.join(parts)

        if self.lowercase:
            name = name.lower()

        return name


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('--without-planets', default=True, action='store_false')
    parser.add_argument('--without-species', default=True, action='store_false')
    parser.add_argument('--without-characters', default=True, action='store_false')
    parser.add_argument('--lower', default=False, action='store_true')
    parser.add_argument('--separator', default="-")
    arguments = parser.parse_args(args)

    generator = NameGenerator(
        use_planets=arguments.without_planets,
        use_species=arguments.without_species,
        use_characters=arguments.without_characters,
        separator=arguments.separator,
        lowercase=arguments.lower
    )

    print(generator.generate())
