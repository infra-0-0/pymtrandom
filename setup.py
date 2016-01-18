from distutils.core import setup
setup(
    name='mtrandom',
    description='Pure Python Implementation of the Mersenne Twister PRNG',
    license='3-Clause BSD / PSF',
    version='1.0',
    author='Makoto Matsumoto and Takuji Nishimura, Jeff Miller',
    platforms='CrossPlatform',
    packages=['mtrandom'],
    scripts=['mtrandom/__init__.py', 'mtrandom/mtrandom.py']
)
