#!/usr/bin/python3

import internetarchive

# Search for items with the keyword "test"
search_results = internetarchive.search_items('test')

# Iterate through the search results and print the item identifiers
for result in search_results:
	print(result['identifier'])

# Search for items in the "audio" collection with the keyword "radio"
search_results = internetarchive.search_items('radio', collection='audio')

# Print the total number of search results
print(search_results.total)
