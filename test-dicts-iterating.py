

#
# Test iterating dicts
#


taxon_dict = {'9606': 'H. sapiens', '7955': 'D. rerio', '6239': 'C. elegans', '3702': 'A. thaliana', '7227': 'D. melanogaster', '284812': 'S. pombe', '559292': 'S. cerevisiae'}

for key in taxon_dict:
	print(f"This key is: {key}, This value is: {taxon_dict[key]}")