#!/usr/bin/python

'''Adapted from https://developers.google.com/appengine/docs/python/tools/localunittesting
Some tests require webtest to be installed (see http://webtest.pythonpaste.org/en/latest/index.html#installation)
Some tests require jinja2 to be installed (see http://jinja.pocoo.org/docs/intro/)
'''

import optparse
import sys
import unittest

USAGE = """%prog [options]
Run unit tests for App Engine apps."""

def main(sdk_path, test_path, pattern):
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest.loader.TestLoader().discover(test_path, pattern=pattern)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    parser.add_option('-s', '--sdk_path', dest='sdk_path', help='Path to the SDK installation', default='/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine')
    parser.add_option('-t', '--test_path', dest='test_path', help='Path to package containing test modules', default='.')
    parser.add_option('-p', '--pattern', dest='pattern', help='Pattern to match test files', default='*_test.py')
    options, args = parser.parse_args()
    main(options.sdk_path, options.test_path, options.pattern)