import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['MacOS', 'Windows', 'Linux', 'Debian'])
def test_multiplication_of_number(browser: str, os: str):
    assert len(os + browser) > 0

#Параметризация фикстуры
@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest) -> str:
    return request.param

#Использование параметризированной фикстуры
def test_open_browser(browser: str):
    print(f'Opening browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_with_operations(self, user: str, account: str):
        print(f'User with operations: {user} with {account}')


    def test_without_operations(self, user: str):
        print(f'User without operations: {user}')


users = {
    '+70000000011': 'User with money on bank account',
    '+70000000022': 'User without money on bank account',
    '+70000000033': 'User with operations on bank account'
}


@pytest.mark.parametrize(
   'phone_number',
    users.keys(),
    ids= lambda phone_number: f'{phone_number}: {users[phone_number]}'
    )
def test_identifiers(phone_number: str):
    pass