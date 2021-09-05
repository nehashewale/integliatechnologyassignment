from setuptools import setup, find_packages
setup(
      # If name is changed be sure to update the open file path above.
      name = "integliadb",
      version = "v0.1",
      packages = find_packages(),
      package_dir = {'integliadb':'integliadb'},
      author = 'Neha',
      author_email = 'nehashewale3010@gmail.com',
      descipriton = 'Database Layer access used across integliadb',
      license = "PSF",
      include_package_data = True,
      )