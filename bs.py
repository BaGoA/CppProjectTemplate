#!/usr/bin/python3

import argparse
import subprocess
import pathlib
import shutil

def get_build_dir(build_type: str) -> str:
    ''' Get build directory from build type '''
    return "build/" + build_type


def run_command(command: [str]) -> (bool, str):
    ''' Run command given in argument with subprocess '''
    completed_process = subprocess.run(command, capture_output=True, encoding="UTF-8")

    if completed_process.returncode < 0:
        # Error is occured in submission of subprocess
        return (False, f'Error is occured with code {completed_process.returncode} when submission of subprocess')

    if len(completed_process.stderr) > 0:
        # Error is occured in command run
        return (False, f'Error is occured when subprocess run: {completed_process.stderr}')

    return (True, completed_process.stdout)


def init(build_type: str):
    ''' Initialization of cmake project with ninja build system '''
    build_dir: str = get_build_dir(build_type)

    cmake_config_command = ["cmake", "-B", build_dir, "-G", "Ninja", "-DCMAKE_BUILD_TYPE=" + build_type, "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]
    _, message = run_command(cmake_config_command)

    print(message)


def build(build_type: str):
    ''' Build and install the project with cmake, previouly initialized '''
    build_dir: str = get_build_dir(build_type)

    cmake_build_command = ["cmake", "--build", build_dir]
    cmake_build_is_succeed, cmake_build_message = run_command(cmake_build_command)
    print(cmake_build_message)

    if cmake_build_is_succeed:
        cmake_install_command = ["cmake", "--install", build_dir]
        _, cmake_install_message = run_command(cmake_install_command)
        print(cmake_install_message)


def clean():
    ''' Remove build and bin directory '''
    build_dir: pathlib.Path = pathlib.Path("build")

    if build_dir.exists():
        shutil.rmtree(build_dir)

    bin_dir: pathlib.Path = pathlib.Path("bin")

    if bin_dir.exists():
        shutil.rmtree(bin_dir)

        
def main():
    parser = argparse.ArgumentParser(description='Build system for C++ project, based on CMake')
    parser_cmd = parser.add_subparsers(dest='command', required=True)

    # Create 'init' command to run project setup
    parser_init = parser_cmd.add_parser('init', help='Initialization of project')
    parser_init.add_argument('init_type', choices=['debug', 'release'], help='Type of build')

    # Create 'build' command to build project 
    parser_build = parser_cmd.add_parser('build', help='Build the project')
    parser_build.add_argument('build_type', choices=['debug', 'release'], help='Type of build')

    # Create 'clean' command to clean project 
    parser_build = parser_cmd.add_parser('clean', help='Clean the project')

    # Process command line arguments
    args = parser.parse_args()

    # Call command
    if args.command == 'init':
        init(args.init_type)
    elif args.command == 'build':
        build(args.build_type)
    elif args.command == 'clean':
        clean()
    else:
        print('Unknown command')

if __name__=='__main__':
    main()
    
