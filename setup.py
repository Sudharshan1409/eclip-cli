from setuptools import setup, find_packages

def load_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()
print(load_requirements('requirements.txt'))

print(find_packages())
setup (
    name = 'eclip',
    version = '0.0.1',
    description = 'CLI to delete all node_modules and venv folders in specified directory',
    author = 'Sudharshan V',
    author_email = 'sudarshan61kv@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires = load_requirements('requirements.txt'),
    entry_points = '''
        [console_scripts]
        eclip=eclip_cli.cli:cli
    ''',
)

