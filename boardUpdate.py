#!/usr/bin/env python

import sys
import ConfigParser

from trello import TrelloApi

config = ConfigParser.ConfigParser()
config.read("/Users/sam/.trello.ini")

trello = TrelloApi(config.get("trello", "app_key"), config.get("trello", "token"))
boardId = sys.argv[1]

# tokenUrl = trello.get_token_url('svs.boardUpdate', expires='30days', write_access=True)
# print "Please open this URL, then enter the token to proceed: ", tokenUrl
# token = input("Token:")

for list in trello.boards.get_list(boardId):
	member_card = dict()
	print "\n## Actions: %s" % list['name']

	for card in trello.lists.get_card(list['id']):
		for member in card['idMembers']:
			if not member_card.has_key(member):
				member_card[member] = []
			member_card[member].append(card)

	for memberId in member_card.keys():
		member = trello.members.get(memberId)
		print "\n### %s" % member['fullName']
		for card in member_card[memberId]:
			print "* [%s](%s)" % (card['name'], card['url'])

