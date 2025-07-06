"""
Test runner script for Robot Framework tests
"""
import os
import sys
import argparse
# from pathlib import Path
from robot import run

def main():
    parser = argparse.ArgumentParser(description='Run Robot Framework tests')
    parser.add_argument('--env', default='dev', choices=['dev', 'staging', 'prod'],
                       help='Environment to run tests against')
    parser.add_argument('--browser', default='chrome', choices=['chrome', 'firefox', 'edge'],
                       help='Browser to use for testing')
    parser.add_argument('--headless', action='store_true',
                       help='Run browser in headless mode')
    parser.add_argument('--suite', help='Specific test suite to run')
    parser.add_argument('--test', help='Specific test to run')
    parser.add_argument('--tags', help='Tags to include/exclude (e.g., smoke AND NOT slow)')
    parser.add_argument('--parallel', type=int, default=1,
                       help='Number of parallel processes')
    parser.add_argument('--report-dir', default='reports',
                       help='Directory for test reports')

    args = parser.parse_args()

    # Set environment variables
    os.environ['TEST_ENV'] = args.env
    os.environ['BROWSER'] = args.browser
    os.environ['HEADLESS'] = str(args.headless).lower()

    # Prepare Robot Framework arguments
    robot_args = []

    # Output directory
    robot_args.extend(['--outputdir', args.report_dir])

    # Log level
    robot_args.extend(['--loglevel', 'INFO'])

    # Test selection
    if args.suite:
        robot_args.extend(['--suite', args.suite])

    if args.test:
        robot_args.extend(['--test', args.test])

    if args.tags:
        robot_args.extend(['--include', args.tags])

    # Parallel execution
    if args.parallel > 1:
        robot_args.extend(['--processes', str(args.parallel)])

    # Variables
    robot_args.extend(['--variable', f'BROWSER:{args.browser}'])
    robot_args.extend(['--variable', f'HEADLESS:{args.headless}'])

    # Test directory
    robot_args.append('tests')

    # Run tests
    try:
        return run(*robot_args)
    except Exception as e:
        print(f"Error running tests: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
