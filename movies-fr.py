import os
import time
import sys
import internetarchive as ia
from internetarchive.session import ArchiveSession
from internetarchive import get_item
from internetarchive import download

search = ia.search_items('collection:%s' % sys.argv[1])

num = 0

for result in search: #for all items in a collection
	num = num + 1 #item count
	itemid = result['identifier']
	#title = get_item(itemid).item_metadata['metadata']['title']
	#language = get_item(itemid).item_metadata['metadata']['language']
	print('Downloading: #' + str(num) + '\t' + itemid)
	try:
		#download(itemid) 
		print(itemid)
		print('\t\t Download success.')
	except Exception as e:
		print("Error Occurred downloading () = {}".format(itemid, e))
	print('Pausing for 40 minutes')
	#time.sleep(2400)# IA restricts the number of things you can download. Be nice to 
			# their servers -- limit how much you download, too. For me, this
			# time restriction is still not polite enough, and my connection gets
			# cut off all the dang time.
    
    
    
