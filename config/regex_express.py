# -*- coding: utf-8 -*-
# @Author  : Alex.Wang

class RegexExpress:

	main_version = r"/client-web/main.(.*?)\.js"
	nft_version = r"/client-web/bundle.UserNft.(.*?)\.js"
	user_nft_container_query_id = r"id:\"(\w+)"
	user_by_screen_name_query_id = r"queryId:\"(.{22})\",operationName:\"UserByScreenName\","
	bearer_token = r"(AAAAA.*?)\""


