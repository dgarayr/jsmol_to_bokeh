from setuptools import setup,find_packages
setup(name='jsmol_to_bokeh',
      version='0.5',
      author="Diego Garay-Ruiz, Leopold Talirz",
      description="Bokeh extension for JSMol, adapted to support precompilation",
      install_requires="bokeh>=2.3.2<3.0.0",
      url="https://github.com/dgarayr/jsmol_to_bokeh",
      packages=find_packages()
)
