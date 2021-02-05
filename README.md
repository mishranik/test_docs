# package-template

### FILES DESCRIPTION
1. .gitignore

2. MANIFEST.in

3. README.md

4. setup.py

5. VERSION

6. CHANGELOG.md\
Changelog should be updated when a release candidate is cut from develop

7. fury.json\
Internal dependencies and their versions

8. RELEASENOTES.md\
RELEASENOTES should be updated when merging a release candidate to master

9. requirements.txt\
External dependencies with their versions

10. setup.cfg\
Test runner configurations



### GETTING STARTED

1. Create a new repository using the template

2. Update below mentioned configs in setup.py\
    * YOUR_PACKAGE_NAME_HERE - Package name
    * YOUR_DESCRIPTION_HERE - Package Description
    * YOUR_NAME - Author name
    * YOUR_EMAIL - Author email

3. Run python setup.py install


### DEPLOYMENT CONFIG
https://moengagetrial.atlassian.net/wiki/spaces/EN/pages/1067941917/Deployment+Template