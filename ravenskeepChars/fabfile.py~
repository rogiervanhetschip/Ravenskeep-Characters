from fabric.api import local
from fabric.api import lcd

def prepare_deployment(branch_name):
#    local('python manage.py test chars')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branchname)

def deploy():
    with lcd('/home/rogier/digi/ravenskeepChars'):
        local('git pull /home/rogier/digi/devRavenskeepChars')
        local('python manage.py migrate chars')
        local('python manage.py test chars')
        local('/my/command/to/restart/webserver')

