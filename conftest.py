# -*- coding: utf-8 -*-
# @Author  : Alex.Wang

import re

import pytest
from playwright.sync_api import Playwright, APIRequestContext
from pytest import fixture

from config.regex_express import RegexExpress
from config.urls import Urls


def regx_match(regex, content):
    return re.search(regex, content)


@fixture(scope="session")
def api_request_context(playwright: Playwright):

    browser = playwright.chromium.connect_over_cdp(
        endpoint_url="http://localhost:9222/"
    )
    context = browser.contexts[0]
    request_context = context.request
    yield request_context
    request_context.dispose()


@fixture(scope="session", autouse=True)
def env_init(api_request_context: APIRequestContext):

    sw_content = api_request_context.get(Urls.sw_js).text()
    home_content = api_request_context.get(Urls.home).text()

    main_version_candidate_1 = regx_match(RegexExpress.main_version, sw_content)
    main_version_candidate_2 = regx_match(RegexExpress.main_version, home_content)

    main_version_match = (
        main_version_candidate_1
        if main_version_candidate_1
        else main_version_candidate_2
        if main_version_candidate_2
        else None
    )

    if main_version_match:
        main_version = main_version_match.group(1)
    else:
        raise("Can't match main_js version")

    nft_version = regx_match(RegexExpress.nft_version, sw_content).group(1)

    nft_content = api_request_context.get(
        Urls.user_nft_js.format(nft_version=nft_version)
    ).text()
    main_content = api_request_context.get(
        Urls.main_js.format(main_version=main_version)
    ).text()

    user_nft_container_query_id = regx_match(
        RegexExpress.user_nft_container_query_id, nft_content
    ).group(1)
    user_by_screen_name_query_id = regx_match(
        RegexExpress.user_by_screen_name_query_id, main_content
    ).group(1)

    authorization = "Bearer " + regx_match(
        RegexExpress.bearer_token, main_content
    ).group(1)
    ss = api_request_context.storage_state()
    cookies = ss.get("cookies")
    csrf_token = (
        cookie.get("value")
        for cookie in cookies
        if cookie.get("name") == "ct0" and cookie.get("domain") == ".twitter.com"
    ).__next__()

    headers = {"authorization": authorization, "x-csrf-token": csrf_token}
    pytest.nft_version = nft_version
    pytest.twitter_headers = headers
    pytest.user_nft_query_url = Urls.user_nft_query.format(
        user_nft_container_query_id=user_nft_container_query_id
    )
    pytest.settings_url = Urls.settings
    pytest.twitter_screen_name_url = Urls.twitter_screen_name.format(
        user_by_screen_name_query_id=user_by_screen_name_query_id
    )
    pytest.minds_screen_name_url = Urls.minds_screen_name
