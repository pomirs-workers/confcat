from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'


print(Style.BOLD + """
☆ *　. 　☆ 
　　. ∧＿∧　∩　* ☆ 
* ☆ ( ・∀・)/ . 
　. ⊂　　 ノ* ☆ 
☆ * (つ ノ .☆ 
　　 (ノ
""" + Style.ENDC)

print(Style.OKBLUE + 'Confcat' + Style.ENDC + ' v.1.0')
print('Github: ' + Style.UNDERLINE + 'pomirs-workers/confcat' + Style.ENDC)
print('Thank you for using!\n')

config_file = open('cc.yml', 'r')
config_str = config_file.read()
config_file.close()
config_dict = load(config_str, Loader=Loader)

print(Style.BOLD + '--- ' + config_dict['name'] + ' ---' + Style.ENDC)

questions = config_dict['questions']

gen = open(config_dict['out'], 'w')

for question in questions:
    if question['type'] == 'common':
        print(question['text'] + ' ' + Style.GRAY + '(' + question['default'] + ') ' + Style.ENDC, end='')
        value = input()
        gen.write(question['bind'] + ': ' + (question['default'] if value == '' else value) + '\n')
    elif question['type'] == 'yesno':
        print(question['text'] + ' ' + Style.GRAY + '[Y/n] ' + Style.ENDC, end='')
        yes = {'yes', 'y', 'ye', ''}
        no = {'no', 'n'}
        value = input().lower()
        if value in yes:
            gen.write(question['bind'] + ': ' + str(question['yv'] if 'yv' in question is not None else 1) + '\n')
        elif value in no:
            gen.write(question['bind'] + ': ' + str(question['nv'] if 'nv' in question is not None else 0) + '\n')
        else:
            print(Style.FAIL + "Please respond with 'yes' or 'no'" + Style.ENDC)
            exit(1)


gen.close()
print('Generating...')
print('Done!')
print('Check ' + Style.OKGREEN + config_dict['out'] + Style.ENDC)

