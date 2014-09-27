#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of swnamer.
# https://github.com/heynemann/swnamer

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

import random
from StringIO import StringIO

from preggy import expect
from mock import patch

from swnamer import NameGenerator
from swnamer.generator import main
from tests.base import TestCase


class NameGeneratorTestCase(TestCase):
    def test_can_generate_names(self):
        generator = NameGenerator(seed="test-1")
        expect(generator.generate()).to_equal("Rori-Latter-Ponda-Baba")

    def test_can_generate_names_without_characters(self):
        generator = NameGenerator(use_characters=False, seed="test-2")
        expect(generator.generate()).to_equal("Utapau-Yaka")

    def test_can_generate_lowercase_name(self):
        generator = NameGenerator(lowercase=True, seed="test-3")
        expect(generator.generate()).to_equal("centax-1-bouncer-thire")

    def test_can_generate_names_without_characters_and_species(self):
        generator = NameGenerator(use_characters=False, use_species=False, seed="test-4")
        expect(generator.generate()).to_equal("Taanab")

    def test_can_generate_names_without_species(self):
        generator = NameGenerator(use_species=False, seed="test-5")
        expect(generator.generate()).to_equal("Corellia-Rush-Clovis")

    @patch('sys.stdout', new_callable=StringIO)
    def test_can_call_main(self, mock_stdout):
        random.seed('test-6')
        main(['--lower'])
        expect(mock_stdout.getvalue()).to_be_like('iego-askajian-corde')
