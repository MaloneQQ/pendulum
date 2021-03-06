# -*- coding: utf-8 -*-

from pendulum import Pendulum


class AbstractLocalizationTestCase(object):

    locale = None

    def setUp(self):
        Pendulum.set_locale(self.locale)

    def tearDown(self):
        Pendulum.set_locale('en')

    def test_diff_for_humans_localized(self):
        self.diff_for_humans()

    def diff_for_humans(self):
        raise NotImplementedError()
