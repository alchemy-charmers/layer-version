from charms.reactive import when, when_not, set_state
from charmhelpers.core.hookenv import application_version_set


@when_not('layer-version.installed')
def install_layer_version():
    with open('VERSION', 'r') as version:
        application_version_set(version.readline().strip())
    set_state('layer-version.installed')


@when('config.changed')
def update_version():
    with open('VERSION', 'r') as version:
        application_version_set(version.readline().strip())
