import pytest

"""old variants:
@pytest.mark.api
def test_user_exists():
    api = GitHub()
    #user = api.get_user_defunkt()
    user = api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api    
def test_user_not_exists():
    api = GitHub()
    #r = api.get_not_exist_user()
    r = api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'
    """
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api    
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0    

@pytest.mark.api
def test_get_emojis(github_api):
    emojis = github_api.get_emojis()
    assert 'astronaut' in emojis
    assert emojis['astronaut'] == "https://github.githubassets.com/images/icons/emoji/unicode/1f9d1-1f680.png?v8"

@pytest.mark.api
def test_list_commits(github_api):
    commits = github_api.list_commits('NataliaShylina', 'Prometheus_HW')
    assert len(commits) > 0
    assert 'commit' in commits[0]
    assert 'sha' in commits[0]    

@pytest.mark.api
def test_get_repo_languages(github_api):
    languages = github_api.get_repo_languages('NataliaShylina', 'Prometheus_HW')
    assert 'Python' in languages or 'Java' in languages

@pytest.mark.api
def test_get_commit(github_api):
    commit = github_api.get_commit('NataliaShylina', 'Prometheus_HW', 'd96c4e1acbc8750987a157282d72855e53ceb06f')
    assert 'sha' in commit
    assert 'commit' in commit
    assert commit['sha'] == 'd96c4e1acbc8750987a157282d72855e53ceb06f'    