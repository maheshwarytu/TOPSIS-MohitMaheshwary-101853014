from distutils.core import setup
setup(
  name = 'TOPSIS_MohitMaheshwary_101853014',
  packages = ['TOPSIS_MohitMaheshwary_101853014'],
  version = '1.0.0',  
  license='MIT', 
  description = 'Topsis score calculator',
  long_description=open("README.txt").read(),
  author = 'Mohit Maheshwary',
  author_email = 'mmaheshwary_be18@thapar.edu',
  url = 'https://github.com/maheshwarytu/TOPSIS-MohitMaheshwary-101853014',
  download_url = 'https://github.com/maheshwarytu/TOPSIS-MohitMaheshwary-101853014/archive/v_1.0.0.tar.gz',
  keywords = ['topsis', 'thapar', 'rank', 'topsis score'], 
  install_requires=["pandas"],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
