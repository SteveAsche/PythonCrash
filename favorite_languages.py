from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['pete'] = 'javascript'
favorite_languages['sophie'] = 'ruby'
favorite_languages['giles'] = 'cobol'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() +".")