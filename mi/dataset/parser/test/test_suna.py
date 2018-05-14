import os
from nose.plugins.attrib import attr

from mi.core.log import get_logger
from mi.dataset.parser.utilities import particle_to_yml
from mi.dataset.driver.suna.resource import RESOURCE_PATH
from mi.dataset.test.test_parser import ParserUnitTestCase
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.parser.suna import SunaParser

from mi.dataset.driver.suna.suna_driver import MODULE_NAME, RECOVERED_PARTICLE_CLASS

log = get_logger()

@attr('UNIT', group='mi')
class SunaDclParserUnitTestCase(ParserUnitTestCase):

    def create_parser(self, particle_class, file_handle):
        """
        This function creates a MetbkADcl parser for recovered data.
        """
        parser = SunaParser(
            {DataSetDriverConfigKeys.PARTICLE_MODULE: MODULE_NAME,
             DataSetDriverConfigKeys.PARTICLE_CLASS: particle_class},
            file_handle,
            self.exception_callback)
        return parser

    def open_file(self, filename):
        my_file = open(os.path.join(RESOURCE_PATH, filename), mode='r')
        return my_file

    def setUp(self):
        ParserUnitTestCase.setUp(self)

    def create_yml(self, particles, filename):
        particle_to_yml(particles, os.path.join(RESOURCE_PATH, filename))

    def test_good_dcl(self):
        """
        Test dcl with good data
        """
        log.debug("Running test_happy_path")

        filename = "dcl_good.log"

        with open(os.path.join(RESOURCE_PATH, filename), 'r') as file_handle:

            parser = self.create_parser(RECOVERED_PARTICLE_CLASS, file_handle)

            particles = parser.get_records(1000)
            particle_to_yml(particles, os.path.join(RESOURCE_PATH, 'dcl_good.yml'))
            log.debug("Num particles: %d", len(particles))

            self.assertEqual(len(particles), 144)

    def test_bad_dcl(self):
        """
        Test dcl with some good data, and some bad data (4 of them)
        """
        log.debug("Running test_happy_path")

        filename = "dcl_bad.log"

        with open(os.path.join(RESOURCE_PATH, filename), 'r') as file_handle:

            parser = self.create_parser(RECOVERED_PARTICLE_CLASS, file_handle)

            particles = parser.get_records(1000)
            particle_to_yml(particles, os.path.join(RESOURCE_PATH, 'dcl_bad.yml'))
            log.debug("Num particles: %d", len(particles))

            self.assertEqual(len(particles), 140)

    def test_good_instrument_recovered(self):
        """
        Test instrument recovered with some good data
        """
        log.debug("Running test_happy_path")

        filename = "instrument_recovered_good.CSV"

        with open(os.path.join(RESOURCE_PATH, filename), 'r') as file_handle:

            parser = self.create_parser(RECOVERED_PARTICLE_CLASS, file_handle)

            particles = parser.get_records(1000)
            particle_to_yml(particles, os.path.join(RESOURCE_PATH, 'instrument_recovered_good.yml'))
            log.debug("Num particles: %d", len(particles))

            self.assertEqual(len(particles), 39)

    def test_bad_instrument_recovered(self):
        """
        Test instrument recovered with some bad data (
        """
        log.debug("Running test_happy_path")

        filename = "instrument_recovered_bad.CSV"

        with open(os.path.join(RESOURCE_PATH, filename), 'r') as file_handle:

            parser = self.create_parser(RECOVERED_PARTICLE_CLASS, file_handle)

            particles = parser.get_records(100)
            particle_to_yml(particles, os.path.join(RESOURCE_PATH, '.yml'))
            log.debug("Num particles: %d", len(particles))

            self.assertEqual(len(particles), 35)
