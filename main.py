from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'


print(style.BOLD + """
☆ *　. 　☆ 
　　. ∧＿∧　∩　* ☆ 
* ☆ ( ・∀・)/ . 
　. ⊂　　 ノ* ☆ 
☆ * (つ ノ .☆ 
　　 (ノ
""" + style.ENDC)

print(style.OKBLUE + 'Confcat' + style.ENDC + ' v.1.0')
print(style.UNDERLINE + 'Github: pomirs-workers/confcat' + style.ENDC)
print('Thank you for using!\n')

config_file = open('cc.yml', 'r')
config_str = config_file.read()
config_file.close()
config_dict = load(config_str, Loader=Loader)

print(style.BOLD + '--- ' + config_dict['name'] + ' ---' + style.ENDC)

questions = config_dict['questions']

gen = open(config_dict['out'], 'w')

for question in questions:
    print(question['text'] + ' ' + style.GRAY + '(' + question['default'] + ') ' + style.ENDC, end='')
    value = input()
    gen.write(question['bind'] + ': ' + (question['default'] if value == '' else value) + '\n')


gen.close()
print('Generating...')
print('Done!')

