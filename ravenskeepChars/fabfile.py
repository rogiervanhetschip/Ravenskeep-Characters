from fabric.api import local
from fabric.api import lcd

def prepare_deployment(branch_name):
#    local('python manage.py test chars')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

def deploy():
    with lcd('/home/rogier/digi/ravenskeepChars'):
        local('git pull /home/rogier/digi/devRavenskeepChars')
        local('python manage.py migrate chars')
        local('python manage.py test chars')
        local('/my/command/to/restart/webserver')

def testdata():
    local('export SSLMODE=required')
# d71oban8h9igvg: dbname
    local('psql -h MyM09bY4cYT2Qs1D_N84aZbFWq@ec2-107-22-170-211.compute-1.amazonaws.com -U fpjmwxkyfisyzb d71oban8h9igvg')
