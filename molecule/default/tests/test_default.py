import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('f',
                         ['boss__fact.fact'])
def test_packages_installed(host, f):
    path_to_fact = "/etc/ansible/facts.d/{}".format(f)
    fact_file = host.file(path_to_fact)
    assert fact_file.exists


def test_path_to_private_fact_ini(host):
    fact_file = host.file("/etc/ansible/boss__fact_priv.ini")
    assert fact_file.exists


def test_path_to_public_fact_ini(host):
    fact_file = host.file("/etc/ansible/boss__fact.ini")
    assert fact_file.exists

