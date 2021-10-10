# sdm-phr
Provides an implementation of CP-ABE on the assignment for personal health records.

## Recommendations
1. ABE (2020) with Python 3.7 according to this installation: https://lrusso96.github.io/blog/cryptography/2021/03/04/charm-setup.html
2. open-ABE (2021) building CLI executables within a docker instance
4. Manually trying to copy and import files from https://github.com/JHUISI/charm/blob/dev/charm/toolbox/ to circumvent the library compile
3. Manually rebuilding existing libraries to replace the non-compiling and outdated cryptographic library

## Possible libraries found
These libraries are sorted on their popularity and how recent they have been updated.
- C++ (2021) (171 star): https://github.com/zeutro/openabe
- Rust (2021) (42 star): https://github.com/Fraunhofer-AISEC/rabe
- Python (2020) (90 star): https://github.com/sagrawal87/ABE
- Go (2020) (15 star): https://github.com/marcellop71/mosaic
- C++ (2020) (2 star): https://github.com/babbadeckl/ABE-RestAPI
- C (2020) (0 star): https://github.com/Juve45/abe-cas
- Java (2018) (10 star): https://github.com/rajatks/CP-ABE
- Python (2016) (17 star): https://github.com/jfdm/pyPEBEL

## Python 2020 (ABE)
We were unable to get this project to work as it required the charm-crypto library from 2011 which is incompatible with modern operating systems.

## C++ 2021 (open-ABE)
We were unable to compile this project as the Make process showed errors that we couldnt resolve.
