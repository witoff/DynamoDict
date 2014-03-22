from distutils.core import setup
    setup(
        name = 'dynamodict',
        packages = ['dynamodict', 'dynamodict.ddbd'], # this must be the same as the name above
        version = '0.2',
        description = 'A simple ORM that maps DynamoDB Tables to native python dicts',
        author = 'Rob Witoff',
        install_requires = ['boto>=2.25'],
        author_email = 'dynamodict@pspct.com',
        url = 'https://github.com/witoff/DynamoDict',   # use the URL to the github repo
        download_url = 'https://github.com/witoff/DynamoDict/tarball/0.1', # I'll explain this in a second
        keywords = ['dynamodb', 'orm', 'python'], # arbitrary keywords
        classifiers = [],
    )
