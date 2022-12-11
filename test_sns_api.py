# -*- coding: utf-8 -*-
# @Author  : Alex.Wang

import pytest
from playwright.sync_api import APIRequestContext


def test_twitter_getUserNftContainer(api_request_context: APIRequestContext):
    # getUserNftContainer
    params = {
        "variables": '{"screenName":"suji_yan"}',
        "features": '{"responsive_web_twitter_blue_verified_badge_is_enabled":false}',
    }
    response = api_request_context.get(
        url=pytest.user_nft_query_url,
        headers=pytest.twitter_headers,
        params=params,
    )
    print(response.url)
    assert response.status == 200


def test_twitter_getSettings(api_request_context: APIRequestContext):
    # getSettings
    params = {
        "include_mention_filter": False,
        "include_nsfw_user_flag": False,
        "include_nsfw_admin_flag": False,
        "include_ranked_timeline": False,
        "include_alt_text_compose": False,
        "include_country_code": False,
        "include_ext_dm_nsfw_media_filter": False,
    }
    response = api_request_context.get(
        pytest.settings_url,
        headers=pytest.twitter_headers,
        params=params,
    )
    print(response.url)
    assert response.status == 200


def test_twitter_getUserByScreenName(api_request_context: APIRequestContext):
    # getUserByScreenName
    params = {
        "variables": '{"screen_name":"suji_yan",'
        '"withSafetyModeUserFields":true,'
        '"withSuperFollowsUserFields":true}',
        "features": '{"responsive_web_twitter_blue_verified_badge_is_enabled":false,'
        '"verified_phone_label_enabled":false,'
        '"responsive_web_graphql_timeline_navigation_enabled":true,'
        '"responsive_web_twitter_blue_new_verification_copy_is_enabled":false}',
    }
    response = api_request_context.get(
        pytest.twitter_screen_name_url,
        headers=pytest.twitter_headers,
        params=params,
    )
    print(response.url)
    assert response.status == 200


def test_minds_getUserByScreenName(api_request_context: APIRequestContext):
    # getUserByScreenName
    response = api_request_context.get(pytest.minds_screen_name_url)
    print(response.url)
    assert response.status == 200
