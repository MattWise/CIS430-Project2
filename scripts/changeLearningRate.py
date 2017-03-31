import os,re,argparse

import orange

def change_learning_rate(lr=0.05):
    lines_to_change=[216,428]
    replacement="learning_rate={}".format(lr)
    regex=re.compile(r"learning_rate\s*=\s*[0-9\.]*")
    path=os.path.dirname(orange.__file__)+"/projection/som.py"
    with open(path) as f:
        lines=f.readlines()
    for line in lines_to_change:
        lines[line]=regex.sub(replacement,lines[line])
    with open(path,'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("learning_rate", help="Learning rate to change to.", default=0.05, type=float)
    args = parser.parse_args()
    # change_learning_rate(args.learning_rate)
    change_learning_rate(0.01)